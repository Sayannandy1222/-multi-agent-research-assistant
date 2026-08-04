from langchain_core.output_parsers import PydanticOutputParser

from app.core.llm import get_llm
from app.models.schemas import ResearchFinding
from app.prompts.researcher_prompt import researcher_prompt
from app.tools.tavily_search import TavilySearchTool


class ResearcherAgent:
    """
    Research Agent

    Receives one sub-question,
    searches the web,
    produces structured findings.
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

        search_results = self.search.search(
            query=sub_question,
            max_results=5,
        )

        return self.chain.invoke(
            {
                "sub_question": sub_question,
                "search_results": str(search_results),
            }
        )