# 📘 POML README Structurer

![Python](https://img.shields.io/badge/Python-3.10-blue)
![CI](https://github.com/SANJAI-s0/readme-structurer-poml/actions/workflows/ci.yml/badge.svg)
![Built with POML](https://img.shields.io/badge/Built%20with-POML-blueviolet)

A **Streamlit-based documentation tool** that restructures README-like content into a **clean, standardized Markdown format** using **POML (Prompt Orchestration Markup Language) as the single source of truth**.

The tool accepts multiple input formats (text, JSON, documents, and markup files) and normalizes them into a readable, well-structured `README.md` **without inference or hallucination**.

---

## 📑 Table of Contents

- [Key Features](#-key-features)
- [Versioning & Build Metadata](#-versioning--build-metadata)
- [Semantic Versioning Policy](#-semantic-versioning-policy)
- [How It Works](#-how-it-works-high-level)
- [Project Structure](#project-structure)
- [Prerequisites](#-prerequisites)
- [Setup Instructions](#setup-instructions)
- [Working Directory Convention](#-working-directory-convention-important)
- [Environment Setup](#environment-setup)
- [Install Dependencies](#install-dependencies)
- [Run the Application](#run-the-application-streamlit)
- [Run Tests](#-run-tests-pytest)
- [Docker](#-run-with-docker)
- [GitHub Actions CI](#-github-actions-ci-automatic)
- [Releases](#-releases)
- [Customization](#-customization)
- [Design Principles](#-design-principles)
- [License](#-license)

---

## ✨ Key Features

- 📄 Supports TXT, JSON, PDF, DOCX, RTF, HTML, XML 
- 🔀 Order-independent section detection 
- 📐 Structure strictly defined by POML rules 
- ❌ No inference / no hallucination 
- 🧱 Modular, production-ready architecture 
- 🧪 Automated tests with pytest 
- 🐳 Docker support 
- 🤖 GitHub Actions CI enabled

---

## 🔖 Versioning & Build Metadata

This project follows a **single source of truth** approach for versioning.

- The application version is defined in `pyproject.toml`
- Docker builds inject the version using build arguments
- GitHub Actions injects the commit hash during CI runs
- The Streamlit footer displays:
  - App version
  - Git commit (short hash)
  - Build timestamp

This ensures every build is **traceable, reproducible, and transparent**.

---

### Version Source (`pyproject.toml`)

The canonical version lives in:

```toml
[project]
name = "poml-readme-structurer"
version = "1.0.0"
```
---

## 🔢 Semantic Versioning Policy

This project follows **Semantic Versioning (SemVer)**:


### Version increment rules

- **MAJOR** (`X.0.0`)
  - Breaking changes
  - Removal or redefinition of POML rules
  - Incompatible API or behavior changes

- **MINOR** (`0.X.0`)
  - New features
  - New supported input formats
  - Backward-compatible enhancements

- **PATCH** (`0.0.X`)
  - Bug fixes
  - Performance improvements
  - Documentation-only changes

### Version source of truth

- The canonical version is defined in `pyproject.toml`
- Docker images and CI builds derive their version from this file


---

## 🧠 How It Works (High Level)

1. User uploads a file or pastes content 
2. Content is parsed into plain text 
3. JSON inputs are flattened into readable lines 
4. Sections are detected using POML rules 
5. Output is normalized into structured Markdown 
6. User previews and downloads README.md

---

## Project Structure
```
readme-structurer-poml/
│
├── app/
│   ├── __init__.py
│   ├── app.py                 # Streamlit entry point
│   ├── formatter.py           # Section structuring & cleanup
│   ├── parser.py              # Input parsing (TXT/JSON/PDF/etc.)
│   ├── poml_engine.py         # POML loader & interpreter
│   └── ui_helpers.py          # Sidebar + footer (version, CI metadata)
│
├── config/
│   └── poml_rules.xml         # POML rules (single source of truth)
│
├── tests/
│   ├── __init__.py
│   ├── test_poml_engine.py    # Tests for POML loading
│   ├── test_parser.py         # Tests for JSON flattening
│   ├── test_formatter.py      # Tests for README formatting
│   │
│   └── samples/               # Manual test inputs
│       ├── plaintext.txt
│       ├── jsonfile.json
│       ├── xmlfile.xml
│       ├── htmlfile.html
│       ├── rtffile.rtf
│       ├── docfile.docx
│       └── pdffile.pdf
│
├── assets/
│   └── poml_readme_structurer.svg    # Architecture / banner graphic
│
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI (tests, metadata)
│
├── PROJECT/
│   └── create-project.ps1    # Entire Project script (lighter version)
│
├── Dockerfile                 # OCI-labeled Docker image definition
├── pyproject.toml             # Project metadata & version source
├── requirements.txt           # Runtime dependencies
├── CHANGELOG.md               # Release history (SemVer)
├── README.md                  # Project documentation
├── LICENSE                    # MIT license
├── .gitignore                 # Git ignore rules
└── pytest.ini                 # Pytest configuration
```

---

## ⚙️ Prerequisites

- Python 3.10.x (recommended: 3.10.11)
- pip
- (Optional) Docker

---

## Setup Instructions

**Clone the Repository**

```bash
git clone https://github.com/SANJAI-s0/readme-structurer-poml.git
cd readme-structurer-poml
```

---

## 📍 Working Directory Convention (IMPORTANT)

All commands below must be run from the project root directory:
```
readme-structurer-poml/
```

Do **not run commands** from inside `app/`, `tests/`, or any subdirectory.

---

## Environment Setup
**Windows (PowerShell)**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Environment Variables

This project supports a `.env` file for sensitive configuration.

**Required variables:**

GEMINI_API_KEY=<your-api-key>

> ⚠️ The `.env` file is ignored by Git and **must not be committed** 🔒.

---

## Install Dependencies
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Run the Application (Streamlit)

This **starts** the **Streamlit web UI** (Run from the root dir).
```bash
streamlit run app/main.py
```

Open in browser:
```
http://localhost:8501
```

---

## 🧪 Run Tests (pytest)

**📂 Run from project root**

Install pytest (if needed):
```bash
pip install pytest
```

Run all tests:
```bash
pytest
```

⚠️ Do not run pytest from inside the tests/ directory.

---

## 🐳 Run with Docker

**📂 Run from project root (directory containing Dockerfile)**

Docker allows you to run the application in a fully isolated, reproducible environment
without installing Python or dependencies locally.

All Docker commands **must be executed from the project root directory**:

```text
readme-structurer-poml/     #In the directory containing Dockerfile
```

### Build Docker Image (With Version Injection)

The Docker image supports explicit version injection via build arguments.

The injected version is:

- Displayed in the Streamlit footer 
- Stored in Docker image metadata (OCI labels)
- Used for release traceability


**Build Docker Image**
```powershell
docker build --build-arg APP_VERSION=1.0.0 -t poml-readme-structurer:1.0.0 .
```

**Run Docker Container**
After building the image, start the container:
```powershell
docker run -p 8501:8501 --env-file .env poml-readme-structurer
```

Open in browser:
```
http://localhost:8501
```

### Verify Docker Image Metadata (Optional)

To inspect the OCI image labels embedded during build:
```powershell
docker inspect poml-readme-structurer:1.0.0
```

You should see metadata similar to:

```json
"org.opencontainers.image.version": "1.0.0",
"org.opencontainers.image.revision": "<git-commit>",
"org.opencontainers.image.created": "<build-date>"
```

These labels ensure the image is traceable, reproducible, and release-ready.

---

## 🤖 GitHub Actions CI (Automatic)

This project includes **Continuous Integration** using GitHub Actions.

**What it does:**
- Runs on every push and pull request 
- Sets up Python 3.10
- Installs dependencies 
- Executes all pytest tests

**Configuration file:**
```bash
.github/workflows/ci.yml
```

No manual steps are required — GitHub always runs CI **from the repository root**.

---

## 🚀 Releases

Official releases are published on GitHub:

https://github.com/<your-username>/readme-structurer-poml/releases

Each release corresponds to:
- A tagged version from `pyproject.toml`
- A reproducible Docker build
- A traceable commit hash

---

## 📌 Design Principles
- POML-first architecture 
- Deterministic behavior 
- No silent assumptions 
- Clear separation of concerns 
- Portfolio- and production-ready

---

## 📜 License

MIT License

---

### © Copyright

© 2025 Sanjai. All rights reserved.

This project and its source code are provided for **educational and development** purposes.
Unauthorized copying, modification, or redistribution of this project, in whole or in part,
without explicit permission from the author, is prohibited except as permitted by the license.

---

## Who this is for (Optional)
`This project is intended for developers who want consistent, maintainable, and deterministic project documentation.`

---

## 🛠 Customization

**To change:**
- Section order 
- Section names 
- Aliases

Edit:

```
config/poml_rules.xml
```

No Python code changes are required.

---

### Lightweight Core Project Generator

This repository includes a **single-file PowerShell script** that embeds a core project definition directly inside itself.

When executed, it **extracts a minimal project kernel** consisting of:
- one Python file
- one XML rules file

No external templates, no scaffolding, and no assumptions.

```ini
.\create-core-project.ps1
```

This mode is intended for **quick experiments, demos, and learning**, following the same principles as this project:
**explicit rules, deterministic output, and zero inference**.

> If you want it even shorter (one-liner style) or more technical, say the word.

---

## ✅ Final Notes

This project demonstrates:
- Advanced documentation normalization
- Strong modular architecture
- Clean parsing and formatting logic
- Real-world engineering practices (tests, Docker, CI)

The application UI footer dynamically displays build metadata (version, commit, timestamp)
for full runtime transparency.

---
