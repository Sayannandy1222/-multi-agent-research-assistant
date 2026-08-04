from app.agents.researcher import ResearcherAgent

researcher = ResearcherAgent()


def research_worker(state):
    """
    Executes one research task.

    Input:
        state["sub_question"]

    Output:
        {
            "findings": [ResearchFinding]
        }
    """

    finding = researcher.research(
        state["sub_question"]
    )

    return {
        "findings": [finding]
    }