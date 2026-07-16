"""
Course catalog for Resume Analyzer.

Each category contains recommended learning resources.
"""

from __future__ import annotations

DATA_SCIENCE_COURSES = [
    (
        "Machine Learning Specialization - Andrew Ng",
        "https://www.coursera.org/specializations/machine-learning-introduction",
    ),
    (
        "Python for Data Science",
        "https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/",
    ),
    (
        "IBM Data Science Professional Certificate",
        "https://www.coursera.org/professional-certificates/ibm-data-science",
    ),
]

WEB_DEVELOPMENT_COURSES = [
    (
        "The Odin Project",
        "https://www.theodinproject.com/",
    ),
    (
        "Full Stack Open",
        "https://fullstackopen.com/en/",
    ),
    (
        "CS50 Web Programming",
        "https://cs50.harvard.edu/web/",
    ),
]

ANDROID_COURSES = [
    (
        "Android Basics with Compose",
        "https://developer.android.com/courses/android-basics-compose/course",
    ),
]

IOS_COURSES = [
    (
        "Develop in Swift",
        "https://developer.apple.com/learn/curriculum/",
    ),
]

UIUX_COURSES = [
    (
        "Google UX Design Professional Certificate",
        "https://www.coursera.org/professional-certificates/google-ux-design",
    ),
]

COURSE_MAP = {
    "Data Science": DATA_SCIENCE_COURSES,
    "Web Development": WEB_DEVELOPMENT_COURSES,
    "Android Development": ANDROID_COURSES,
    "iOS Development": IOS_COURSES,
    "UI/UX": UIUX_COURSES,
}