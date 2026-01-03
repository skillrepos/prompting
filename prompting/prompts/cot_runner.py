from __future__ import annotations

import argparse
import re
from pathlib import Path

from common.ollama_client import generate

PROMPTS = Path(__file__).parent / "cot_prompts.txt"

def parse_pairs(text: str):
    blocks = re.split(r"\[Q\d+\]", text)
    pairs = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        d = re.search(r"DIRECT:\s*(.+)", b)
        c = re.search(r"COT:\s*(.+)", b)
        if d and c:
            pairs.append((d.group(1).strip(), c.group(1).strip()))
    return pairs

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["direct","cot"], default="direct")
    args = ap.parse_args()

    pairs = parse_pairs(PROMPTS.read_text(encoding="utf-8"))
    print(f"CoT Runner mode={args.mode}\n")
    for i,(d,c) in enumerate(pairs, start=1):
        prompt = d if args.mode == "direct" else c
        out = generate(prompt, temperature=0.2, num_predict=220)
        print(f"Q{i} prompt: {prompt}")
        print(out)
        print("-"*60)

if __name__ == "__main__":
    main()
