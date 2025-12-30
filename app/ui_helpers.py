import streamlit as st
from datetime import datetime
import os
from importlib.metadata import version, PackageNotFoundError

# --------------------------------------------------
# App / Repo metadata
# --------------------------------------------------
AUTHOR = "Sanjai"
REPO_URL = "https://github.com/<your-username>/readme-structurer-poml"
RELEASES_URL = f"{REPO_URL}/releases"

# --------------------------------------------------
# Build metadata (Docker / CI)
# --------------------------------------------------
BUILD_TIME = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
GIT_COMMIT = os.getenv("GIT_COMMIT", "local")
ENV_VERSION = os.getenv("APP_VERSION")


def get_app_version() -> str:
    """
    Resolve application version in this order:
    1. APP_VERSION env var (Docker / CI)
    2. pyproject.toml package version
    3. fallback to 'dev'
    """
    if ENV_VERSION:
        return ENV_VERSION

    try:
        return version("poml-readme-structurer")
    except PackageNotFoundError:
        return "dev"


def sidebar():
    st.sidebar.title("POML README Structurer")
    st.sidebar.markdown(
        """
- POML-controlled logic  
- Supports TXT / JSON / PDF / DOCX / RTF / HTML / XML  
- No inference or hallucination  
        """
    )


def footer():
    """
    Footer with:
    - Auto-updating year
    - GitHub + Releases links
    - Version (Docker / CI / pyproject)
    - Commit hash
    - Build timestamp
    - Dark / light theme adaptive styling
    """
    year = datetime.now().year
    app_version = get_app_version()

    st.markdown(
        f"""
        <hr style="margin-top: 2.5rem; margin-bottom: 1rem;" />

        <div style="
            text-align: center;
            font-size: 0.85rem;
            color: var(--text-color);
        ">
            © {year} {AUTHOR} ·
            <a href="{REPO_URL}" target="_blank" style="text-decoration:none;">
                GitHub
            </a>
            ·
            <a href="{RELEASES_URL}" target="_blank" style="text-decoration:none;">
                Releases
            </a>
            <br/>
            <span style="opacity: 0.7;">
                Version {app_version}
                · Commit {GIT_COMMIT}
                · Build {BUILD_TIME}
            </span>
            <br/>
            <span style="opacity: 0.6;">
                Built with POML
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )
