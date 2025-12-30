def main():
    import streamlit as st
    import json

    from app.poml_engine import load_poml
    from app.parser import extract_text, flatten_json
    from app.formatter import structure_text, format_markdown
    from app.ui_helpers import sidebar, footer
    from app.ai_preprocessor import gemini_cleanup

    st.set_page_config(
        page_title="POML README Structurer",
        layout="wide"
    )

    sidebar()
    st.title("📘 POML README Structurer")

    ordered_sections, alias_map = load_poml("config/poml_rules.xml")

    use_gemini = st.checkbox(
        "Enable Gemini (formatting cleanup only — no inference)",
        value=False
    )

    uploaded = st.file_uploader(
        "Upload file (txt, json, pdf, docx, rtf, html, xml)",
        type=["txt","md","json","pdf","docx","rtf","html","htm","xml"]
    )

    text_input = st.text_area("Or paste text / JSON", height=300)

    if st.button("Structure README"):
        raw_text = ""

        if uploaded:
            raw_text = extract_text(uploaded)
        elif text_input.strip():
            try:
                raw_text = "\n".join(flatten_json(json.loads(text_input)))
            except Exception:
                raw_text = text_input.strip()

        if not raw_text.strip():
            st.warning("Please provide input.")
            st.stop()

        if use_gemini:
            raw_text = gemini_cleanup(raw_text)

        buckets = structure_text(raw_text, ordered_sections, alias_map)
        result = format_markdown(buckets, ordered_sections)

        st.subheader("Structured README (Markdown)")
        st.code(result, language="markdown")

        st.subheader("Preview")
        st.markdown(result)

        st.download_button(
            "Download README.md",
            result.encode("utf-8"),
            "README.md",
            "text/markdown"
        )

    footer()
