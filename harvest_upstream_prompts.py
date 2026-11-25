#!/usr/bin/env python3
"""
harvest_upstream_prompts.py
Multi-Repo GitHub Prompt Harvester

Discovers, clones, and synchronizes the world's highest-starred and most comprehensive
AI prompt libraries into categorized collections under ~/Desktop/prompts/imported_libraries.
"""
import os
import subprocess
try:
    import orjson

    class _JsonFastAdapter:
        JSONDecodeError = orjson.JSONDecodeError
        @staticmethod
        def loads(obj, **kwargs):
            return orjson.loads(obj)
        @staticmethod
        def dumps(obj, **kwargs):
            opt = 0
            if kwargs.pop("sort_keys", False):
                opt |= orjson.OPT_SORT_KEYS
            if kwargs.pop("indent", None):
                opt |= orjson.OPT_INDENT_2
            return orjson.dumps(obj, option=opt).decode("utf-8")
        @staticmethod
        def load(fp, **kwargs):
            return orjson.loads(fp.read())
        @staticmethod
        def dump(obj, fp, **kwargs):
            fp.write(_JsonFastAdapter.dumps(obj, **kwargs))

    json = _JsonFastAdapter()
except ImportError:
    import json
import time
from pathlib import Path

TARGET_BASE = Path("/home/batman/Desktop/prompts/imported_libraries")
TARGET_BASE.mkdir(parents=True, exist_ok=True)

TOP_PROMPT_REPOSITORIES = [
    # Master System Prompts & Reverse-Engineered Agent Prompts
    ("x1xhlol/system-prompts-and-models-of-ai-tools", "master-system-prompts"),
    ("jujumilk3/leaked-system-prompts", "leaked-system-prompts"),
    ("LouisShark/chatgpt_system_prompt", "chatgpt-system-prompts"),
    ("asgeirtj/system_prompts", "asgeir-system-prompts"),
    ("elder-plinius/CL4R1T4S", "plinius-claritas-prompts"),
    ("dontriskit/awesome-ai-system-prompts", "awesome-ai-system-prompts"),

    # Massive Prompt Collections & Curated Libraries
    ("f/prompts.chat", "awesome-chatgpt-prompts"),
    ("0xeb/TheBigPromptLibrary", "the-big-prompt-library"),
    ("ai-boost/awesome-prompts", "awesome-prompts-curated"),
    ("PickleBoxer/dev-chatgpt-prompts", "developer-chatgpt-prompts"),
    ("alphatrait/100000-ai-prompts", "100k-ai-prompts-dataset"),
    ("TakSec/chatgpt-prompts-cybersecurity", "cybersecurity-prompts"),
    ("SabrinaRamonov/prompts", "free-prompts-library"),
    ("0aicoder0/Ultimate-Coding-Prompts", "ultimate-coding-prompts"),
    ("harish-garg/gemini-cli-prompts", "gemini-cli-prompts"),
    ("YouMind-OpenLab/awesome-nano-banana-prompts", "awesome-nano-prompts"),
    ("PlexPt/awesome-chatgpt-prompts-zh", "awesome-chatgpt-prompts-zh")
]

def clone_or_pull_repo(repo_slug: str, folder_name: str):
    dest_dir = TARGET_BASE / folder_name
    print(f"[*] Processing {repo_slug} -> {folder_name}...")
    
    if dest_dir.exists() and (dest_dir / ".git").exists():
        print(f"    Existing repo found. Running git pull...")
        try:
            res = subprocess.run(
                ["git", "pull", "--ff-only"],
                cwd=str(dest_dir),
                capture_output=True,
                text=True,
                timeout=60
            )
            print(f"    Pull output: {res.stdout.strip() or res.stderr.strip() or 'Up-to-date'}")
        except Exception as e:
            print(f"    Pull error: {e}")
    else:
        print(f"    Cloning {repo_slug}...")
        try:
            res = subprocess.run(
                ["git", "clone", "--depth", "1", f"https://github.com/{repo_slug}.git", str(dest_dir)],
                capture_output=True,
                text=True,
                timeout=120
            )
            if res.returncode == 0:
                print(f"    ✓ Successfully cloned {repo_slug}")
            else:
                print(f"    ✗ Clone failed: {res.stderr.strip()}")
        except Exception as e:
            print(f"    ✗ Clone exception: {e}")

def generate_prompt_catalog():
    """Generates an index of all harvested prompts by category."""
    catalog = {}
    total_files = 0
    total_bytes = 0
    
    for root, dirs, files in os.walk(TARGET_BASE):
        if ".git" in root:
            continue
        valid_files = [f for f in files if f.endswith((".md", ".txt", ".json", ".yaml", ".yml", ".py", ".csv"))]
        if valid_files:
            rel_dir = os.path.relpath(root, TARGET_BASE)
            size = sum(os.path.getsize(os.path.join(root, f)) for f in valid_files)
            catalog[rel_dir] = {
                "file_count": len(valid_files),
                "total_kb": round(size / 1024, 2)
            }
            total_files += len(valid_files)
            total_bytes += size
            
    summary_path = Path("/home/batman/Desktop/prompts/PROMPT_LIBRARIES_CATALOG.md")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("# 📚 Master AI Prompt Libraries Catalog\n\n")
        f.write(f"**Total Harvested Prompt Files**: {total_files:,}\n")
        f.write(f"**Total Storage Size**: {round(total_bytes / (1024*1024), 2)} MB\n")
        f.write(f"**Imported Repositories**: {len(TOP_PROMPT_REPOSITORIES)}\n\n")
        f.write("| Library / Subdirectory | File Count | Size (KB) |\n")
        f.write("| :--- | :---: | :---: |\n")
        for dir_name, stats in sorted(catalog.items()):
            f.write(f"| `{dir_name}` | {stats['file_count']} | {stats['total_kb']} KB |\n")
            
    print(f"\n[✓] Generated Master Catalog: {summary_path} ({total_files:,} files, {round(total_bytes/(1024*1024), 2)} MB)")

def main():
    print("=== STARTING MULTI-REPO AI PROMPTS HARVESTING ===")
    for repo_slug, folder_name in TOP_PROMPT_REPOSITORIES:
        clone_or_pull_repo(repo_slug, folder_name)
        # SOTA 2026: Non-blocking yield
        pass
        
    generate_prompt_catalog()
    print("=== HARVESTING COMPLETE ===")

if __name__ == "__main__":
    main()
