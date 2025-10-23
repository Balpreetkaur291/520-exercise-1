!pip install datasets -q

from datasets import load_dataset

# Load the HumanEval dataset
dataset = load_dataset("openai_humaneval")

# Take the first problem (Question 1)
problem = dataset["test"][128]

# Display the problem details
print("Problem ID:", problem["task_id"])
print("\n=== Problem Prompt ===\n")
print(problem["prompt"])

print("\n=== Canonical Solution ===\n")
print(problem["canonical_solution"])

print("\n=== Test Code ===\n")
print(problem["test"])
