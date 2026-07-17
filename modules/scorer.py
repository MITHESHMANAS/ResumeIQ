"""
ResumeIQ AI
Resume Scoring Engine

Calculates a resume score using weighted metrics.
"""

from __future__ import annotations

from typing import Dict, List


class ResumeScorer:
    """
    Computes a weighted score for a parsed resume.
    """

    def __init__(self, resume_data: Dict):

        self.data = resume_data

        self.breakdown = {}

    # ==========================================================
    # Internal Helpers
    # ==========================================================

    def _add_score(self, category: str, score: int):

        self.breakdown[category] = score

    # ==========================================================
    # Contact Information
    # ==========================================================

    def score_contact(self):

        score = 0

        if self.data.get("name"):
            score += 2

        if self.data.get("email"):
            score += 2

        if self.data.get("phone"):
            score += 2

        self._add_score("Contact Information", score)

    # ==========================================================
    # Education
    # ==========================================================

    def score_education(self):

        score = 5 if self.data.get("degree") else 0

        self._add_score("Education", score)

    # ==========================================================
    # Technical Skills
    # ==========================================================

    def score_skills(self):

        count = len(self.data.get("skills", []))

        if count >= 15:
            score = 25

        elif count >= 10:
            score = 20

        elif count >= 6:
            score = 15

        elif count >= 3:
            score = 10

        else:
            score = 5 if count else 0

        self._add_score("Technical Skills", score)

    # ==========================================================
    # Professional Profiles
    # ==========================================================

    def score_profiles(self):

        score = 0

        if self.data.get("github"):
            score += 5

        if self.data.get("linkedin"):
            score += 5

        self._add_score("Professional Profiles", score)

    # ==========================================================
    # Resume Length
    # ==========================================================

    def score_pages(self):

        pages = self.data.get("pages", 1)

        if pages == 1:
            score = 10

        elif pages == 2:
            score = 8

        else:
            score = 5

        self._add_score("Resume Length", score)

    # ==========================================================
    # Experience
    # ==========================================================

    def score_experience(self):

        level = self.data.get("experience")

        mapping = {
            "Experienced": 20,
            "Intermediate": 12,
            "Fresher": 5,
        }

        self._add_score(
            "Experience",
            mapping.get(level, 0),
        )

    # ==========================================================
    # Final Score
    # ==========================================================

    def calculate_score(self):

        self.breakdown.clear()

        self.score_contact()

        self.score_education()

        self.score_skills()

        self.score_profiles()

        self.score_pages()

        self.score_experience()

        total = sum(self.breakdown.values())

        total = min(total, 100)

        return {
            "score": total,
            "grade": self.grade(total),
            "breakdown": self.breakdown,
        }

    # ==========================================================
    # Grade
    # ==========================================================

    @staticmethod
    def grade(score: int):

        if score >= 90:
            return "A+"

        if score >= 80:
            return "A"

        if score >= 70:
            return "B"

        if score >= 60:
            return "C"

        return "Needs Improvement"

    # ==========================================================
    # Suggestions
    # ==========================================================

    def suggestions(self) -> List[str]:

        tips = []

        if not self.data.get("github"):
            tips.append("Add your GitHub profile.")

        if not self.data.get("linkedin"):
            tips.append("Include your LinkedIn profile.")

        if len(self.data.get("skills", [])) < 8:
            tips.append("Include more relevant technical skills.")

        if self.data.get("pages", 1) > 2:
            tips.append("Reduce your resume to one or two pages.")

        if not self.data.get("degree"):
            tips.append("Mention your educational qualification.")

        return tips