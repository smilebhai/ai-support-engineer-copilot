def category_evaluator(outputs, reference_outputs):

    predicted = outputs["category"].strip().lower()

    expected = reference_outputs["expected_category"].strip().lower()

    return {
        "key": "category_accuracy",
        "score": 1 if predicted == expected else 0
    }