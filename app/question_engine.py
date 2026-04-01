import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def generate_questions(resume_text, job_description):

    prompt = f"""
You are an expert technical interviewer.

Analyze the candidate's RESUME and JOB DESCRIPTION carefully.

Identify key skills, technologies, and domain areas mentioned in the resume.

Generate diverse interview questions that test:
- conceptual understanding
- practical experience
- real-world problem solving

The questions must be tailored to the candidate’s domain 
(e.g., software, VLSI, electronics, data science, etc.).

Avoid repeating similar question patterns.

Return only valid JSON in this format:

{{
"technical_questions": ["q1","q2","q3","q4"],
"behavioral_questions": ["q1","q2","q3"],
"scenario_questions": ["q1","q2","q3"]
}}

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3-8b-instruct",
        messages=[{"role":"user","content":prompt}],
        temperature=0.4
    )

    content = response.choices[0].message.content

    import json,re

    try:
        json_text = re.search(r"\{.*\}", content, re.DOTALL).group()
        return json.loads(json_text)
    except:
        return {
            "technical_questions": [],
            "behavioral_questions": [],
            "scenario_questions": []
        }