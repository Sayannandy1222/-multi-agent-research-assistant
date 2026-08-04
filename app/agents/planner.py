from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser

from app.config import GROQ_API_KEY
from app.models.schemas import (
    ResearchPlan,
    ResearchRequest,
)
from app.prompts.planner_prompt import (
    planner_prompt,
    parser,
)


class PlannerAgent:
    """
    Planner Agent

    Responsibility:
    ----------------
    Accept a research question and break it into
    structured research sub-questions.

    Input:
        ResearchRequest

    Output:
        ResearchPlan
    """

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=GROQ_API_KEY,
            temperature=0,
        )

        self.parser = PydanticOutputParser(
            pydantic_object=ResearchPlan
        )

        self.chain = (
            planner_prompt
            | self.llm
            | self.parser
        )

    def plan(
        self,
        request: ResearchRequest,
    ) -> ResearchPlan:
        """
        Generate a structured research plan.
        """

        return self.chain.invoke(
            {
                "question": request.question,
            }
        )