from app.core.llm import get_llm
from app.prompts.writer_prompt import writer_prompt


class WriterAgent:
    """
    Writer Agent

    Converts research findings
    into a polished report.
    """

    def __init__(self):

        self.llm = get_llm()

        self.chain = (
            writer_prompt
            | self.llm
        )

    def write(
        self,
        question: str,
        findings: str,
    ):

        return self.chain.invoke(
            {
                "question": question,
                "findings": findings,
            }
        )