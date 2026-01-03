from __future__ import annotations

import re
from common.ollama_client import chat

PROMPT_PATH = __import__("pathlib").Path(__file__).parent / "react_prompt_insecure.txt"

def tool_weather(city: str) -> str:
    return f"Weather for {city}: 7C, light rain (stub)."

def parse_action(text: str):
    m = re.search(r"Action:\s*weather\((.*)\)", text)
    if not m:
        return None
    args = m.group(1)
    m2 = re.search(r"city\s*=\s*['\"]([^'\"]+)['\"]", args)
    return m2.group(1) if m2 else None

def main() -> None:
    system = PROMPT_PATH.read_text(encoding="utf-8")
    print("ReAct Weather Agent. Type 'exit' to quit.\n")
    while True:
        user = input("You: ").strip()
        if user.lower() in {"exit","quit"}:
            break

        msgs = [{"role":"system","content": system}, {"role":"user","content": user}]
        out = chat(msgs, temperature=0.2, num_predict=260)
        print(out)

        city = parse_action(out)
        if city:
            obs = tool_weather(city)
            out2 = chat(msgs + [{"role":"user","content": f"Observation: {obs}\nProvide Final:"}], temperature=0.2, num_predict=260)
            print(out2)
        print()

if __name__ == "__main__":
    main()
