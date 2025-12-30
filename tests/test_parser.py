from app.parser import flatten_json

def test_flatten_json_simple():
    data = {
        "Title": "Demo",
        "Features": ["A", "B"]
    }

    lines = flatten_json(data)

    assert "Title: Demo" in lines
    assert "- A" in lines
    assert "- B" in lines
