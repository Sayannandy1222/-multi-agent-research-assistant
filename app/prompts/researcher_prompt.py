from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.models.schemas import ResearchFinding


parser = PydanticOutputParser(
    pydantic_object=ResearchFinding
)

researcher_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a Senior AI Research Analyst.

Your job is to answer ONE research sub-question using ONLY the provided search results.

Rules:

1. Use ONLY the supplied Tavily search results.
2. Never hallucinate or invent facts.
3. Never invent URLs or citations.
4. Ignore information that is not present in the search results.
5. Produce a concise, factual summary.
6. Return ONLY valid JSON.
7. Do NOT wrap the JSON inside markdown.
8. Do NOT add explanations outside the JSON.

{format_instructions}
"""
        ),
        (
            "human",
            """
Sub Question:
{sub_question}

Search Results:
{search_results}
"""
        ),
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)