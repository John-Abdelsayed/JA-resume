#!/usr/bin/env python3

import subprocess
import json
import argparse
from pathlib import Path
from datetime import datetime

AGENTS_FILE = "AGENTS.md"
MODEL_PLANNER = "kamekichi128/qwen3-4b-instruct-2507:latest"
MODEL_EXECUTOR = "nemotron-3-nano:4b"


# ---------- Core LLM Call ----------
def run_ollama(model, prompt):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode().strip()


# ---------- Load Context ----------
def load_agents_md():
    if not Path(AGENTS_FILE).exists():
        raise FileNotFoundError("AGENTS.md not found")
    return Path(AGENTS_FILE).read_text()


def load_repo_files():
    files = {}
    for path in Path(".").rglob("*.md"):
        if path.name == AGENTS_FILE:
            continue
        try:
            files[str(path)] = path.read_text()
        except:
            pass
    return files


# ---------- Planning ----------
def plan_task(task, agents_md):
    prompt = f"""
You are a planning agent.

Follow ALL rules in AGENTS.md:
{agents_md}

Task:
{task}

CRITICAL:
- Output MUST be valid JSON
- Do NOT include line breaks inside strings
- Use \\n for newlines if needed
- Do NOT add explanations

Output JSON:
{{
  "steps": [
    "step 1",
    "step 2"
  ]
}}
"""
    response = run_ollama(MODEL_PLANNER, prompt)

    try:
        return json.loads(response)
    except:
        print("⚠️ Failed to parse plan. Raw output:\n", response)
        return {"steps": [task]}


# ---------- Execution ----------
def execute_step(step, agents_md, repo_files):
    context = "\n\n".join(
        [f"FILE: {k}\n{v[:2000]}" for k, v in repo_files.items()]
    )

    prompt = f"""
You are an execution agent.

Follow ALL rules in AGENTS.md:
{agents_md}

Repository snapshot:
{context}

Execute this step:
{step}

Output JSON:
{{
  "changes": [
    {{
      "file": "filename.md",
      "content": "FULL updated file content"
    }}
  ]
}}
"""

    response = run_ollama(MODEL_EXECUTOR, prompt)

    try:
        return json.loads(response)
    except:
        print("⚠️ Failed to parse execution. Raw output:\n", response)
        return {"changes": []}


# ---------- Apply Changes ----------
def apply_changes(changes):
    for change in changes:
        file_path = Path(change["file"])
        old = file_path.read_text() if file_path.exists() else ""
        new = change["content"]

        file_path.write_text(new)

        print(f"\n📝 Updated: {file_path}")
        print_diff(old, new)


def print_diff(old, new):
    import difflib
    diff = difflib.unified_diff(
        old.splitlines(),
        new.splitlines(),
        lineterm=""
    )
    print("\n".join(diff))


# ---------- Main ----------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task", help="Task for the agent")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print("🤖 Agent starting...\n")

    agents_md = load_agents_md()
    repo_files = load_repo_files()

    print("🧠 Planning...")
    plan = plan_task(args.task, agents_md)
    steps = plan.get("steps", [])

    for i, step in enumerate(steps, 1):
        print(f"\n➡️ Step {i}: {step}")

        result = execute_step(step, agents_md, repo_files)
        changes = result.get("changes", [])

        if not changes:
            print("⚠️ No changes proposed.")
            continue

        if args.dry_run:
            print("🔍 Dry run (no files written)")
            for c in changes:
                print(f"- {c['file']}")
            continue

        apply_changes(changes)


if __name__ == "__main__":
    main()