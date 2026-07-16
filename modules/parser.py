"""
ResumeIQ AI
Modern Resume Parser

Responsible for:
- Reading PDF resumes
- Extracting raw text
- Preparing structured data
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import pdfplumber
import spacy


class ResumeParser:
    """
    Resume parser responsible for extracting structured
    information from PDF resumes.
    """

    def __init__(self, pdf_path: str):

        self.pdf_path = Path(pdf_path)

        self.resume_text = ""

        self.nlp = self._load_spacy_model()

        self.data: dict[str, Any] = {
            "name": "",
            "email": "",
            "phone": "",
            "degree": "",
            "skills": [],
            "github": "",
            "linkedin": "",
            "experience": "",
            "pages": 0,
        }

        self._extract_pdf_text()

    # ==========================================================
    # spaCy
    # ==========================================================

    @staticmethod
    def _load_spacy_model():

        try:
            return spacy.load("en_core_web_sm")

        except OSError as exc:

            raise RuntimeError(
                "spaCy model not installed.\n"
                "Run:\n"
                "python -m spacy download en_core_web_sm"
            ) from exc

    # ==========================================================
    # PDF Extraction
    # ==========================================================

    def _extract_pdf_text(self):

        if not self.pdf_path.exists():

            raise FileNotFoundError(self.pdf_path)

        extracted_text = []

        with pdfplumber.open(self.pdf_path) as pdf:

            self.data["pages"] = len(pdf.pages)

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    extracted_text.append(page_text)

        self.resume_text = "\n".join(extracted_text)

        self.resume_text = self._normalize_text(
            self.resume_text
        )

    # ==========================================================
    # Normalization
    # ==========================================================

    @staticmethod
    def _normalize_text(text: str) -> str:

        text = text.replace("\t", " ")

        text = re.sub(r"[ ]{2,}", " ", text)

        text = re.sub(r"\n{2,}", "\n", text)

        return text.strip()

    # ==========================================================
    # Public API
    # ==========================================================

    def parse(self):

        """
        Main parser entry.
        """

        self._extract_name()

        self._extract_email()

        self._extract_phone()

        self._extract_github()

        self._extract_linkedin()

        self._extract_degree()

        self._extract_skills()

        self._estimate_experience()

        return self.data

    # ==========================================================
    # Extraction Methods
    # (Implemented in next commit)
    # ==========================================================

    def _extract_name(self):
        pass

    def _extract_email(self):
        pass

    def _extract_phone(self):
        pass

    def _extract_degree(self):
        pass

    def _extract_skills(self):
        pass

    def _extract_github(self):
        pass

    def _extract_linkedin(self):
        pass

    def _estimate_experience(self):
        pass