from langchain_core.output_parsers import PydanticOutputParser

from app.core.llm import get_llm
from app.models.schemas import ResearchFinding
from app.prompts.researcher_prompt import researcher_prompt
from app.tools.tavily_search import TavilySearchTool


class ResearcherAgent:
    """
    Research Agent

    Receives one sub-question,
    searches Tavily,
    extracts useful information,
   and generates a structured finding.
    """

    def __init__(self):

        self.search = TavilySearchTool()

        self.llm = get_llm()

        self.parser = PydanticOutputParser(
            pydantic_object=ResearchFinding
        )

        self.chain = (
            researcher_prompt
            | self.llm
            | self.parser
        )

    def research(
        self,
        sub_question: str,
    ) -> ResearchFinding:

        response = self.search.search(
            query=sub_question,
            max_results=3,
        )

        cleaned_results = []

        for result in response.get("results", []):

            cleaned_results.append(
                {
                    "title": result.get("title", ""),
                    "content": result.get("content", "")[:400],
                    "url": result.get("url", ""),
                }
            )

        return self.chain.invoke(
            {
                "sub_question": sub_question,
                "search_results": cleaned_results,
            }
        )