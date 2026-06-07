from langchain_openai import ChatOpenAI

judge_llm = ChatOpenAI(
    model="gpt-4o-mini"
)

def summary_quality_evaluator(
    outputs,
    reference_outputs
):

    summary = outputs["escalation_summary"]

    response = judge_llm.invoke(
        f"""
        You are a senior technical support manager.

        Evaluate the following escalation summary.

        Give a score of 1 if:

        - Problem is clearly described
        - Troubleshooting actions are present
        - Recommended next step is present
        - Summary is technically relevant

        Otherwise return 0.

        Return only:
        1
        or
        0

        Summary:

        {summary}
        """
    )

    score = int(
        response.content.strip()
    )

    return {
        "key": "summary_quality",
        "score": score
    }