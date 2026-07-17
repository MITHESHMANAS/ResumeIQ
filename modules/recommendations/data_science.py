from .base import BaseRecommendationEngine

DATA_SCIENCE_SKILLS = {
    "python": 5,
    "numpy": 4,
    "pandas": 5,
    "matplotlib": 3,
    "scikit-learn": 5,
    "tensorflow": 6,
    "keras": 5,
    "opencv": 5,
    "machine learning": 6,
    "deep learning": 6,
}


class DataScienceRecommendation(BaseRecommendationEngine):

    DOMAIN = "Data Science & AI"

    def recommend(self):

        score = self.calculate_score(DATA_SCIENCE_SKILLS)

        return {
            "domain": self.DOMAIN,
            "score": score,
            "missing_skills": self.missing_skills(DATA_SCIENCE_SKILLS),
        }