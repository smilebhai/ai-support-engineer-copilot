from dotenv import load_dotenv

load_dotenv()

from graph import graph


test_cases = [
    {
        "name": "Authentication",
        "issue": "Users started receiving 401 errors after rotating API keys."
    },
    {
        "name": "SSL",
        "issue": "Users are receiving SSL certificate validation errors when connecting to the platform."
    },
    {
        "name": "Kubernetes",
        "issue": "Several pods are being OOMKilled after a recent deployment."
    },
    {
        "name": "Connectivity",
        "issue": "Users are unable to connect to the platform due to DNS resolution failures."
    },
    {
        "name": "Performance",
        "issue": "Users are reporting slow API responses and increased latency during peak hours."
    }
]


for test in test_cases:

    print("\n" + "=" * 80)
    print(f"TEST CASE: {test['name']}")
    print("=" * 80)

    result = graph.invoke(
        {
            "issue": test["issue"]
        }
    )

    print("\nCATEGORY:")
    print(result["category"])

    print("\nTROUBLESHOOTING:")
    for step in result["troubleshooting"]:
        print(f"- {step}")

    print("\nESCALATION SUMMARY:")
    print(result["escalation_summary"])

    print("\n")