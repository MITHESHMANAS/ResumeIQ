"""
Base Recommendation Engine

Calculates domain suitability based on
weighted skill matching.
"""

from __future__ import annotations

from typing import Dict, List


class BaseRecommendationEngine:

    def __init__(self, skills: List[str]):

        self.skills = {skill.lower() for skill in skills}

    def calculate_score(self, weights: Dict[str, int]) -> int:

        score = 0

        for skill, weight in weights.items():

            if skill.lower() in self.skills:

                score += weight

        return score

    def missing_skills(self, weights: Dict[str, int]) -> List[str]:

        missing = []

        for skill in weights:

            if skill.lower() not in self.skills:

                missing.append(skill)

        return missing