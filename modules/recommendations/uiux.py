from .base import BaseRecommendationEngine

UIUX_SKILLS = {
    "figma": 6,
    "adobe xd": 5,
    "photoshop": 4,
    "illustrator": 4,
    "ui": 4,
    "ux": 4,
}


class UIUXRecommendation(BaseRecommendationEngine):

    DOMAIN = "UI/UX Design"

    def recommend(self):

        return {
            "domain": self.DOMAIN,
            "score": self.calculate_score(UIUX_SKILLS),
            "missing_skills": self.missing_skills(UIUX_SKILLS),
        }