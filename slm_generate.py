import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

EXAMPLE_1_INPUT = """TASK: Create a Manim animation.

OBJECTS:
- A blue circle at position (0, 0) with radius 1.

ANIMATION STEPS:
1. Show the blue circle at the center of the screen.
2. Move the circle smoothly to position (3, 0) over 2 seconds.
"""

EXAMPLE_1_OUTPUT = """from manim import *

class AutoScene(Scene):
    def construct(self):
        circle = Circle(radius=1.0, color=BLUE).move_to([0, 0, 0])
        self.add(circle)
        self.play(circle.animate.move_to([3, 0, 0]), run_time=2.0)
"""

EXAMPLE_2_INPUT = """TASK: Create a Manim animation.

OBJECTS:
- A red rectangle centered at (0, 0) with width 4 and height 2.

ANIMATION STEPS:
1. Start with a blank screen.
2. Fade in the red rectangle at the center over 2 seconds.
3. Hold the rectangle on screen for 1 second.
"""

EXAMPLE_2_OUTPUT = """from manim import *

class AutoScene(Scene):
    def construct(self):
        rect = Rectangle(width=4.0, height=2.0, color=RED).move_to([0, 0, 0])
        self.play(FadeIn(rect), run_time=2.0)
        self.wait(1)
"""

def generate_manim(enhanced_text: str) -> str:
    prompt = f"""
You convert structured animation descriptions into valid Manim scripts.

Always:
- Use: from manim import *
- Define: class AutoScene(Scene): def construct(self): ...
- Use 3D coordinates for positions, like [x, y, 0] (never [x, y]).
- Follow the OBJECTS and ANIMATION STEPS exactly.

Here are some examples:

Example 1
Animation description:
{EXAMPLE_1_INPUT}

Manim script:
{EXAMPLE_1_OUTPUT}

Example 2
Animation description:
{EXAMPLE_2_INPUT}

Manim script:
{EXAMPLE_2_OUTPUT}

Now convert a new description.

Animation description:
{enhanced_text}

Manim script:
"""
    resp = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        max_output_tokens=800,
    )
    return resp.output[0].content[0].text

if __name__ == "__main__":
    test_description = """TASK: Create a Manim animation.

OBJECTS:
- A green square centered at (0, 0) with side length 2.

ANIMATION STEPS:
1. Show the green square at the center.
2. Move the square to the left over 2 seconds.
3. Hold for 1 second.
"""
    print(generate_manim(test_description))
