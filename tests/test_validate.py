from awesome_cl.validate import validate_papers, validate_taxonomy


def test_taxonomy_rejects_duplicate_id():
    item = {"id": "memory", "name": "Memory", "name_zh": "记忆", "description": "x"}
    assert any("duplicate id" in error for error in validate_taxonomy([item, item]))


def test_paper_rejects_unknown_topic_and_enum():
    paper = {
        "id": "p1", "title": "Example", "year": 2026, "status": "draft",
        "topics": ["unknown"], "paper_url": "https://example.org/paper", "priority": "P3",
        "evidence_level": "D", "why_read": "Test", "added": "2026-01-01",
        "last_verified": "2026-01-01",
    }
    errors = validate_papers([paper], {"memory"})
    assert any("unknown topics" in error for error in errors)
    assert any("invalid status" in error for error in errors)
    assert any("invalid priority" in error for error in errors)


def test_paper_rejects_duplicate_url():
    base = {
        "title": "Example", "year": 2026, "status": "preprint", "topics": ["memory"],
        "paper_url": "https://example.org/paper/", "priority": "P1", "evidence_level": "B",
        "why_read": "Test", "added": "2026-01-01", "last_verified": "2026-01-01",
    }
    errors = validate_papers([{**base, "id": "p1"}, {**base, "id": "p2", "paper_url": "https://example.org/paper"}], {"memory"})
    assert any("duplicate URL" in error for error in errors)
