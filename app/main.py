from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from app.resume_parser import parse_resume
from app.ai_engine import analyze_alignment
from app.models import AlignmentResponse
from app.question_engine import generate_questions

app = FastAPI(title="AI Interview Intelligence Platform - Phase 1")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        resume_text = parse_resume(file)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="Empty resume text")

        result = analyze_alignment(resume_text, job_description)
        questions = generate_questions(resume_text, job_description)
        return {
            "analysis": result,
            "questions": questions
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))