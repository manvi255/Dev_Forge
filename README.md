# Dev Forge – Manim SLM

Dev Forge is a tool that turns natural language math / physics descriptions into Manim Community v0.19.0 animations.  
It uses OpenAI `gpt-4o-mini` plus a few-shot prompt of curated Manim examples to generate `AutoScene.py`.

## Features

- Convert plain English prompts into Manim code.
- Support for:
  - Basic shapes (circles, rectangles, arrows, text).
  - Quadratic equation graphs using `Axes` and `plot`.
  - Conceptual visualizations like Bernoulli’s theorem.
- Automatic pipeline:
  - User prompt → enhanced structured description → Manim code → render.

## Tech Stack

- Python 3.13
- Manim Community v0.19.0
- OpenAI API (`gpt-4o-mini`)
- VS Code + PowerShell (Windows)

## Project Structure

- `main.py` – CLI entry point; runs the pipeline.
- `llm_enhance.py` – turns raw user text into a structured description.
- `openai_generate_manim.py` – calls OpenAI to generate Manim code.
- `AutoScene.py` – generated scene file rendered by Manim.
- `slm_dataset.jsonl` – training-style examples used to design the prompt.




