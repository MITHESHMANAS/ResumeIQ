from .android import AndroidRecommendation
from .data_science import DataScienceRecommendation
from .ios import IOSRecommendation
from .uiux import UIUXRecommendation
from .web import WebRecommendation


def generate_recommendations(skills):

    engines = [
        WebRecommendation(skills),
        DataScienceRecommendation(skills),
        AndroidRecommendation(skills),
        IOSRecommendation(skills),
        UIUXRecommendation(skills),
    ]

    reports = [engine.recommend() for engine in engines]

    reports.sort(key=lambda item: item["score"], reverse=True)

    return {
        "best_match": reports[0],
        "all_domains": reports,
    }