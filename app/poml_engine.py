import xml.etree.ElementTree as ET
from pathlib import Path


def load_poml(path: str):
    """
    Load POML rules safely using a project-root-relative path.
    """
    path = Path(path)

    # Resolve relative to project root
    if not path.is_absolute():
        project_root = Path(__file__).resolve().parent.parent
        path = project_root / path

    tree = ET.parse(path)
    root = tree.getroot()

    ordered_sections = []
    alias_map = {}

    for sec in root.findall(".//output/sections/section"):
        name = sec.get("name")
        ordered_sections.append(name)
        alias_map[name.lower()] = name

        for alias in sec.findall("alias"):
            alias_map[
                alias.text.strip().lower()
            ] = name

    return ordered_sections, alias_map
