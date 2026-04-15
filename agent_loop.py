import subprocess
from pathlib import Path

AGENTS_MD = Path("AGENTS.md").read_text()

def run_ollama(model, prompt):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()

def plan(task):
    prompt = f"""
You are a planning agent.

Follow these rules:
{AGENTS_MD}

Task:
{task}

Output a step-by-step plan.
"""
    return run_ollama("kamekichi128/qwen3-4b-instruct-2507:latest", prompt)

def execute(step):
    prompt = f"""
You are a coding agent.

Follow these rules:
{AGENTS_MD}

Execute this step:
{step}

Return:
- File changes
- Exact code edits
"""
    return run_ollama("nemotron-3-nano:4b", prompt)

def main():
    task = "Improve homepage readability and add a Key Achievements section"

    plan_output = plan(task)
    print("PLAN:\n", plan_output)

    steps = plan_output.split("\n")

    for step in steps:
        result = execute(step)
        print("STEP RESULT:\n", result)

if __name__ == "__main__":
    main()