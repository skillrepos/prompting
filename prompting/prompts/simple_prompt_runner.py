from __future__ import annotations

from common.ollama_client import generate

def main() -> None:
    print("Simple Prompt Runner (Ollama). Paste a prompt. Type 'exit' to quit.\n")
    while True:
        prompt = input("Prompt> ").strip()
        if prompt.lower() in {"exit","quit"}:
            break
        out = generate(prompt, temperature=0.4, num_predict=300)
        print(f"\n---\n{out}\n---\n")

if __name__ == "__main__":
    main()
