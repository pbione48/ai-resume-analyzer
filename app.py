import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv()

# Secure API key loading with fallback to Streamlit secrets
api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key not found. Add it to your .env file or Streamlit secrets.")
    st.stop()

client = OpenAI(api_key=api_key)


def clear_resume():
    st.session_state["resume_text"] = ""


# --- UI ---
st.title("AI Resume Analyzer")
st.markdown("Paste your resume below to get structured feedback from an AI recruiter.")

resume_text = st.text_area(
    "Paste your resume here:",
    key="resume_text",
    height=300,
    placeholder="Copy and paste the full text of your resume..."
)

col1, col2 = st.columns([1, 5])
with col1:
    st.button("Clear", on_click=clear_resume)
with col2:
    analyze = st.button("Analyze Resume", type="primary")

if analyze:
    if not resume_text.strip():
        st.warning("Please paste your resume before analyzing.")
    else:
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
        try:
            with st.spinner("Analyzing your resume..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
            st.markdown("---")
            st.subheader("Analysis Results")
            st.markdown(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.info("Check your API key and internet connection.")
