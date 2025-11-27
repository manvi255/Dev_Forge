from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import json

model_name = "codellama/CodeLlama-7b-Instruct-hf"
print(f"Loading {model_name}...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("Model loaded!\n")

# Read first example from your dataset
with open("slm_dataset.jsonl", "r", encoding="utf-8") as f:
    line = f.readline().strip()
    example = json.loads(line)

enhanced_desc = example["input"]

prompt = f"""You are an assistant that writes complete Manim scripts in Python.

Follow this exact pattern:

from manim import *
class AutoScene(Scene):
    def construct(self):
        # animation code here

Use only valid Manim syntax.

Animation description:
{enhanced_desc}

Manim script:
"""

print("Prompt:\n")
print(prompt)
print("\n" + "="*60 + "\n")

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.2,
        do_sample=True,
        top_p=0.9
    )

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Generated output:\n")
print(generated_text)
