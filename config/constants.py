"""
Global constants used throughout the application.
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Resume Sections
# -----------------------------------------------------------------------------

RESUME_SECTIONS = [
    "Objective",
    "Summary",
    "Education",
    "Experience",
    "Internships",
    "Skills",
    "Projects",
    "Achievements",
    "Certifications",
    "Hobbies",
    "Interests",
]

# -----------------------------------------------------------------------------
# Candidate Levels
# -----------------------------------------------------------------------------

FRESHER = "Fresher"
INTERMEDIATE = "Intermediate"
EXPERIENCED = "Experienced"
UNKNOWN = "NA"

# -----------------------------------------------------------------------------
# Supported Domains
# -----------------------------------------------------------------------------

SUPPORTED_FIELDS = [
    "Data Science",
    "Web Development",
    "Android Development",
    "iOS Development",
    "UI/UX",
]

# -----------------------------------------------------------------------------
# Sidebar Navigation
# -----------------------------------------------------------------------------

NAVIGATION_ITEMS = [
    "User",
    "Feedback",
    "About",
    "Admin",
]

# -----------------------------------------------------------------------------
# UI Messages
# -----------------------------------------------------------------------------

SUCCESS_ANALYSIS = "Analysis completed successfully."

ERROR_PDF = "Unable to read the uploaded PDF."

ERROR_PARSE = "Unable to extract resume information."

NO_RECOMMENDATION = (
    "No specific recommendation could be generated for the uploaded resume."
)