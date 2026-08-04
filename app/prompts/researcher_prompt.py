from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from app.models.schemas import ResearchFinding


parser = PydanticOutputParser(
    pydantic_object=ResearchFinding
)


researcher_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a senior AI research analyst.

Your job is to analyze search results and extract
accurate factual information.

Rules:

- Use ONLY the supplied search results.
- Never hallucinate facts.
- Never invent citations.
- Summarize clearly.
- Return structured output.

{format_instructions}
"""
        ),
        (
            "human",
            """
Question:

{question}


Search Results:

{search_results}
"""
        )
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)