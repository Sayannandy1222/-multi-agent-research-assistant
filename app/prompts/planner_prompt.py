from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from app.models.schemas import ResearchPlan


parser = PydanticOutputParser(
    pydantic_object=ResearchPlan
)


planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are responsible for planning research.

Your task is to decompose one research question into clear,
independent sub-questions.

Rules:

- Return between 3 and 7 sub-questions.
- Every sub-question should investigate exactly one topic.
- Do not answer the research question.
- Do not perform research.
- Do not generate citations.
- Return only the structured planning output.

{format_instructions}
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)