"""Validation rules for curated data."""

from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from .load import load_yaml_list
from .model import EVIDENCE_LEVELS, INDUSTRY_KINDS, PAPER_STATUSES, PRIORITIES, normalize_url

TAXONOMY_FIELDS = {"id", "name", "name_zh", "description"}
PAPER_FIELDS = {
    "id", "title", "year", "status", "topics", "paper_url", "priority",
    "evidence_level", "why_read", "added", "last_verified",
}
INDUSTRY_FIELDS = {
    "id", "name", "organization", "kind", "topics", "url", "evidence_level",
    "summary", "caveat", "added", "last_verified",
}


def _missing(item: dict[str, Any], required: set[str]) -> set[str]:
    return {field for field in required if field not in item or item[field] in (None, "", [])}


def _valid_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def _valid_date(value: Any) -> bool:
    try:
        date.fromisoformat(str(value))
        return True
    except ValueError:
        return False


def validate_taxonomy(items: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(items, 1):
        label = item.get("id", f"item-{index}")
        missing = _missing(item, TAXONOMY_FIELDS)
        if missing:
            errors.append(f"taxonomy {label}: missing {', '.join(sorted(missing))}")
        if label in seen:
            errors.append(f"taxonomy {label}: duplicate id")
        seen.add(label)
    return errors


def _validate_common(
    items: list[dict[str, Any]], required: set[str], taxonomy_ids: set[str], url_field: str, kind: str
) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    for index, item in enumerate(items, 1):
        label = str(item.get("id", f"item-{index}"))
        missing = _missing(item, required)
        if missing:
            errors.append(f"{kind} {label}: missing {', '.join(sorted(missing))}")
        if label in seen_ids:
            errors.append(f"{kind} {label}: duplicate id")
        seen_ids.add(label)
        url = item.get(url_field)
        if not _valid_url(url):
            errors.append(f"{kind} {label}: {url_field} must be an https URL")
        else:
            normalized = normalize_url(url)
            if normalized in seen_urls:
                errors.append(f"{kind} {label}: duplicate URL")
            seen_urls.add(normalized)
        topics = item.get("topics", [])
        unknown = set(topics if isinstance(topics, list) else []) - taxonomy_ids
        if not isinstance(topics, list) or not topics:
            errors.append(f"{kind} {label}: topics must be a non-empty list")
        if unknown:
            errors.append(f"{kind} {label}: unknown topics {', '.join(sorted(unknown))}")
        if item.get("evidence_level") not in EVIDENCE_LEVELS:
            errors.append(f"{kind} {label}: invalid evidence_level")
        for field in ("added", "last_verified"):
            if field in item and not _valid_date(item[field]):
                errors.append(f"{kind} {label}: {field} must be YYYY-MM-DD")
    return errors


def validate_papers(items: list[dict[str, Any]], taxonomy_ids: set[str]) -> list[str]:
    errors = _validate_common(items, PAPER_FIELDS, taxonomy_ids, "paper_url", "paper")
    for item in items:
        label = item.get("id", "unknown")
        if item.get("status") not in PAPER_STATUSES:
            errors.append(f"paper {label}: invalid status")
        if item.get("priority") not in PRIORITIES:
            errors.append(f"paper {label}: invalid priority")
        year = item.get("year")
        if not isinstance(year, int) or not 2000 <= year <= 2100:
            errors.append(f"paper {label}: invalid year")
    return errors


def validate_industry(items: list[dict[str, Any]], taxonomy_ids: set[str]) -> list[str]:
    errors = _validate_common(items, INDUSTRY_FIELDS, taxonomy_ids, "url", "industry")
    for item in items:
        if item.get("kind") not in INDUSTRY_KINDS:
            errors.append(f"industry {item.get('id', 'unknown')}: invalid kind")
    return errors


def validate_all(root: str | Path) -> list[str]:
    root = Path(root)
    taxonomy = load_yaml_list(root / "data/taxonomy.yaml")
    papers = load_yaml_list(root / "data/papers.yaml")
    industry = load_yaml_list(root / "data/industry.yaml")
    errors = validate_taxonomy(taxonomy)
    taxonomy_ids = {item.get("id") for item in taxonomy if item.get("id")}
    errors.extend(validate_papers(papers, taxonomy_ids))
    errors.extend(validate_industry(industry, taxonomy_ids))
    return errors
