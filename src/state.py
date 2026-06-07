from typing import TypedDict

class SupportState(TypedDict):
    issue: str
    category: str
    troubleshooting: list[str]
    escalation_summary: str