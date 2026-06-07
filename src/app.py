from graph import graph


def support_copilot(inputs):

    result = graph.invoke(
        {
            "issue": inputs["issue"]
        }
    )

    return {
        "category": result["category"],
        "escalation_summary": result["escalation_summary"]
    }