from .base import BaseRecommendationEngine

ANDROID_SKILLS = {
    "java": 5,
    "kotlin": 6,
    "android": 6,
    "firebase": 4,
    "sqlite": 3,
    "git": 2,
}


class AndroidRecommendation(BaseRecommendationEngine):

    DOMAIN = "Android Development"

    def recommend(self):

        return {
            "domain": self.DOMAIN,
            "score": self.calculate_score(ANDROID_SKILLS),
            "missing_skills": self.missing_skills(ANDROID_SKILLS),
        }