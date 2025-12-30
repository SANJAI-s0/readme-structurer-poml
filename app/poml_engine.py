import xml.etree.ElementTree as ET

def load_poml(path):
    tree = ET.parse(path)
    root = tree.getroot()

    ordered_sections = []
    alias_map = {}

    for sec in root.findall(".//output/sections/section"):
        name = sec.get("name")
        ordered_sections.append(name)
        alias_map[name.lower()] = name

        for alias in sec.findall("alias"):
            alias_map[alias.text.strip().lower()] = name

    return ordered_sections, alias_map
