import os
from dotenv import load_dotenv

try:
    import google.generativeai as genai
except ImportError:
    genai = None

# --------------------------------------------------
# Load environment variables from .env (local only)
# --------------------------------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

_MODEL = None


def _get_model():
    """
    Lazily initialize Gemini model.
    Avoids import / config side effects at startup.
    """
    global _MODEL

    if _MODEL is not None:
        return _MODEL

    if genai is None:
        raise RuntimeError(
            "google-generativeai is not installed. "
            "Install it to enable Gemini support."
        )

    if not GEMINI_API_KEY:
        raise RuntimeError(
            "Gemini is enabled but GEMINI_API_KEY "
            "is missing in the .env file."
        )

    genai.configure(api_key=GEMINI_API_KEY)
    _MODEL = genai.GenerativeModel("gemini-1.5-flash")
    return _MODEL


def gemini_cleanup(text: str) -> str:
    """
    SAFE Gemini usage:
    - Formatting cleanup only
    - No inference
    - No summarization
    - No content addition or removal
    """

    model = _get_model()

    prompt = f"""
You are a STRICT text formatter.

Rules:
- DO NOT add content
- DO NOT remove content
- DO NOT infer meaning
- DO NOT summarize
- DO NOT reorder text
- Preserve wording EXACTLY
- Fix spacing and line-break issues only

Text:
{text}
"""

    response = model.generate_content(prompt)

    if not response or not response.text:
        return text

    return response.text.strip()
