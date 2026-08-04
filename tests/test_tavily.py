from app.tools.tavily_search import TavilySearchTool


def main():

    tool = TavilySearchTool()

    result = tool.search(
        "Latest AI models released in 2026"
    )

    print(result)


if __name__ == "__main__":
    main()