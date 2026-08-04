from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    question: str


class SubQuestion(BaseModel):
    id: int
    question: str


class ResearchPlan(BaseModel):
    original_question: str
    sub_questions: list[SubQuestion]


class ResearchFinding(BaseModel):
    sub_question: str
    summary: str
    sources: list[str] = Field(default_factory=list)


class ResearchReport(BaseModel):
    question: str
    findings: list[ResearchFinding]
    final_report: str