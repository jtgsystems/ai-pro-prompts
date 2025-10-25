"""
AI-Pro-Prompts Command Line Interface

Provides CLI commands for generating professional AI agent templates.
"""

import os
import sys
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table
from .prompt_generator import PromptGenerator
from .batch_generator import BatchGenerator

console = Console()


@click.group()
@click.version_option(version="1.0.0", prog_name="AI-Pro-Prompts")
def main():
    """
    AI-Pro-Prompts: Professional AI Agent Templates

    Generate customized prompts for 67+ professions and careers.
    """
    pass


@main.command()
@click.option(
    "--profession",
    "-p",
    prompt="Profession",
    help="Job title or profession (e.g., 'SEO Specialist')",
)
@click.option(
    "--goal",
    "-g",
    prompt="Goal",
    help="Specific goal (e.g., '#1 Google Rankings Achievement')",
)
@click.option(
    "--industry",
    "-i",
    default=None,
    help="Industry or field (optional)",
)
@click.option(
    "--experience",
    "-e",
    default="Intermediate",
    type=click.Choice(["Beginner", "Intermediate", "Advanced", "Expert"]),
    help="Experience level",
)
@click.option(
    "--backend",
    "-b",
    default="ollama",
    type=click.Choice(["ollama", "openai"]),
    help="LLM backend to use",
)
@click.option(
    "--model",
    "-m",
    default="granite4",
    help="Model name (e.g., 'granite4' for Ollama, 'gpt-4' for OpenAI)",
)
@click.option(
    "--output",
    "-o",
    default="./templates",
    help="Output directory for templates",
)
def generate(profession, goal, industry, experience, backend, model, output):
    """
    Generate a single professional template.

    Example:
        ai-pro-prompts generate -p "SEO Specialist" -g "#1 Google Rankings"
    """
    try:
        console.print(
            f"\n📋 Generating template for [bold cyan]{profession}[/bold cyan]...\n"
        )

        # Create output directory
        os.makedirs(output, exist_ok=True)

        # Initialize generator
        generator = PromptGenerator(backend=backend, model=model)

        # Generate template
        content = generator.generate(
            profession=profession,
            goal=goal,
            industry=industry,
            experience_level=experience,
        )

        # Save template
        filepath = generator.save_template(profession, goal, content, output)

        console.print(f"✅ [green]Successfully generated![/green]")
        console.print(f"📁 Saved to: [bold]{filepath}[/bold]\n")

    except Exception as e:
        console.print(f"❌ [red]Error: {str(e)}[/red]\n", err=True)
        sys.exit(1)


@main.command()
@click.option(
    "--csv",
    "-c",
    required=True,
    type=click.Path(exists=True),
    help="Path to CSV file with profession-goal pairs",
)
@click.option(
    "--output",
    "-o",
    default="./templates",
    help="Output directory for templates",
)
@click.option(
    "--backend",
    "-b",
    default="ollama",
    type=click.Choice(["ollama", "openai"]),
    help="LLM backend to use",
)
@click.option(
    "--model",
    "-m",
    default="granite4",
    help="Model name",
)
@click.option(
    "--workers",
    "-w",
    default=2,
    type=int,
    help="Number of parallel workers",
)
@click.option(
    "--skip-existing",
    is_flag=True,
    default=True,
    help="Skip already generated templates",
)
def batch(csv, output, backend, model, workers, skip_existing):
    """
    Generate multiple templates from a CSV file.

    CSV Format:
        profession,goal,industry,experience_level
        SEO Specialist,#1 Google Rankings,Marketing,Intermediate
        Data Scientist,ML Model Deployment,Data & Analytics,Advanced

    Example:
        ai-pro-prompts batch --csv professions.csv --workers 4
    """
    try:
        console.print(
            f"\n🚀 Starting batch generation from [bold cyan]{csv}[/bold cyan]\n"
        )

        # Create output directory
        os.makedirs(output, exist_ok=True)

        # Initialize batch generator
        batch_gen = BatchGenerator(
            backend=backend,
            model=model,
            max_workers=workers,
        )

        # Generate from CSV
        results = batch_gen.generate_from_csv(csv, output, skip_existing)

        # Display results
        console.print(f"\n✅ [green]Batch generation complete![/green]\n")
        console.print(f"📊 Generated {len(results)} templates")
        console.print(f"📁 Output directory: [bold]{output}[/bold]\n")

    except Exception as e:
        console.print(f"❌ [red]Error: {str(e)}[/red]\n", err=True)
        sys.exit(1)


@main.command()
@click.option(
    "--backend",
    "-b",
    default="ollama",
    type=click.Choice(["ollama", "openai"]),
    help="LLM backend",
)
@click.option(
    "--model",
    "-m",
    default="granite4",
    help="Model name",
)
def check(backend, model):
    """
    Check configuration and LLM connectivity.

    Verifies that your chosen backend is properly configured.
    """
    console.print("\n🔍 Checking AI-Pro-Prompts configuration...\n")

    # Check environment
    table = Table(title="System Configuration")
    table.add_column("Setting", style="cyan")
    table.add_column("Status", style="green")

    # Backend check
    backend_status = "✅" if backend in ["ollama", "openai"] else "❌"
    table.add_row("Backend", f"{backend_status} {backend}")

    # Model check
    table.add_row("Model", f"✅ {model}")

    # Environment files
    env_exists = os.path.exists(".env")
    table.add_row(".env File", f"{'✅' if env_exists else '⚠️ '} {'Found' if env_exists else 'Missing'}")

    # Output directory
    output_dir = os.getenv("OUTPUT_DIR", "./templates")
    table.add_row("Output Dir", f"📁 {output_dir}")

    console.print(table)

    # Backend-specific checks
    console.print("\n🌐 Backend Connectivity:\n")

    if backend == "ollama":
        try:
            import requests

            ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
            response = requests.get(f"{ollama_host}/api/tags", timeout=5)
            if response.status_code == 200:
                console.print(f"✅ [green]Ollama is running at {ollama_host}[/green]\n")
            else:
                console.print(
                    f"⚠️  [yellow]Ollama returned status {response.status_code}[/yellow]\n"
                )
        except Exception as e:
            console.print(
                f"❌ [red]Cannot connect to Ollama: {str(e)}[/red]\n"
            )

    elif backend == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            masked_key = api_key[:10] + "..." + api_key[-4:]
            console.print(f"✅ [green]OpenAI API key configured: {masked_key}[/green]\n")
        else:
            console.print(
                "❌ [red]OpenAI API key not found. Set OPENAI_API_KEY in .env[/red]\n"
            )

    console.print("✨ Configuration check complete!\n")


@main.command()
def init():
    """
    Initialize AI-Pro-Prompts in the current directory.

    Creates .env file and templates directory.
    """
    console.print("\n⚙️  Initializing AI-Pro-Prompts...\n")

    # Create .env if it doesn't exist
    if not os.path.exists(".env"):
        env_content = """# AI-Pro-Prompts Environment Configuration

# LLM Backend Selection
# Options: "ollama" or "openai"
LLM_BACKEND=ollama

# For Ollama Backend
OLLAMA_MODEL=granite4
OLLAMA_HOST=http://localhost:11434

# For OpenAI Backend (uncomment if using OpenAI)
# OPENAI_API_KEY=your_api_key_here
# OPENAI_MODEL=gpt-4

# Output Directory for Generated Templates
OUTPUT_DIR=./templates

# Batch Generation Settings
MAX_PARALLEL_JOBS=2
SKIP_EXISTING_TEMPLATES=true

# Logging
LOG_LEVEL=INFO
"""
        with open(".env", "w") as f:
            f.write(env_content)
        console.print("✅ [green]Created .env file[/green]")
    else:
        console.print("ℹ️  .env file already exists")

    # Create templates directory
    os.makedirs("templates", exist_ok=True)
    console.print("✅ [green]Created templates directory[/green]")

    console.print(
        "\n✨ Initialization complete! Run [bold]ai-pro-prompts --help[/bold] to get started.\n"
    )


@main.command()
def list_professions():
    """
    List all available professions.

    Shows the 67+ professions that can be used for template generation.
    """
    professions = [
        "SEO Specialist",
        "Data Scientist",
        "Full Stack Developer",
        "Accountant",
        "Business Consultant",
        "Project Manager",
        "Product Manager",
        "HR Manager",
        "Virtual Assistant",
        "Frontend Developer",
        "Backend Developer",
        "Mobile App Developer",
        "DevOps Engineer",
        "Cloud Architect",
        "Database Administrator",
        "QA Engineer",
        "Digital Marketer",
        "Content Manager",
        "Video Producer",
        "Graphic Designer",
        "UX/UI Designer",
        "Financial Analyst",
        "Investment Banker",
        "Sales Manager",
        "Customer Success Manager",
        "Technical Writer",
        "Social Media Manager",
        "Email Marketer",
        "Brand Manager",
        "E-commerce Manager",
        "Logistics Manager",
        "Supply Chain Manager",
        "Operations Manager",
        "Manufacturing Engineer",
        "Product Designer",
        "Mechanical Engineer",
        "Software Architect",
        "Security Engineer",
        "Machine Learning Engineer",
        "Data Engineer",
        "Systems Administrator",
        "Network Engineer",
        "Help Desk Technician",
        "IT Manager",
        "Legal Consultant",
        "Patent Attorney",
        "Real Estate Agent",
        "Interior Designer",
        "Architect",
        "Civil Engineer",
        "Environmental Specialist",
        "Chemist",
        "Biologist",
        "Physicist",
        "Research Scientist",
        "Academic Professor",
        "Instructor/Trainer",
        "Career Counselor",
        "Healthcare Administrator",
        "Nurse",
        "Physician",
        "Therapist",
        "Fitness Coach",
        "Nutritionist",
        "Event Planner",
        "Travel Agent",
        "Photographer",
    ]

    console.print("\n📚 Available Professions for Template Generation:\n")

    table = Table(title="AI-Pro-Prompts Professions")
    table.add_column("No.", style="cyan", width=4)
    table.add_column("Profession", style="green")

    for i, prof in enumerate(professions, 1):
        table.add_row(str(i), prof)

    console.print(table)
    console.print(
        f"\n✨ Total: {len(professions)}+ professions available\n"
    )


@main.command()
def show_template():
    """
    Display an example generated template.

    Shows what a generated professional template looks like.
    """
    example = """# SEO Specialist - #1 Google Rankings Achievement

## 🎯 Overview
As an SEO Specialist focused on achieving #1 Google rankings, your goal is to systematically improve search visibility,
drive organic traffic, and establish domain authority for targeted keywords.

## 📋 Phase 1: Information Gathering & Context Setup
- What is the current website structure and technical foundation?
- What keywords are being targeted?
- Who are the main competitors ranking in the top 10?
- What is the current search visibility and traffic baseline?
- What content assets already exist?

## 📊 Phase 2: Research & Analysis
- Conduct comprehensive keyword research and competitor analysis
- Analyze backlink profiles of top-ranking competitors
- Identify content gaps and opportunities
- Assess on-page SEO factors (meta tags, headers, internal linking)
- Evaluate technical SEO issues

## 🚀 Phase 3: Execution Workflow
- Optimize on-page elements for target keywords
- Create high-quality, comprehensive content
- Build backlinks through outreach and partnerships
- Optimize for Core Web Vitals and page speed
- Implement schema markup and structured data

## ⚡ Phase 4: Optimization & Refinement
- Monitor keyword rankings weekly
- Analyze user behavior and engagement metrics
- Refine content based on search intent
- Improve click-through rates in SERPs
- Iterate based on performance data

## 📈 Phase 5: Reporting & Documentation
- Create weekly ranking reports
- Track traffic and conversion metrics
- Document all optimization changes
- Present findings to stakeholders
- Plan next steps based on results
"""
    console.print(example)


if __name__ == "__main__":
    main()
