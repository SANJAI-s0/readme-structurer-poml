from app.formatter import structure_text, format_markdown

def test_formatter_basic():
    text = """
    Title
    Demo Project

    Features
    Fast
    Simple
    """

    sections = ["Title", "Features"]
    aliases = {"title": "Title", "features": "Features"}

    buckets = structure_text(text, sections, aliases)
    result = format_markdown(buckets, sections)

    assert "## Title" in result
    assert "Demo Project" in result
    assert "## Features" in result
