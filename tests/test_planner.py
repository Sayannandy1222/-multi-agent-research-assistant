from app.agents.planner import PlannerAgent
from app.models.schemas import ResearchRequest


def main():

    planner = PlannerAgent()

    request = ResearchRequest(
        question="""
Compare OpenAI, Anthropic, Google Gemini,
and Meta Llama in terms of pricing,
context window, benchmarks,
enterprise adoption,
and developer experience.
"""
    )

    plan = planner.plan(request)

    print("\n========== RESEARCH PLAN ==========\n")

    print(plan)


if __name__ == "__main__":
    main()