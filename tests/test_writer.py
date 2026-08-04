from app.agents.writer import WriterAgent


def main():

    writer = WriterAgent()

    findings = """
Finding 1
OpenAI provides usage-based pricing.

Finding 2
Anthropic offers long-context models.

Finding 3
Both provide enterprise APIs.
"""

    report = writer.write(
        question="Compare OpenAI and Anthropic",
        findings=findings,
    )

    print()

    print("========== FINAL REPORT ==========")

    print()

    print(report.content)


if __name__ == "__main__":
    main()