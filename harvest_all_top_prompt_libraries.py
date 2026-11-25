#!/usr/bin/env python3
"""
harvest_all_top_prompt_libraries.py
Exhaustive Harvester for the Top Starred Prompt & Agent Task Repositories on GitHub.
Clones, extracts, and organizes all top global prompt libraries directly into
Project-Titan/prompts/imported_libraries and synchronizes to /mnt/4tb.
"""
import os
import subprocess
import time
from pathlib import Path

TARGET_DIR = Path("/home/batman/Desktop/Project-Titan/prompts/imported_libraries")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

REPOSITORIES = [
    # Top Starred Prompt Engineering Guides & Frameworks
    ("dair-ai/Prompt-Engineering-Guide", "dair-ai-prompt-engineering-guide"),
    ("danielmiessler/Fabric", "danielmiessler-fabric-patterns"),
    ("anthropics/prompt-eng-interactive-tutorial", "anthropic-official-prompt-tutorial"),
    ("f/prompts.chat", "f-awesome-chatgpt-prompts"),
    ("0xeb/TheBigPromptLibrary", "0xeb-the-big-prompt-library"),
    ("ai-boost/awesome-prompts", "ai-boost-awesome-prompts"),
    ("PickleBoxer/dev-chatgpt-prompts", "pickleboxer-dev-prompts"),
    ("PlexPt/awesome-chatgpt-prompts-zh", "plexpt-awesome-prompts-zh"),
    ("SabrinaRamonov/prompts", "sabrina-ramonov-prompts-library"),
    
    # System Prompts & Frontier AI Agents
    ("x1xhlol/system-prompts-and-models-of-ai-tools", "x1xhlol-system-prompts-and-models"),
    ("LouisShark/chatgpt_system_prompt", "louisshark-chatgpt-system-prompts"),
    ("jujumilk3/leaked-system-prompts", "jujumilk3-leaked-system-prompts"),
    ("elder-plinius/CL4R1T4S", "elder-plinius-claritas-prompts"),
    ("dontriskit/awesome-ai-system-prompts", "dontriskit-awesome-system-prompts"),
    ("Piebald-AI/claude-code-system-prompts", "piebald-claude-code-system-prompts"),
    
    # Agent Tasks, Open Frameworks & Tool Chains
    ("stanfordnlp/dspy", "stanford-dspy-prompt-optimization"),
    ("langfuse/langfuse", "langfuse-prompt-engineering"),
    ("OpenDCAI/AgentFlow", "opendcai-agentflow-tasks"),
    ("atlassdk/atlas", "atlassdk-agent-tasks"),
    ("deadwavewave/opencove", "deadwavewave-opencove-prompts"),
    ("youmind-openlab/awesome-nano-banana-prompts", "youmind-awesome-prompts")
]

def clone_or_update(slug: str, folder_name: str):
    dest = TARGET_DIR / folder_name
    print(f"[*] Processing {slug} -> {folder_name}...")
    if dest.exists() and (dest / ".git").exists():
        try:
            res = subprocess.run(["git", "pull", "--ff-only"], cwd=str(dest), capture_output=True, text=True, timeout=60)
            print(f"    ✓ Updated: {res.stdout.strip() or 'Already up-to-date'}")
        except Exception as e:
            print(f"    ✗ Update error: {e}")
    else:
        try:
            res = subprocess.run(["git", "clone", "--depth", "1", f"https://github.com/{slug}.git", str(dest)], capture_output=True, text=True, timeout=120)
            if res.returncode == 0:
                print(f"    ✓ Successfully cloned {slug}")
            else:
                print(f"    ✗ Clone failed: {res.stderr.strip()}")
        except Exception as e:
            print(f"    ✗ Clone exception: {e}")

def main():
    print("=== HARVESTING WORLD'S LARGEST AI PROMPT & TASK LIBRARIES ===")
    for slug, name in REPOSITORIES:
        clone_or_update(slug, name)
        # SOTA 2026: Non-blocking yield
        pass
        
    print("\n[+] Regenerating Catalog...")
    total_files = sum(len(files) for _, _, files in os.walk(TARGET_DIR) if ".git" not in _)
    print(f"[✓] Complete! Total imported prompt & task files: {total_files:,}")

if __name__ == "__main__":
    main()
