import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

SYSTEM_PROMPT = """
You are a code generator that writes Manim Community v0.19.0 scenes.
Given a structured animation description, output ONLY valid Python code:

from manim import *

class AutoScene(Scene):
    def construct(self):
        ...

Rules:
- No markdown, no ```
- Import anything you use (e.g., numpy as np).
- Use 3D coordinates [x, y, 0].
"""

def generate_manim(enhanced_description: str) -> str:
    prompt = SYSTEM_PROMPT + "\n\nHere is the animation description:\n\n" + enhanced_description
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text
