from typing import TypedDict, List, Annotated
import operator

from app.models.schemas import (
    ResearchPlan,
    ResearchFinding,
)


class ResearchState(TypedDict):

    question: str

    plan: ResearchPlan

    sub_question: str

    findings: Annotated[
        List[ResearchFinding],
        operator.add,
    ]

    report: str