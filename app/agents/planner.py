from langchain_core.output_parsers import PydanticOutputParser

from app.core.llm import get_llm
from app.models.schemas import ResearchPlan, ResearchRequest
from app.prompts.planner_prompt import planner_prompt


class PlannerAgent:
    """
    Planner Agent

    Responsible for decomposing a user's research question
    into multiple focused sub-questions.
    """

    def __init__(self):

        self.llm = get_llm()

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

        return self.chain.invoke(
            {
                "question": request.question,
            }
        )