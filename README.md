# Resume Analyzer

A professional AI-powered Resume Analyzer built using **Streamlit**, **spaCy**, **MySQL**, and **Python**.

The application extracts information from resumes, evaluates resume quality, identifies the candidate's domain, recommends missing skills, suggests learning resources, and provides an overall resume score.

---

## Features

- Resume Parsing (PDF)
- Resume Score (0–100)
- Candidate Level Detection
- Skill Extraction
- Domain Prediction
- Personalized Skill Recommendations
- Course Recommendations
- Resume Preview
- Admin Dashboard
- Feedback System
- Analytics Dashboard

---

## Tech Stack

- Python
- Streamlit
- spaCy
- pdfplumber
- MySQL
- Plotly
- Pandas

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/resume-analyzer.git

cd resume-analyzer
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install Packages

```bash
pip install -r requirements.txt
```

Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

Run

```bash
streamlit run app.py
```

---

## Folder Structure

The project follows a modular architecture where

- UI
- Business Logic
- Database
- Utilities
- Recommendations

are separated for better maintainability.

---

## License

MIT License.