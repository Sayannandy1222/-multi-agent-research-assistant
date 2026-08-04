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
You are a senior AI research planner.

Your responsibility is ONLY to break a research question into
high-quality research tasks.

Rules:

1. Generate EXACTLY 3 sub-questions.
2. Each sub-question must focus on one independent topic.
3. The three sub-questions together should completely cover the user's question.
4. Do NOT answer the question.
5. Do NOT perform research.
6. Do NOT generate citations.
7. Keep each sub-question concise (under 20 words).
8. Return ONLY the structured output.

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