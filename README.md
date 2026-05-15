# AI Resume Analyzer

A Streamlit web application that uses the OpenAI API to analyze resumes and provide structured, actionable feedback — the way a senior technical recruiter would.

---

## What It Does

Paste any resume into the app and get back:

- **Strengths** — what's working well
- **Weaknesses** — what's missing or unconvincing
- **Specific improvements** — actionable changes to make
- **Rewritten bullet points** — at least 2 examples improved with impact and metrics
- **Overall score (1–10)** — with a short justification

---

## Demo

> Paste resume → click Analyze → get structured recruiter feedback in seconds.

Built with a prompt engineered to respond like a senior technical recruiter reviewing a software engineering candidate.

---

## Tech Stack

| Layer | Tool |
|-------|------|
| UI | Streamlit |
| AI | OpenAI API (`gpt-4o-mini`) |
| Language | Python 3 |
| Config | python-dotenv / Streamlit secrets |

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/pbione48/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_key_here
```

Or if deploying to Streamlit Cloud, add it under **Settings → Secrets**:
```
OPENAI_API_KEY = "your_key_here"
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## Project Structure

```
resume-analyzer/
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
├── .env                # API key (not committed)
├── .gitignore          # Excludes .env
└── README.md
```

---

## Key Features

- **Secure API key management** — loads from `.env` locally, Streamlit secrets in production
- **Input validation** — warns the user if the resume field is empty before calling the API
- **Error handling** — catches API failures gracefully with user-friendly messages
- **Loading indicator** — spinner while the model processes the resume
- **Prompt engineering** — structured prompt designed to produce consistent, recruiter-style output

---

## Author

**Paulo Bezerra** · [GitHub](https://github.com/pbione48)
