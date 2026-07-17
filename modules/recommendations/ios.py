from .base import BaseRecommendationEngine

IOS_SKILLS = {
    "swift": 6,
    "ios": 6,
    "xcode": 5,
    "firebase": 4,
    "git": 2,
}


class IOSRecommendation(BaseRecommendationEngine):

    DOMAIN = "iOS Development"

    def recommend(self):

        return {
            "domain": self.DOMAIN,
            "score": self.calculate_score(IOS_SKILLS),
            "missing_skills": self.missing_skills(IOS_SKILLS),
        }