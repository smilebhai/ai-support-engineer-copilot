from langgraph.graph import StateGraph
from langgraph.graph import START, END

from state import SupportState

from nodes import (
    classify_issue,
    generate_summary,
    route_issue,
    auth_troubleshooter,
    ssl_troubleshooter,
    kubernetes_troubleshooter,
    connectivity_troubleshooter,
    performance_troubleshooter
)

graph_builder = StateGraph(SupportState)

# Core nodes
graph_builder.add_node("classify", classify_issue)
graph_builder.add_node("summary", generate_summary)

# Specialized troubleshooters
graph_builder.add_node("authentication", auth_troubleshooter)
graph_builder.add_node("ssl", ssl_troubleshooter)
graph_builder.add_node("kubernetes", kubernetes_troubleshooter)
graph_builder.add_node("connectivity", connectivity_troubleshooter)
graph_builder.add_node("performance", performance_troubleshooter)

# Start
graph_builder.add_edge(
    START,
    "classify"
)

# Conditional routing
graph_builder.add_conditional_edges(
    "classify",
    route_issue
)

# All paths converge
graph_builder.add_edge(
    "authentication",
    "summary"
)

graph_builder.add_edge(
    "ssl",
    "summary"
)

graph_builder.add_edge(
    "kubernetes",
    "summary"
)

graph_builder.add_edge(
    "connectivity",
    "summary"
)

graph_builder.add_edge(
    "performance",
    "summary"
)

# Finish
graph_builder.add_edge(
    "summary",
    END
)

graph = graph_builder.compile()