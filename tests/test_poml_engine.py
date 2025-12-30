from app.poml_engine import load_poml

def test_load_poml():
    sections, aliases = load_poml("config/poml_rules.xml")

    assert "Title" in sections
    assert aliases["title"] == "Title"
    assert aliases["architecture"] == "Architecture"
