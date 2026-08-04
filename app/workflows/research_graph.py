from typing import TypedDict, List, Annotated
import operator

from langgraph.graph import StateGraph, END

from app.agents.planner import PlannerAgent
from app.agents.researcher import ResearcherAgent
from app.agents.writer import WriterAgent
from app.models.schemas import (
    ResearchRequest,
    ResearchFinding,
    ResearchPlan,
)


class ResearchState(TypedDict):
    question: str
    plan: ResearchPlan

    findings: Annotated[
        List[ResearchFinding],
        operator.add,
    ]

    report: str


planner = PlannerAgent()
researcher = ResearcherAgent()
writer = WriterAgent()


def planner_node(state: ResearchState):

    request = ResearchRequest(
        question=state["question"]
    )

    plan = planner.plan(request)

    return {
        "plan": plan,
    }


def researcher_node(state: ResearchState):

    findings = []

    for sub_question in state["plan"].sub_questions:

        finding = researcher.research(
            sub_question.question
        )

        findings.append(finding)

    return {
        "findings": findings,
    }


def writer_node(state: ResearchState):

    findings_text = ""

    for finding in state["findings"]:

        findings_text += f"""
Sub Question:
{finding.sub_question}

Summary:
{finding.summary}

Sources:
{", ".join(finding.sources)}

"""

    report = writer.write(
        question=state["question"],
        findings=findings_text,
    )

    return {
        "report": report.content,
    }


graph = StateGraph(ResearchState)

graph.add_node(
    "planner",
    planner_node,
)

graph.add_node(
    "researcher",
    researcher_node,
)

graph.add_node(
    "writer",
    writer_node,
)

graph.set_entry_point("planner")

graph.add_edge(
    "planner",
    "researcher",
)

graph.add_edge(
    "researcher",
    "writer",
)

graph.add_edge(
    "writer",
    END,
)

research_graph = graph.compile()