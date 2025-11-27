import json

def main():
    path = "slm_dataset.jsonl"
    examples = []

    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                print(f"Line {i} is empty, skipping")
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"JSON error on line {i}: {e}")
                return

            # basic checks
            if "input" not in obj or "output" not in obj:
                print(f"Line {i} missing 'input' or 'output'")
                return

            examples.append(obj)

    print(f"Loaded {len(examples)} examples successfully.")
    # show a small preview of first and last
    if examples:
        print("\nFirst example input preview:")
        print(examples[0]["input"][:200])
        print("\nLast example input preview:")
        print(examples[-1]["input"][:200])

if __name__ == "__main__":
    main()
