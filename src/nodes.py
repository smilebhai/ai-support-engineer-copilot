from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini"
)

def route_issue(state):

    category = state["category"].strip().lower()

    if "auth" in category:
        return "authentication"

    elif "ssl" in category:
        return "ssl"

    elif "kubernetes" in category:
        return "kubernetes"

    elif "connect" in category:
        return "connectivity"

    elif category == "performance":
        return "performance"

    else:
        raise ValueError(
            f"Unknown category: {category}"
        )

def classify_issue(state):
    issue = state["issue"]

    response = llm.invoke(
        f"""
        Classify the following support issue into exactly one category:

        Authentication
        SSL
        Kubernetes
        Connectivity
        Performance

        Issue:
        {issue}

        Return exactly one of the following values:

        Authentication
        SSL
        Kubernetes
        Connectivity
        Performance

        Do not return any other text.
        """
    )

    return {
        "category": response.content.strip()
    }

def generate_summary(state):

    issue = state["issue"]
    category = state["category"]
    troubleshooting = state["troubleshooting"]

    response = llm.invoke(
        f"""
        Create a concise escalation summary.

        Issue:
        {issue}

        Category:
        {category}

        Troubleshooting:
        {troubleshooting}

        Include:

        - Problem
        - Category
        - Actions Taken
        - Recommended Next Step
        """
    )

    return {
        "escalation_summary": response.content
    }

def auth_troubleshooter(state):

    print("Routing to Authentication Troubleshooter")
    return {
        "troubleshooting": [
            "Verify API key validity",
            "Check Authorization header",
            "Verify token expiration",
            "Confirm permissions",
            "Review authentication logs"
        ]
    }

def ssl_troubleshooter(state):

    print("Routing to SSL Troubleshooter")
    return {
        "troubleshooting": [
            "Check certificate expiration",
            "Verify certificate chain",
            "Validate trust store",
            "Check hostname mismatch",
            "Review recent certificate changes"
        ]
    }

def kubernetes_troubleshooter(state):

    print("Routing to Kubernetes Troubleshooter")
    return {
        "troubleshooting": [
            "Check pod status",
            "Check restart count",
            "Review pod logs",
            "Verify memory limits",
            "Check OOMKilled events"
        ]
    }

def connectivity_troubleshooter(state):

    print("Routing to Connectivity Troubleshooter")
    return {
        "troubleshooting": [
            "Verify DNS resolution",
            "Test network connectivity",
            "Check firewall rules",
            "Review load balancer health",
            "Inspect connection logs"
        ]
    }

def performance_troubleshooter(state):

    print("Routing to Performance Troubleshooter")
    return {
        "troubleshooting": [
            "Review latency metrics",
            "Check CPU utilization",
            "Check memory utilization",
            "Review recent deployments",
            "Analyze application traces"
        ]
    }

