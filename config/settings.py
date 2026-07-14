"""
Application settings.

Loads environment variables from the .env file and exposes them
through strongly named constants.
"""

from __future__ import annotations

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -----------------------------------------------------------------------------
# Database Configuration
# -----------------------------------------------------------------------------

DB_HOST: str = os.getenv("DB_HOST", "localhost")
DB_PORT: int = int(os.getenv("DB_PORT", "3306"))
DB_NAME: str = os.getenv("DB_NAME", "resume_db")
DB_USER: str = os.getenv("DB_USER", "root")
DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")

# -----------------------------------------------------------------------------
# Admin Configuration
# -----------------------------------------------------------------------------

ADMIN_USER: str = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS: str = os.getenv("ADMIN_PASS", "admin")

# -----------------------------------------------------------------------------
# Application Configuration
# -----------------------------------------------------------------------------

APP_NAME: str = "Resume Analyzer"

UPLOAD_FOLDER: str = "Uploaded_Resumes"

MAX_UPLOAD_SIZE: int = 5 * 1024 * 1024  # 5 MB

ALLOWED_EXTENSIONS = {"pdf"}

DEFAULT_PAGE_TITLE = "Resume Analyzer"

DEFAULT_PAGE_ICON = "📄"

DEFAULT_LAYOUT = "wide"