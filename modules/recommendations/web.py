from .base import BaseRecommendationEngine

WEB_SKILLS = {
    "html": 2,
    "css": 2,
    "javascript": 5,
    "react": 6,
    "node.js": 5,
    "express.js": 4,
    "mongodb": 4,
    "mysql": 3,
    "git": 2,
    "github": 2,
}


class WebRecommendation(BaseRecommendationEngine):

    DOMAIN = "Full Stack Web Development"

    def recommend(self):

        score = self.calculate_score(WEB_SKILLS)

        return {
            "domain": self.DOMAIN,
            "score": score,
            "missing_skills": self.missing_skills(WEB_SKILLS),
        }