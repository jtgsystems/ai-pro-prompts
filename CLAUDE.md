# AI-Pro-Prompts - Claude Code System Reference

## Project Overview

**AI-Pro-Prompts** is a comprehensive library of professional AI agent templates designed to accelerate workflow automation across 67+ career paths. The project generates structured, phase-based prompts that guide AI systems (Claude, GPT-4, Gemini, Granite4, etc.) in executing professional tasks with industry best practices.

### Core Purpose
- Eliminate prompt engineering overhead for common professional tasks
- Provide production-ready templates following a standardized 5-phase framework
- Support multiple LLM backends (Ollama/Granite4, OpenAI)
- Enable batch generation of profession-specific AI workflows

### Key Metrics
- **591+ Templates**: Pre-generated professional prompts
- **67 Professions**: Across 17 industry categories
- **10 Goals per Profession**: Specific, actionable objectives
- **5-Phase Framework**: Consistent structure from planning to reporting

---

## Directory Structure

```
ai-pro-prompts/
├── generators/                 # Python generation toolkit
│   ├── __init__.py            # Module initialization
│   ├── prompt_generator.py    # Single template generator
│   ├── batch_generator.py     # Parallel batch generation
│   └── cli.py                 # Click-based CLI interface
│
├── templates/                  # 591+ profession templates
│   ├── Business/              # Business professions
│   ├── Development/           # Software development roles
│   ├── Marketing/             # Digital marketing specialists
│   ├── Data/                  # Data science & analytics
│   ├── Design/                # Creative & UX design
│   ├── Finance/               # Accounting & financial analysis
│   ├── IT/                    # IT infrastructure & support
│   ├── E-commerce/            # Online retail & FBA
│   ├── Writing/               # Content & technical writing
│   └── [13 more categories]   # Legal, Media, Healthcare, etc.
│
├── README.md                   # Comprehensive documentation
├── CONTRIBUTING.md             # Contribution guidelines
├── LICENSE                     # MIT License
├── setup.py                    # Python package configuration
├── requirements.txt            # Python dependencies
├── .env.example               # Environment configuration template
└── .gitignore                 # Git exclusions
```

### Template Organization

Templates are organized in two parallel structures:
1. **Flat structure**: All templates in `/templates` root (e.g., `SEO-SPECIALIST---GOAL.md`)
2. **Category structure**: Templates organized in category subdirectories

**Naming Convention**: `PROFESSION-NAME---GOAL-DESCRIPTION.md`
- Example: `SEO-ANALYST---REPORTING--RECOMMENDATIONS.md`
- Example: `FULL-STACK-DEVELOPER---PRODUCTION-READY-WEB-APPLICATION.md`

---

## Technology Stack

### Core Technologies

#### Python Backend
- **Python**: 3.8+ (primary language)
- **Purpose**: Template generation, CLI tools, batch processing

#### Key Dependencies
```
requests>=2.31.0       # HTTP client for API calls
openai>=1.3.0         # OpenAI API integration
python-dotenv>=1.0.0  # Environment configuration
pyyaml>=6.0           # YAML parsing
click>=8.1.0          # CLI framework
rich>=13.0.0          # Terminal formatting/tables
```

### LLM Backends

#### 1. Ollama (Local, Recommended)
- **Model**: Granite4 (IBM's enterprise AI model)
- **Host**: `http://localhost:11434` (default)
- **Benefits**:
  - No API costs
  - Full data privacy
  - Unlimited generation
  - Offline capability
- **Use Case**: Bulk template generation, development, testing

#### 2. OpenAI API (Cloud)
- **Models**: GPT-4, GPT-4 Turbo
- **Benefits**:
  - Higher quality output
  - Faster generation
  - No local infrastructure
- **Use Case**: Premium templates, quick prototyping

### Development Tools
- **setuptools**: Python packaging
- **ThreadPoolExecutor**: Parallel batch processing
- **Click**: Command-line interface framework
- **Rich**: Terminal UI with tables/formatting

---

## Template Framework (5-Phase System)

Every profession template follows this standardized structure:

### Phase 1: Information Gathering & Context Setup
- **Purpose**: Define required inputs and validate data quality
- **Outputs**: Checklists, baseline metrics, input validation
- **Example**: Website URL, target keywords, business objectives

### Phase 2: Research & Analysis
- **Purpose**: Deep-dive into 10-12 critical knowledge areas
- **Outputs**: Industry research, tool comparisons, best practices
- **Example**: SEO fundamentals, keyword research tools, competitor analysis

### Phase 3: Execution Workflow
- **Purpose**: Step-by-step actionable process
- **Outputs**: 8-12 detailed implementation steps with tools/timelines
- **Example**: On-page optimization, content creation, link building

### Phase 4: Optimization & Refinement
- **Purpose**: Measure, analyze, and iterate
- **Outputs**: KPIs, performance metrics, continuous improvement cycles
- **Example**: Weekly ranking reports, A/B testing, conversion tracking

### Phase 5: Reporting & Documentation
- **Purpose**: Document findings and share with stakeholders
- **Outputs**: Executive summaries, detailed reports, next steps
- **Example**: Traffic analytics, ROI reports, strategic recommendations

---

## Development Workflow

### Installation & Setup

```bash
# Clone repository
git clone https://github.com/jtgsystems/ai-pro-prompts.git
cd ai-pro-prompts

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your LLM backend settings

# Install package (development mode)
pip install -e .
```

### Environment Configuration

Edit `.env` file:

```bash
# LLM Backend Selection
LLM_BACKEND=ollama              # or "openai"

# Ollama Settings
OLLAMA_MODEL=granite4
OLLAMA_HOST=http://localhost:11434

# OpenAI Settings (if using)
# OPENAI_API_KEY=sk-...
# OPENAI_MODEL=gpt-4

# Output Configuration
OUTPUT_DIR=./templates
MAX_PARALLEL_JOBS=2
SKIP_EXISTING_TEMPLATES=true
LOG_LEVEL=INFO
```

### Running the CLI

#### Initialize Project
```bash
# Create .env and templates directory
python -m generators.cli init
```

#### Check Configuration
```bash
# Verify LLM connectivity and settings
python -m generators.cli check --backend ollama --model granite4
```

#### List Available Professions
```bash
# Display all 67+ professions
python -m generators.cli list-professions
```

#### Generate Single Template
```bash
# Interactive prompts
python -m generators.cli generate

# With arguments
python -m generators.cli generate \
  --profession "SEO Specialist" \
  --goal "#1 Google Rankings Achievement" \
  --industry "Marketing" \
  --experience "Intermediate" \
  --backend ollama \
  --model granite4 \
  --output ./templates
```

#### Batch Generation from CSV
```bash
# Create CSV file (professions.csv):
# profession,goal,industry,experience_level
# SEO Specialist,#1 Google Rankings,Marketing,Intermediate
# Data Scientist,ML Model Deployment,Data & Analytics,Advanced

# Generate from CSV
python -m generators.cli batch \
  --csv professions.csv \
  --workers 2 \
  --backend ollama \
  --skip-existing
```

### Python API Usage

#### Single Template Generation
```python
from generators.prompt_generator import PromptGenerator

# Initialize generator
generator = PromptGenerator(backend="ollama", model="granite4")

# Generate template
template = generator.generate(
    profession="SEO Specialist",
    goal="Achieve #1 Google Rankings",
    industry="Marketing",
    experience_level="Intermediate"
)

# Save to file
filepath = generator.save_template(
    profession="SEO Specialist",
    goal="Google Rankings",
    content=template,
    output_dir="./templates"
)

print(f"Saved to: {filepath}")
```

#### Batch Generation
```python
from generators.batch_generator import BatchGenerator

# Initialize batch generator
batch_gen = BatchGenerator(
    backend="ollama",
    model="granite4",
    max_workers=2  # Parallel workers
)

# Generate from list
profession_goals = [
    {
        "profession": "SEO Specialist",
        "goal": "#1 Google Rankings",
        "industry": "Marketing"
    },
    {
        "profession": "Data Scientist",
        "goal": "Predictive ML Model",
        "industry": "Data & Analytics"
    }
]

results = batch_gen.generate_from_list(profession_goals)
print(f"Generated {len(results)} templates")

# Or generate from CSV
results = batch_gen.generate_from_csv(
    csv_file="professions.csv",
    output_dir="./templates",
    skip_existing=True
)
```

---

## Configuration & Setup

### Backend Selection

#### Ollama Setup (Recommended for Development)
```bash
# Install Ollama
# Visit: https://ollama.ai

# Pull Granite4 model
ollama pull granite4

# Verify installation
ollama list

# Start Ollama server (usually auto-starts)
ollama serve
```

#### OpenAI Setup
```bash
# Set environment variable
export OPENAI_API_KEY="sk-your-key-here"

# Or add to .env file
echo "OPENAI_API_KEY=sk-..." >> .env
echo "LLM_BACKEND=openai" >> .env
echo "OPENAI_MODEL=gpt-4" >> .env
```

### Performance Tuning

#### Parallel Processing
- **Max Workers**: 2-4 recommended (depends on hardware)
- **GPU Acceleration**: Ollama can use dual GPUs for faster generation
- **Rate Limiting**: OpenAI has rate limits; adjust workers accordingly

#### Generation Rate
- **Ollama + Granite4**: 2-3 templates per minute per GPU
- **OpenAI GPT-4**: 1-2 templates per minute (API limits)
- **Total Time (670 templates)**: 4-6 hours with 2 parallel workers

---

## Testing Approach

### Manual Testing
```bash
# Test single generation
python -m generators.cli generate -p "Test Profession" -g "Test Goal"

# Verify output
cat templates/TEST-PROFESSION---TEST-GOAL.md

# Test batch generation
echo "profession,goal" > test.csv
echo "Test Pro,Test Goal" >> test.csv
python -m generators.cli batch --csv test.csv --workers 1
```

### Template Quality Checks
1. **Structure Validation**: Ensure 5-phase framework is present
2. **Content Completeness**: Verify all sections have detailed content
3. **Actionability**: Confirm steps are specific and executable
4. **Tool Recommendations**: Check for free/paid tool suggestions
5. **Metadata**: Validate profession, goal, and industry fields

### Backend Connectivity
```bash
# Check Ollama
curl http://localhost:11434/api/tags

# Check configuration
python -m generators.cli check
```

---

## Performance Considerations

### Optimization Strategies

#### 1. Template Caching
- **Skip Existing**: Use `--skip-existing` flag to avoid regeneration
- **Incremental Builds**: Only generate new profession-goal pairs
- **Storage**: Templates are ~3-5KB each (minimal disk usage)

#### 2. Parallel Processing
- **ThreadPoolExecutor**: Built-in parallel batch generation
- **Worker Count**: 2 workers for dual GPU, 4 for high-RAM systems
- **Memory Usage**: ~500MB per worker during generation

#### 3. LLM Backend Selection
| Backend | Speed | Cost | Quality | Privacy |
|---------|-------|------|---------|---------|
| Ollama/Granite4 | Medium | Free | Good | Full |
| OpenAI GPT-4 | Fast | Paid | Excellent | API-dependent |

#### 4. Network Optimization
- **Local Ollama**: No network latency
- **OpenAI API**: Use retry logic for rate limits
- **Timeouts**: 300s timeout for slow generations

---

## Known Issues & Troubleshooting

### Common Issues

#### 1. Ollama Connection Failed
```
Error: Cannot connect to Ollama at http://localhost:11434
```
**Solution**:
```bash
# Start Ollama service
ollama serve

# Verify it's running
curl http://localhost:11434/api/tags

# Check .env configuration
cat .env | grep OLLAMA_HOST
```

#### 2. OpenAI Rate Limit Exceeded
```
Error: Rate limit exceeded for gpt-4
```
**Solution**:
- Reduce `--workers` count to 1
- Add delays between batches
- Upgrade OpenAI plan for higher limits

#### 3. Template Generation Timeout
```
Error: Ollama generation failed: timeout
```
**Solution**:
- Increase timeout in `prompt_generator.py` (line 100)
- Use faster model (e.g., `granite3` instead of `granite4`)
- Check system resources (CPU/GPU/RAM)

#### 4. Missing Dependencies
```
ModuleNotFoundError: No module named 'click'
```
**Solution**:
```bash
pip install -r requirements.txt
# Or install individually
pip install click rich requests openai python-dotenv pyyaml
```

#### 5. Template Quality Issues
- **Incomplete Sections**: Regenerate with more detailed prompt
- **Generic Content**: Use more specific profession/goal descriptions
- **Formatting Errors**: Check markdown rendering, regenerate if needed

### Debug Mode

Enable verbose logging:
```bash
# Set log level in .env
LOG_LEVEL=DEBUG

# Run with verbose output
python -m generators.cli generate -p "..." -g "..." --verbose
```

---

## Next Steps & Roadmap

### Immediate Priorities
1. **Template Completion**: Finish generating all 670 profession-goal templates
2. **Quality Assurance**: Review and refine existing templates
3. **Category Organization**: Standardize directory structure

### Short-Term Goals (1-3 Months)
1. **Web Interface**: Build search/browse UI for templates
2. **API Endpoints**: RESTful API for template access
3. **Enhanced CLI**: Add search, filter, preview commands
4. **Template Versioning**: Track template updates and improvements
5. **Community Contributions**: Accept PRs for new professions

### Long-Term Vision (3-12 Months)
1. **AI Agent Integration**: Direct integration with Claude, GPT-4 APIs
2. **Custom Template Builder**: Interactive template customization
3. **Workflow Automation**: Connect templates to execution engines
4. **Analytics Dashboard**: Track template usage and effectiveness
5. **Industry Partnerships**: Collaborate with professional organizations
6. **Certification System**: Validate template quality and best practices
7. **Multi-Language Support**: Translate templates to 10+ languages

### Feature Requests
- **Template Combinations**: Merge multiple profession templates
- **Role-Based Access**: Premium templates for subscribers
- **Live Updates**: Real-time industry best practice updates
- **AI Training Data**: Use templates to fine-tune custom models
- **Integration Plugins**: WordPress, Notion, Slack integrations

---

## Contributing

We welcome contributions! See `CONTRIBUTING.md` for guidelines.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-profession`)
3. Add templates following the 5-phase framework
4. Submit a pull request with clear description

### Areas Needing Help
- **New Professions**: Add templates for emerging careers (AI Engineer, Blockchain Developer, etc.)
- **Template Refinement**: Improve existing templates with real-world examples
- **Documentation**: Expand guides, tutorials, and use cases
- **Tooling**: Build automation scripts, CI/CD pipelines
- **Testing**: Create test suites for template validation

---

## Project Attribution

**Built by**: JTGSYSTEMS (https://www.jtgsystems.com)
**License**: MIT License
**Repository**: https://github.com/jtgsystems/ai-pro-prompts
**Contact**: contact@jtgsystems.com

### Technology Credits
- **Granite4**: IBM's enterprise AI model
- **Ollama**: Local LLM infrastructure
- **Python**: Core development language
- **Click**: CLI framework
- **Rich**: Terminal UI library

---

## Quick Reference

### Essential Commands
```bash
# Initialize project
python -m generators.cli init

# Check connectivity
python -m generators.cli check

# List professions
python -m generators.cli list-professions

# Generate single template
python -m generators.cli generate

# Batch generate from CSV
python -m generators.cli batch --csv file.csv

# Show example template
python -m generators.cli show-template
```

### File Locations
- **Templates**: `./templates/`
- **Configuration**: `.env`
- **Generator Code**: `./generators/`
- **Documentation**: `README.md`, `CONTRIBUTING.md`, `CLAUDE.md`

### Support Resources
- **GitHub Issues**: https://github.com/jtgsystems/ai-pro-prompts/issues
- **Documentation**: README.md
- **Email**: contact@jtgsystems.com
- **Website**: https://www.jtgsystems.com

---

*Last Updated: 2025-10-26*
*Version: 1.0.0*
*Status: Active Development*
