from dotenv import load_dotenv
import csv

load_dotenv()

from app import support_copilot

DATASET_PATH = "data/evaluation_dataset.csv"

total = 0
passed = 0

with open(DATASET_PATH, newline="") as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        issue = row["issue"]
        expected = row["expected_category"]

        result = support_copilot(
            {
                "issue": issue
            }
        )

        predicted = result["category"]

        is_correct = predicted == expected

        total += 1

        if is_correct:
            passed += 1

        status = "PASS" if is_correct else "FAIL"

        print(
            f"{status:5} | Expected: {expected:15} | Predicted: {predicted:15} | Issue: {issue[:50]}..."
        )

accuracy = (passed / total) * 100

print("\n" + "=" * 80)

print(
    f"Accuracy: {passed}/{total} ({accuracy:.2f}%)"
)