from awesome_cl.render import render_readme


def test_render_is_deterministic_and_preserves_outside_text():
    template = "before\n<!-- PAPERS:START -->\nold\n<!-- PAPERS:END -->\n<!-- INDUSTRY:START -->\nold\n<!-- INDUSTRY:END -->\nafter\n"
    taxonomy = [{"id": "memory", "name": "Memory", "name_zh": "记忆"}]
    papers = [{"title": "Paper", "year": 2026, "status": "preprint", "topics": ["memory"], "paper_url": "https://example.org", "priority": "P0", "evidence_level": "B", "why_read": "Useful"}]
    industry = [{"name": "Tool", "organization": "Org", "kind": "open-source", "url": "https://example.org/tool", "evidence_level": "B", "summary": "Summary", "caveat": "Caveat"}]
    first = render_readme(template, papers, industry, taxonomy, "en")
    second = render_readme(first, papers, industry, taxonomy, "en")
    assert first == second
    assert first.startswith("before\n") and first.endswith("after\n")
    assert "[Paper](https://example.org)" in first
