from app.agents.researcher import ResearcherAgent


def main():

    researcher = ResearcherAgent()

    result = researcher.research(
        "Compare OpenAI and Anthropic pricing."
    )

    print()

    print("========== RESEARCH RESULT ==========")

    print()

    print(result)


if __name__ == "__main__":
    main()