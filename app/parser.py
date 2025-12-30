import io
import json
from PyPDF2 import PdfReader
import docx
from bs4 import BeautifulSoup

try:
    from striprtf.striprtf import rtf_to_text
except Exception:
    rtf_to_text = None


# --------------------------------------------------
# JSON → Plain text flattening (README-friendly)
# --------------------------------------------------
def flatten_json(obj, indent=0):
    """
    Convert JSON into readable plain text.
    - Dicts: Key: Value
    - Lists: - Item
    - Nested objects expanded line-by-line
    """
    lines = []
    prefix = "  " * indent

    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{prefix}{k}")
                lines.extend(flatten_json(v, indent + 1))
            else:
                lines.append(f"{prefix}{k}: {v}")

    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, (dict, list)):
                lines.extend(flatten_json(item, indent))
            else:
                lines.append(f"{prefix}- {item}")

    return lines


# --------------------------------------------------
# Universal file text extraction
# --------------------------------------------------
def extract_text(file):
    """
    Extract readable text from supported file types:
    TXT, JSON, PDF, DOCX, RTF, HTML, XML
    """
    name = file.name.lower()
    raw = file.read()
    buf = io.BytesIO(raw)

    # ---------------------------
    # JSON
    # ---------------------------
    if name.endswith(".json"):
        data = json.loads(raw.decode(errors="ignore"))
        return "\n".join(flatten_json(data))

    # ---------------------------
    # PDF
    # ---------------------------
    if name.endswith(".pdf"):
        reader = PdfReader(buf)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    # ---------------------------
    # DOCX
    # ---------------------------
    if name.endswith(".docx"):
        doc = docx.Document(buf)
        return "\n".join(p.text for p in doc.paragraphs if p.text)

    # ---------------------------
    # RTF
    # ---------------------------
    if name.endswith(".rtf"):
        text = raw.decode(errors="ignore")
        return rtf_to_text(text) if rtf_to_text else text

    # ---------------------------
    # HTML
    # ---------------------------
    if name.endswith((".html", ".htm")):
        soup = BeautifulSoup(raw.decode(errors="ignore"), "html.parser")
        tags = soup.find_all(["h1", "h2", "h3", "p", "li"])
        return "\n".join(t.get_text(strip=True) for t in tags)

    # ---------------------------
    # XML (FLATTENED — NO TAGS)
    # ---------------------------
    if name.endswith(".xml"):
        soup = BeautifulSoup(raw.decode(errors="ignore"), "xml")

        lines = []
        for elem in soup.find_all():
            if elem.string and elem.string.strip():
                lines.append(elem.string.strip())

        return "\n".join(lines)

    # ---------------------------
    # TXT / fallback
    # ---------------------------
    return raw.decode(errors="ignore")
