# ------------------------------------
# Base image
# ------------------------------------
FROM python:3.10-slim

# ------------------------------------
# Build arguments
# ------------------------------------
ARG APP_VERSION=dev
ARG BUILD_DATE
ARG VCS_REF

ENV APP_VERSION=${APP_VERSION}

# ------------------------------------
# OCI image labels
# ------------------------------------
LABEL org.opencontainers.image.title="POML README Structurer" \
      org.opencontainers.image.description="Streamlit-based tool to structure README files using POML as the single source of truth" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.authors="Sanjai" \
      org.opencontainers.image.url="https://github.com/<your-username>/readme-structurer-poml" \
      org.opencontainers.image.source="https://github.com/<your-username>/readme-structurer-poml" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.revision="${VCS_REF}"

# ------------------------------------
# Working directory
# ------------------------------------
WORKDIR /app

# ------------------------------------
# Install dependencies
# ------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ------------------------------------
# Copy source files
# ------------------------------------
COPY app ./app
COPY config ./config
COPY pyproject.toml .

# ------------------------------------
# Expose Streamlit port
# ------------------------------------
EXPOSE 8501

# ------------------------------------
# Streamlit environment
# ------------------------------------
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# ------------------------------------
# Run application
# ------------------------------------
CMD ["streamlit", "run", "app/app.py"]
