import os
from openai import OpenAI
from dotenv import load_dotenv
import json
import re

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def analyze_alignment(resume_text, job_description):

    prompt = f"""
You are an expert technical recruiter.

Compare the following resume and job description.

Return ONLY valid JSON in this exact format:

{{
  "alignment_score": number,
  "strengths": ["skill1", "skill2"],
  "missing_skills": ["skill1", "skill2"],
  "recommendations": ["recommendation1", "recommendation2"]
}}

Resume:
{resume_text}

Job Description:
{job_description}

Important:
Return ONLY JSON. Do not write explanations.
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3-8b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    content = response.choices[0].message.content

    try:
        json_text = re.search(r"\{.*\}", content, re.DOTALL).group()
        return json.loads(json_text)
    except:
        return {
            "alignment_score": 0,
            "strengths": [],
            "missing_skills": [],
            "recommendations": ["AI output parsing failed."]
        }