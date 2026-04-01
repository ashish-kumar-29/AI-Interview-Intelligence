from pydantic import BaseModel

class JDRequest(BaseModel):
    job_description: str


class AlignmentResponse(BaseModel):
    alignment_score: int
    strengths: list[str]
    missing_skills: list[str]
    recommendations: list[str]