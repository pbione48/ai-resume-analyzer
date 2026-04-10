import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clear_resume():
    st.session_state["resume_text"] = ""

st.title("AI Resume Analyzer")

st.button("Clear", on_click=clear_resume)

resume_text = st.text_area("Paste your resume here:", key="resume_text")

if st.button("Analyze"):
    prompt = f"""
You are a senior technical recruiter reviewing a software engineering resume.

Analyze the resume and provide:

1. Strengths (what is good)
2. Weaknesses (what is missing or weak)
3. Specific improvements (actionable changes)
4. Improved bullet point examples (rewrite at least 2 bullets with impact and metrics)
5. Overall score (1–10) with short justification

Be concise, professional, and structured.

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.markdown(response.choices[0].message.content)