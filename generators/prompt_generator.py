"""
Single Prompt Generator for AI-Pro-Prompts

Generates professional AI agent templates using Granite4 (Ollama) or OpenAI.
"""

import os
import json
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import requests

load_dotenv()


class PromptGenerator:
    """Generate professional AI agent templates for specific professions and goals."""

    def __init__(
        self,
        backend: str = "ollama",
        model: str = "granite4",
        ollama_host: str = "http://localhost:11434",
    ):
        """
        Initialize the prompt generator.

        Args:
            backend: "ollama" or "openai"
            model: Model name (e.g., "granite4" for Ollama, "gpt-4" for OpenAI)
            ollama_host: Ollama server URL (only for Ollama backend)
        """
        self.backend = backend
        self.model = model
        self.ollama_host = ollama_host
        self.api_key = os.getenv("OPENAI_API_KEY") if backend == "openai" else None

    def generate(
        self,
        profession: str,
        goal: str,
        industry: Optional[str] = None,
        experience_level: str = "Intermediate",
    ) -> str:
        """
        Generate a professional template.

        Args:
            profession: Job title (e.g., "SEO Specialist")
            goal: Specific goal (e.g., "#1 Google Rankings Achievement")
            industry: Industry category (optional)
            experience_level: Beginner, Intermediate, or Advanced

        Returns:
            Generated template text
        """
        prompt = self._build_prompt(profession, goal, industry, experience_level)

        if self.backend == "ollama":
            return self._generate_ollama(prompt)
        elif self.backend == "openai":
            return self._generate_openai(prompt)
        else:
            raise ValueError(f"Unknown backend: {self.backend}")

    def _build_prompt(
        self,
        profession: str,
        goal: str,
        industry: Optional[str],
        experience_level: str,
    ) -> str:
        """Build the generation prompt."""
        return f"""Create a comprehensive AI agent template for a {profession} with the following goal:

Goal: {goal}
Experience Level: {experience_level}
{f'Industry: {industry}' if industry else ''}

The template should follow this 5-phase framework:

1. **Information Gathering & Context Setup** - What information is needed?
2. **Research & Analysis** - How to analyze and understand the situation?
3. **Execution Workflow** - What's the step-by-step process?
4. **Optimization & Refinement** - How to improve the results?
5. **Reporting & Documentation** - How to document and share findings?

Provide a detailed, actionable template that a professional can use with an AI assistant."""

    def _generate_ollama(self, prompt: str) -> str:
        """Generate using Ollama backend."""
        try:
            response = requests.post(
                f"{self.ollama_host}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=300,
            )
            response.raise_for_status()
            return response.json()["response"]
        except Exception as e:
            raise RuntimeError(f"Ollama generation failed: {e}")

    def _generate_openai(self, prompt: str) -> str:
        """Generate using OpenAI backend."""
        try:
            import openai

            openai.api_key = self.api_key
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert at creating professional AI agent templates.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=2000,
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"OpenAI generation failed: {e}")

    def save_template(self, profession: str, goal: str, content: str, output_dir: str = "templates") -> str:
        """
        Save generated template to file.

        Args:
            profession: Job title
            goal: Specific goal
            content: Generated template content
            output_dir: Output directory

        Returns:
            Path to saved file
        """
        os.makedirs(output_dir, exist_ok=True)

        filename = f"{profession.upper()}---{goal.upper().replace(' ', '-')}.md"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, "w") as f:
            f.write(f"# {profession} - {goal}\n\n")
            f.write(content)

        return filepath


# Example usage
if __name__ == "__main__":
    generator = PromptGenerator(backend="ollama", model="granite4")

    template = generator.generate(
        profession="SEO Specialist",
        goal="Achieve #1 Google Rankings",
        industry="Marketing",
        experience_level="Beginner to Intermediate",
    )

    print(template)
