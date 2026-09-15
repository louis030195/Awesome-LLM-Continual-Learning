"""Deterministic Markdown rendering for managed README sections."""

from collections import defaultdict
from typing import Any

PAPERS_START = "<!-- PAPERS:START -->"
PAPERS_END = "<!-- PAPERS:END -->"
INDUSTRY_START = "<!-- INDUSTRY:START -->"
INDUSTRY_END = "<!-- INDUSTRY:END -->"


def _escape(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def _replace_managed(text: str, start: str, end: str, content: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"expected exactly one marker pair: {start}, {end}")
    before, remainder = text.split(start, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{start}\n{content.rstrip()}\n{end}{after}"


def render_papers(papers: list[dict[str, Any]], taxonomy: list[dict[str, Any]], language: str) -> str:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for paper in papers:
        grouped[paper["topics"][0]].append(paper)
    sections: list[str] = []
    for topic in taxonomy:
        rows = sorted(grouped.get(topic["id"], []), key=lambda p: (-p["year"], p["title"].lower()))
        if not rows:
            continue
        heading = topic["name_zh"] if language == "zh" else topic["name"]
        sections.extend([
            f"### {heading}", "",
            "| Year | Paper | Status | Priority | Evidence | Why read |",
            "|---:|---|---|:---:|:---:|---|",
        ])
        for paper in rows:
            link = f"[{_escape(paper['title'])}]({paper['paper_url']})"
            sections.append(
                f"| {paper['year']} | {link} | {_escape(paper['status'])} | {paper['priority']} | {paper['evidence_level']} | {_escape(paper['why_read'])} |"
            )
        sections.append("")
    return "\n".join(sections)


def render_industry(items: list[dict[str, Any]]) -> str:
    lines = [
        "| Project | Organization | Kind | Evidence | Summary | Caveat |",
        "|---|---|---|:---:|---|---|",
    ]
    for item in sorted(items, key=lambda value: value["name"].lower()):
        link = f"[{_escape(item['name'])}]({item['url']})"
        lines.append(
            f"| {link} | {_escape(item['organization'])} | {_escape(item['kind'])} | {item['evidence_level']} | {_escape(item['summary'])} | {_escape(item['caveat'])} |"
        )
    return "\n".join(lines)


def render_readme(
    template: str,
    papers: list[dict[str, Any]],
    industry: list[dict[str, Any]],
    taxonomy: list[dict[str, Any]],
    language: str,
) -> str:
    rendered = _replace_managed(template, PAPERS_START, PAPERS_END, render_papers(papers, taxonomy, language))
    return _replace_managed(rendered, INDUSTRY_START, INDUSTRY_END, render_industry(industry))
