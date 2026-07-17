"""
Resume Analysis Engine

Provides high-level analysis based on
parsed resume information.
"""

from __future__ import annotations

from typing import Dict


class ResumeAnalyzer:
    """
    Performs intelligent resume analysis.
    """

    def __init__(self, resume_data: Dict):

        self.data = resume_data

    # ============================================================
    # Candidate Level
    # ============================================================

    def detect_candidate_level(self) -> str:

        experience = self.data.get("experience", "")

        if experience == "Experienced":
            return "Experienced"

        if experience == "Intermediate":
            return "Intermediate"

        return "Fresher"

    # ============================================================
    # Profile Strength
    # ============================================================

    def profile_strength(self) -> str:

        skills = len(self.data.get("skills", []))

        pages = self.data.get("pages", 1)

        score = 0

        score += skills

        score += pages * 2

        if score >= 20:
            return "Excellent"

        if score >= 14:
            return "Strong"

        if score >= 8:
            return "Average"

        return "Needs Improvement"

    # ============================================================
    # Resume Completeness
    # ============================================================

    def resume_completeness(self) -> int:

        fields = [

            "name",

            "email",

            "phone",

            "degree",

            "skills",

            "github",

            "linkedin",

        ]

        completed = 0

        for field in fields:

            value = self.data.get(field)

            if value:

                completed += 1

        return int((completed / len(fields)) * 100)

    # ============================================================
    # Key Highlights
    # ============================================================

    def highlights(self):

        notes = []

        if len(self.data.get("skills", [])) >= 8:

            notes.append("Strong technical skillset detected.")

        if self.data.get("github"):

            notes.append("GitHub profile detected.")

        if self.data.get("linkedin"):

            notes.append("LinkedIn profile detected.")

        if self.data.get("pages", 1) > 1:

            notes.append("Multi-page resume.")

        if self.data.get("experience") == "Experienced":

            notes.append("Professional experience detected.")

        return notes

    # ============================================================
    # Final Report
    # ============================================================

    def generate_report(self):

        return {

            "candidate_level": self.detect_candidate_level(),

            "profile_strength": self.profile_strength(),

            "resume_completeness": self.resume_completeness(),

            "highlights": self.highlights(),

        }