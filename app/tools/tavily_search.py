from tavily import TavilyClient

from app.config import TAVILY_API_KEY


class TavilySearchTool:
    """
    Wrapper around the Tavily Search API.
    """

    def __init__(self):
        self.client = TavilyClient(
            api_key=TAVILY_API_KEY
        )

    def search(
        self,
        query: str,
        max_results: int = 3,
    ):
        """
        Search the web using Tavily.
        """

        return self.client.search(
            query=query,
            search_depth="advanced",
            max_results=max_results,
            include_answer=True,
            include_raw_content=False,
        )