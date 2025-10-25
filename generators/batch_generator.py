"""
Batch Prompt Generator for AI-Pro-Prompts

Generates multiple professional templates in parallel.
"""

import os
import csv
from typing import List, Dict, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from .prompt_generator import PromptGenerator


class BatchGenerator:
    """Generate multiple professional AI agent templates efficiently."""

    def __init__(
        self,
        backend: str = "ollama",
        model: str = "granite4",
        max_workers: int = 2,
        **kwargs
    ):
        """
        Initialize batch generator.

        Args:
            backend: "ollama" or "openai"
            model: Model name
            max_workers: Number of parallel generation jobs
        """
        self.generator = PromptGenerator(backend=backend, model=model, **kwargs)
        self.max_workers = max_workers

    def generate_from_csv(
        self,
        csv_file: str,
        output_dir: str = "templates",
        skip_existing: bool = True,
    ) -> Dict[str, str]:
        """
        Generate templates from CSV file.

        CSV format:
        profession,goal,industry,experience_level

        Args:
            csv_file: Path to CSV file
            output_dir: Output directory for templates
            skip_existing: Skip already generated templates

        Returns:
            Dictionary of generated files
        """
        tasks = []

        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                profession = row.get("profession", "").strip()
                goal = row.get("goal", "").strip()

                if not profession or not goal:
                    continue

                # Check if already exists
                filename = f"{profession.upper()}---{goal.upper().replace(' ', '-')}.md"
                filepath = os.path.join(output_dir, filename)

                if skip_existing and os.path.exists(filepath):
                    print(f"⏭️  Skipping existing: {profession} - {goal}")
                    continue

                tasks.append((profession, goal, row.get("industry"), row.get("experience_level", "Intermediate")))

        results = {}
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._generate_and_save, *task): task for task in tasks
            }

            for future in as_completed(futures):
                task = futures[future]
                try:
                    filepath = future.result()
                    results[f"{task[0]} - {task[1]}"] = filepath
                    print(f"✅ Generated: {task[0]} - {task[1]}")
                except Exception as e:
                    print(f"❌ Failed: {task[0]} - {task[1]}: {e}")

        return results

    def generate_from_list(
        self,
        profession_goals: List[Dict[str, str]],
        output_dir: str = "templates",
    ) -> Dict[str, str]:
        """
        Generate templates from list of profession-goal pairs.

        Args:
            profession_goals: List of dicts with 'profession' and 'goal' keys
            output_dir: Output directory

        Returns:
            Dictionary of generated files
        """
        results = {}

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {}
            for item in profession_goals:
                profession = item.get("profession", "").strip()
                goal = item.get("goal", "").strip()
                industry = item.get("industry")
                experience = item.get("experience_level", "Intermediate")

                if profession and goal:
                    future = executor.submit(
                        self._generate_and_save,
                        profession,
                        goal,
                        industry,
                        experience,
                        output_dir,
                    )
                    futures[future] = (profession, goal)

            for future in as_completed(futures):
                profession, goal = futures[future]
                try:
                    filepath = future.result()
                    results[f"{profession} - {goal}"] = filepath
                    print(f"✅ Generated: {profession} - {goal}")
                except Exception as e:
                    print(f"❌ Failed: {profession} - {goal}: {e}")

        return results

    def _generate_and_save(
        self,
        profession: str,
        goal: str,
        industry: Optional[str],
        experience_level: str,
        output_dir: str = "templates",
    ) -> str:
        """Generate and save a single template."""
        content = self.generator.generate(
            profession=profession,
            goal=goal,
            industry=industry,
            experience_level=experience_level,
        )
        return self.generator.save_template(profession, goal, content, output_dir)


# Example usage
if __name__ == "__main__":
    batch_gen = BatchGenerator(backend="ollama", model="granite4", max_workers=2)

    profession_goals = [
        {"profession": "SEO Specialist", "goal": "Achieve #1 Google Rankings", "industry": "Marketing"},
        {"profession": "Data Scientist", "goal": "Predictive ML Model Deployment", "industry": "Data & Analytics"},
        {"profession": "Full Stack Developer", "goal": "Production-Ready Web Application", "industry": "Development"},
    ]

    results = batch_gen.generate_from_list(profession_goals)
    print(f"\nGenerated {len(results)} templates")
