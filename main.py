from llm_enhance import enhance_description
from openai_generate_manim import generate_manim



def pipeline(user_text: str, output_file: str = "AutoScene.py"):
    # 1) Enhance
    enhanced = enhance_description(user_text)
    print("Enhanced description:\n")
    print(enhanced)
    print("\n" + "="*60 + "\n")

    # 2) Generate Manim code
    manim_code = generate_manim(enhanced)

    # ---- CLEAN MARKDOWN FENCES ----
    if "```" in manim_code:
        manim_code = manim_code.replace("```", "")
        manim_code = manim_code.strip()

    # ---- REMOVE LEADING 'python' TAG IF PRESENT ----
    lines = manim_code.splitlines()
    cleaned_lines = []
    for line in lines:
        if line.strip().lower() == "python":
            continue
        cleaned_lines.append(line)
    manim_code = "\n".join(cleaned_lines).strip()

    # Basic sanity check
    if "from manim import *" not in manim_code or "class AutoScene(Scene):" not in manim_code:
        raise RuntimeError("Generated code does not look like a valid Manim scene.")

    print("Generated Manim code:\n")
    print(manim_code)
    print("\n" + "="*60 + "\n")

    # 3) Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(manim_code)

    print(f"Saved Manim script to {output_file}")


if __name__ == "__main__":
    user_text = input("Describe your animation: ")
    pipeline(user_text)

