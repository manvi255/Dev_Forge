import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
You are a code generator that writes Manim Community v0.19.0 scenes.
Given a structured animation description, output ONLY valid Python code:

from manim import *

class AutoScene(Scene):
    def construct(self):
        ...

Rules:
- No markdown, no ```
- Import anything you use (e.g., import numpy as np).
- Use 3D coordinates like [x, y, 0].
"""

def generate_manim(enhanced_description: str) -> str:
    prompt = SYSTEM_PROMPT + "\n\nHere is the animation description:\n\n" + enhanced_description
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )
    return response.output_text
