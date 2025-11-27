import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def enhance_description(user_text: str) -> str:
    prompt = f"""
You convert informal animation requests into this exact format:

TASK: Create a Manim animation.

OBJECTS:
- ...

ANIMATION STEPS:
1. ...
2. ...

Now convert this user request into that format:

{user_text}
"""
    resp = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        max_output_tokens=300,
    )
    return resp.output[0].content[0].text

if __name__ == "__main__":
    text = "show a blue circle moving from left to right"
    print(enhance_description(text))
