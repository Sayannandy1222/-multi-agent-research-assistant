from app.workflows.research_graph import research_graph


def main():

    result = research_graph.invoke(
        {
            "question": "Compare OpenAI and Anthropic pricing.",
            "plan": None,
            "findings": [],
            "report": "",
        }
    )

    print()

    print("=" * 60)

    print(result["report"])


if __name__ == "__main__":
    main()