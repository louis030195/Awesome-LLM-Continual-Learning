"""Shared schema constants and normalization."""

from urllib.parse import urlsplit, urlunsplit

PAPER_STATUSES = {"preprint", "published", "accepted", "withdrawn"}
PRIORITIES = {"P0", "P1", "P2"}
EVIDENCE_LEVELS = {"A", "B", "C"}
INDUSTRY_KINDS = {"open-source", "product", "platform", "research-release"}


def normalize_url(url: str) -> str:
    """Normalize scheme/host and remove fragments/trailing slash for duplicate checks."""
    parts = urlsplit(url.strip())
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))
