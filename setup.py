"""
AI-Pro-Prompts Setup Configuration

Professional AI agent templates for 67+ careers.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-pro-prompts",
    version="1.0.0",
    author="JTGSYSTEMS",
    author_email="contact@jtgsystems.com",
    description="Professional AI agent templates for 67+ careers. Pre-built prompts for Claude, GPT-4, Granite4, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtgsystems/ai-pro-prompts",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Business",
        "Topic :: Software Development :: Libraries",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "openai>=1.3.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0",
        "click>=8.1.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ai-pro-prompts=generators.cli:main",
        ],
    },
)
