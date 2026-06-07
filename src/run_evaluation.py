from dotenv import load_dotenv

load_dotenv()

from langsmith import evaluate

from app import support_copilot
from evaluators import category_evaluator
from summary_evaluator import summary_quality_evaluator


DATASET_NAME = "Support Escalation Evaluation"

experiment_results = evaluate(
    support_copilot,
    data=DATASET_NAME,
    evaluators=[
        category_evaluator,
        summary_quality_evaluator
    ],
    experiment_prefix="support-escalation-v2"
)

print("Evaluation complete.")

