from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="ibm-granite/granite-guardian-hap-38m"
)

result = classifier("You are worthless and should leave.")
print(result)  # [{'label': 'HAP', 'score': 0.98}]