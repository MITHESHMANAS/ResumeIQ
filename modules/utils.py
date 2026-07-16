"""
Utility functions used throughout the Resume Analyzer.
"""

from __future__ import annotations

import base64
import os
from datetime import datetime
from pathlib import Path

import pdfplumber
import streamlit as st


# =============================================================================
# CSS
# =============================================================================

def load_css(css_path: str = "assets/css/style.css") -> None:
    """
    Load external CSS into the Streamlit application.
    """
    path = Path(css_path)

    if not path.exists():
        st.warning("CSS file not found.")
        return

    with open(path, "r", encoding="utf-8") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )


# =============================================================================
# PDF Preview
# =============================================================================

def show_pdf(file_path: str) -> None:
    """
    Display a PDF inside Streamlit.
    """

    try:
        with open(file_path, "rb") as pdf_file:
            encoded = base64.b64encode(pdf_file.read()).decode()

        pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{encoded}"
            width="100%"
            height="800px"
            type="application/pdf">
        </iframe>
        """

        st.markdown(pdf_display, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Unable to preview PDF.\n\n{e}")


# =============================================================================
# PDF Reader
# =============================================================================

def pdf_reader(file_path: str) -> str:
    """
    Read all text from a PDF.
    """

    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:

        st.error(f"Failed to read PDF.\n\n{e}")

    return text


# =============================================================================
# Save Uploaded Resume
# =============================================================================

def save_uploaded_file(uploaded_file, folder: str = "Uploaded_Resumes") -> str:
    """
    Save uploaded Streamlit file.
    Returns saved path.
    """

    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, uploaded_file.name)

    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return filepath


# =============================================================================
# Timestamp
# =============================================================================

def current_timestamp() -> str:
    """
    Return current timestamp.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# =============================================================================
# CSV Download
# =============================================================================

def dataframe_to_csv(df):

    return df.to_csv(index=False).encode("utf-8")


# =============================================================================
# File Extension
# =============================================================================

def get_extension(filename: str) -> str:

    return Path(filename).suffix.lower()


# =============================================================================
# File Exists
# =============================================================================

def file_exists(path: str) -> bool:

    return Path(path).exists()