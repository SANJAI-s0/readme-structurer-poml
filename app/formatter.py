import re
from collections import defaultdict

def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", text.lower()).strip()


def clean_json_line(line: str) -> str:
    line = line.strip()

    if line.startswith('"') and line.endswith('"'):
        line = line[1:-1]

    line = line.replace('": "', ': ')
    line = line.replace('":"', ': ')
    line = line.replace('":', ': ')
    line = line.replace('",', '')
    line = line.replace('"', '')

    return line.strip()


def structure_text(text, ordered_sections, alias_map):
    buckets = defaultdict(list)
    current = None

    for line in text.splitlines():
        clean = line.strip()
        if not clean:
            continue

        key = normalize(clean)
        if key in alias_map:
            current = alias_map[key]
            continue

        if current and clean not in ("{", "}"):
            cleaned = clean_json_line(clean)
            if cleaned:
                buckets[current].append(cleaned)

    return buckets


def format_markdown(buckets, ordered_sections):
    output = []
    for section in ordered_sections:
        if section in buckets:
            output.append(f"## {section}")
            output.extend(buckets[section])
            output.append("")
    return "\n".join(output).strip()
