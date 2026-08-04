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
You are a senior AI research analyst.

Your task is to answer ONE research sub-question.

You are given:

• one sub-question
• Tavily search results

Rules:

1. Use ONLY the supplied search results.
2. Never hallucinate.
3. Never invent citations.
4. Produce a concise factual summary.
5. Include only URLs that appear in the search results.

{format_instructions}
"""
        ),
        (
            "human",
            """
Sub Question

{sub_question}


Search Results

{search_results}
"""
        )
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)