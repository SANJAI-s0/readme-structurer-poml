# ==========================================================
# Single-File Core Project Extractor
# ----------------------------------------------------------
# This script:
# - Contains embedded XML blueprint
# - Extracts a lightweight project kernel
# - Creates exactly:
#     - one Python file
#     - one XML file
# ==========================================================

# ---------------------------
# Configuration
# ---------------------------
$ProjectRoot = "light-project"
$CorePythonFile = "core.py"
$CoreXmlFile = "core_rules.xml"

# ---------------------------
# Embedded Blueprint (XML)
# ---------------------------
$BlueprintXml = @'
<?xml version="1.0" encoding="utf-8"?>
<project name="light-core" version="0.1.0">

  <files>

    <file path="core.py">
<![CDATA[
import xml.etree.ElementTree as ET

def load_rules(path: str):
    """
    Load core XML rules.
    This is the lightweight kernel of the project.
    """
    tree = ET.parse(path)
    root = tree.getroot()
    return [e.get("name") for e in root.findall(".//section")]

if __name__ == "__main__":
    rules = load_rules("core_rules.xml")
    print("Loaded sections:")
    for r in rules:
        print("-", r)
]]>
    </file>

    <file path="core_rules.xml">
<![CDATA[
<rules>
  <sections>
    <section name="Title"/>
    <section name="Description"/>
    <section name="Usage"/>
  </sections>
</rules>
]]>
    </file>

  </files>
</project>
'@

# ---------------------------
# Load XML from embedded string
# ---------------------------
[xml]$xml = $BlueprintXml

# ---------------------------
# Create project root
# ---------------------------
New-Item -ItemType Directory -Name $ProjectRoot -Force | Out-Null
Set-Location $ProjectRoot

Write-Host "📦 Creating lightweight core project:"
Write-Host "📁 $ProjectRoot"
Write-Host ""

# ---------------------------
# Emit only core files
# ---------------------------
foreach ($file in $xml.project.files.file) {
    $path = $file.path
    $content = $file.'#cdata-section'

    if (-not $content) {
        Write-Warning "Skipping empty file: $path"
        continue
    }

    Set-Content -Path $path -Value $content.Trim() -Encoding UTF8
    Write-Host "✔ Created $path"
}

Write-Host ""
Write-Host "✅ Lightweight core project created successfully."
Write-Host "ℹ️  Files generated: $CorePythonFile, $CoreXmlFile"
