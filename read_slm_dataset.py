import json

with open("slm_dataset.jsonl", "r", encoding="utf-8") as f:
    line = f.readline().strip()
    example = json.loads(line)

print("INPUT (enhanced description):\n")
print(example["input"])
print("\nOUTPUT (Manim script):\n")
print(example["output"])
