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

    @property
    def text(self) -> str:
        """
        Returns cleaned resume text.
        """
        return self.resume_text

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
        
        self.data["total_skills"] = len(self.data["skills"])

        return self.data

    # ==========================================================
    # Extraction Methods
    # ==========================================================

    def _extract_name(self) -> None:
        """
        Extract candidate name using spaCy PERSON entities.
        Falls back to the first meaningful line if needed.
        """
        doc = self.nlp(self.resume_text)

        for entity in doc.ents:
            if entity.label_ == "PERSON":
                if len(entity.text.split()) <= 4:
                    self.data["name"] = entity.text.strip()
                    return

        for line in self.resume_text.splitlines():
            line = line.strip()
            if (
                line
                and len(line.split()) <= 4
                and not any(ch.isdigit() for ch in line)
                and "@" not in line
            ):
                self.data["name"] = line
                return

    def _extract_email(self) -> None:
        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
        match = re.search(pattern, self.resume_text)
        if match:
            self.data["email"] = match.group()

    def _extract_phone(self) -> None:
        pattern = (
            r"(?:\+?\d{1,3}[\s-]?)?"
            r"(?:\(?\d{3}\)?[\s-]?)?"
            r"\d{3}[\s-]?\d{4}"
        )
        matches = re.findall(pattern, self.resume_text)
        for phone in matches:
            digits = re.sub(r"\D", "", phone)
            if len(digits) >= 10:
                self.data["phone"] = digits[-10:]
                return

    def _extract_github(self) -> None:
        pattern = r"github\.com/[A-Za-z0-9_.-]+"
        match = re.search(pattern, self.resume_text, re.I)
        if match:
            self.data["github"] = "https://" + match.group()

    def _extract_linkedin(self) -> None:
        pattern = r"linkedin\.com/in/[A-Za-z0-9_-]+"
        match = re.search(pattern, self.resume_text, re.I)
        if match:
            self.data["linkedin"] = "https://" + match.group()

    def _extract_degree(self) -> None:
        degrees = [
            "B.Tech",
            "B.E",
            "M.Tech",
            "M.E",
            "BCA",
            "MCA",
            "B.Sc",
            "M.Sc",
            "MBA",
            "PhD",
            "Diploma",
        ]
        lower = self.resume_text.lower()
        for degree in degrees:
            if degree.lower() in lower:
                self.data["degree"] = degree
                return

    def _extract_skills(self) -> None:
        """
        Extract technical skills from the resume.

        - Case insensitive
        - Removes duplicates
        - Supports aliases
        - Returns sorted skills
        """
        skill_catalog = {
            # Programming Languages
            "python": ["python"],
            "java": ["java"],
            "c": [" c "],
            "c++": ["c++"],
            "c#": ["c#", "csharp"],
            "javascript": ["javascript", "js"],
            "typescript": ["typescript", "ts"],
            "go": ["golang", "go"],
            "rust": ["rust"],
            # Web
            "html": ["html"],
            "css": ["css"],
            "bootstrap": ["bootstrap"],
            "tailwind css": ["tailwind"],
            "react": ["react", "reactjs"],
            "next.js": ["nextjs", "next.js"],
            "vue": ["vue"],
            "angular": ["angular"],
            "node.js": ["node", "nodejs", "node.js"],
            "express.js": ["express", "expressjs"],
            # Database
            "mysql": ["mysql"],
            "postgresql": ["postgres", "postgresql"],
            "mongodb": ["mongodb"],
            "sqlite": ["sqlite"],
            # AI / ML
            "machine learning": ["machine learning"],
            "deep learning": ["deep learning"],
            "tensorflow": ["tensorflow"],
            "keras": ["keras"],
            "pytorch": ["pytorch"],
            "opencv": ["opencv"],
            "nlp": ["nlp", "natural language processing"],
            "computer vision": ["computer vision"],
            "pandas": ["pandas"],
            "numpy": ["numpy"],
            "matplotlib": ["matplotlib"],
            "scikit-learn": ["sklearn", "scikit-learn"],
            # Cloud
            "aws": ["aws"],
            "azure": ["azure"],
            "gcp": ["google cloud", "gcp"],
            # DevOps
            "docker": ["docker"],
            "kubernetes": ["kubernetes"],
            "git": ["git"],
            "github": ["github"],
            # Mobile
            "android": ["android"],
            "flutter": ["flutter"],
            "dart": ["dart"],
            "swift": ["swift"],
            "kotlin": ["kotlin"],
            # UI
            "figma": ["figma"],
            "adobe xd": ["adobe xd"],
            # Misc
            "linux": ["linux"],
            "streamlit": ["streamlit"],
            "flask": ["flask"],
            "django": ["django"],
            "fastapi": ["fastapi"],
        }

        text = self.resume_text.lower()
        detected = set()

        for skill, aliases in skill_catalog.items():
            for alias in aliases:
                if alias in text:
                    detected.add(skill)
                    break

        self.data["skills"] = sorted(detected)

    def _estimate_experience(self) -> None:
        text = self.resume_text.lower()
        if "work experience" in text:
            self.data["experience"] = "Experienced"
        elif "experience" in text:
            self.data["experience"] = "Experienced"
        elif "internship" in text:
            self.data["experience"] = "Intermediate"
        else:
            self.data["experience"] = "Fresher"