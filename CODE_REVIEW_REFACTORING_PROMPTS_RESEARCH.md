# EXHAUSTIVE RESEARCH REPORT: Best Code Refactoring, Code Review & Code Analysis Prompts
## Found on GitHub and the Web

**Research Date:** 2025  
**Sources Searched:** GitHub repositories, web articles, Gist collections, documentation sites  
**Total Unique Prompts Found:** 50+ specialized prompts across 10+ repositories  
**Total Dimensions Covered:** 10-15 unique quality dimensions per prompt  

---

## TABLE OF CONTENTS

1. [TIER 1: The Most Comprehensive "Super Prompts"](#tier-1)
2. [TIER 2: Multi-Phase Architecture Prompts](#tier-2)
3. [TIER 3: Specialized Dimension Prompts](#tier-3)
4. [TIER 4: Prompt Collections & Libraries](#tier-4)
5. [TIER 5: GitHub Official & Tool-Integrated Prompts](#tier-5)
6. [Comparative Analysis Matrix](#comparative-analysis)
7. [Key Patterns & Techniques Extracted](#key-patterns)

---

## TIER 1: THE MOST COMPREHENSIVE "SUPER PROMPTS" <a name="tier-1"></a>

### 1.1 Tech Debt Auditor (THE BEST OVERALL)
- **Source:** https://github.com/ai-boost/awesome-prompts/blob/main/prompts/tech_debt_auditor.txt
- **Based on:** ksimback/tech-debt-skill (Apr 2026)
- **Stars:** 8.3k (repository)
- **Prompt Size:** ~92 lines, 6.58 KB
- **Phases:** 3

**Structure:**
```
Phase 1: ORIENT (6 steps)
  - Read README, package manifest, architecture docs
  - Map directory structure
  - Review git history (last 200 commits)
  - Identify entry points, hot paths, cold corners
  - List top 20 largest files + 20 most modified files
  - Write 1-2 paragraph mental model

Phase 2: AUDIT (9 dimensions)
  1. Architectural decay
  2. Consistency rot
  3. Type & contract debt
  4. Test debt
  5. Dependency & config debt
  6. Performance & resource hygiene
  7. Error handling & observability
  8. Security hygiene
  9. Documentation drift

Phase 3: DELIVERABLE (7 sections)
  - Executive summary (max 10 bullets)
  - Architectural mental model
  - Findings table (ID | Category | File:Line | Severity | Effort | Description | Recommendation)
  - Top 5 "if you fix nothing else, fix these"
  - Quick wins
  - Things that look bad but are actually fine (REQUIRED)
  - Open questions for the maintainer
```

**Unique Verification/Gating Mechanisms:**
- Mandatory `file:line` citations for every finding
- "Looks bad but is actually fine" section (required - if empty, you didn't look hard enough)
- Stack-specific tooling integration (npm audit, ruff, cargo audit, etc.)
- Large repo protocol (>50k LOC → parallelize by module, cap 200 findings/module)
- Repeat run mode (reads prior audit, marks RESOLVED/NEW)
- Output rules: "No sycophancy. Tell the user what's broken."

---

### 1.2 Comprehensive Refactoring Strategy Prompt
- **Source:** https://github.com/flickleafy/prompt-engineering-models/blob/main/refactoring/12-comprehensive-refactoring/prompt.md
- **Size:** 430 lines, 13.2 KB
- **Phases:** 4 + 5 strategies

**Structure:**
```
Phase 1: Discovery
  - Map all quality issues across 9 dimensions
  - Identify root causes vs. symptoms
  - Find patterns
  - Establish baseline metrics

Phase 2: Dependency Analysis
  - Determine fix order
  - Identify blocking relationships
  - Find cascading benefits
  - Map prerequisites

Phase 3: Strategy Formulation
  - Group refactorings into themes
  - Sequence for safety and efficiency
  - Identify quick wins
  - Balance short-term vs long-term

Phase 4: Implementation Planning
  - Break into increments
  - Define success criteria
  - Establish rollback strategies
  - Plan testing approach

9 Quality Dimensions:
  - Code Smells, Architecture, Performance, Security
  - Testability, Readability, Modularity, Modernization, Technical Debt

5 Refactoring Strategies:
  - Bottom-Up (Foundation First)
  - Top-Down (Architecture First)
  - Risk-Based (Critical Path First)
  - Value-Based (ROI First)
  - Incremental (Continuous Improvement)
```

---

### 1.3 The Ultimate Refactoring Mega-Prompt (PromptsEra)
- **Source:** https://promptsera.com/ai-code-refactoring-prompt/
- **Published:** Feb 2026

**Structure:**
Uses Chain-of-Thought prompting + Constraint Engineering:
```
Role: Senior Staff Engineer
Pre-conditions:
  - Must preserve existing error handling logic
  - Must preserve database transaction boundaries
  - Must preserve third-party API payload structure

Required BEFORE writing code:
  - Bulleted list analyzing cyclomatic complexity
  - Identify exactly which functions to extract
  
Code Requirements:
  - Strict TypeScript interfaces
  - Early return patterns to reduce nesting
  - Highly descriptive variable names
  - Do not invent new dependencies
```

**Includes 5 Specialized Sub-Prompts:**
1. Performance Optimization Prompt
2. Code Readability and Clean Code Prompt
3. Object-Oriented Programming (OOP) Prompt
4. Security Audit Prompt
5. Legacy Framework Translation Prompt

---

## TIER 2: MULTI-PHASE ARCHITECTURE PROMPTS <a name="tier-2"></a>

### 2.1 Multi-Agent Code Review (Diffray.ai)
- **Source:** https://diffray.ai/multi-agent-code-review/
- **Architecture:** 10+ specialized AI agents
- **Claim:** 87% fewer false positives, 3x more real bugs detected

**9-Phase Pipeline:**
```
1. Clone         → Fetch repo & checkout PR
2. Data Prep     → Build dependency graph
3. Summarize     → LLM summarizes changes
4. Triage        → Route files to agents
5. Rules         → Load & filter rules
6. Review        → Parallel agent analysis
7. Dedupe        → Merge & rescore
8. Validation    → Verify & rescore
9. Report        → Generate PR comments
```

**Agent Types:**
- Security Agent, Performance Agent, Bug Detection Agent
- Architecture Agent, Testing Agent

**Key Innovation:** Context dilution avoidance (10-20% performance drop from too many documents)

---

### 2.2 Sub-Agent Refactor Command
- **Source:** https://raw.githubusercontent.com/derek-opdee/subagent-example-script/main/sub-agent-refactor.md
- **Architecture:** Multi-agent orchestration

**4-Stage Pipeline:**
```
Stage 1: Analysis Agent
  - Code Quality Analysis (code smells, complexity)
  - Duplication Detection (exact + 70%+ similar)
  - Pattern Analysis (naming, paradigms, error handling)
  - Dead Code Detection

Stage 2: Planning Agent
  - Sequenced refactoring steps
  - Dependency analysis
  - Impact assessment
  - Rollback planning

Stage 3: Implementation Agent
  - Execute refactorings
  - Maintain functionality
  - Apply patterns

Stage 4: Verification Agent
  - Test execution
  - Regression testing
  - Quality gate validation
```

---

### 2.3 Refactoring Coach (5-Step Diagnostic)
- **Source:** https://github.com/ai-boost/awesome-prompts/blob/main/prompts/refactoring_coach.txt
- **Inspired by:** Martin Fowler's refactoring catalog

**5-Step Process:**
```
Step 1: Diagnose quality issues
  - Code smells (long methods, feature envy, data clumps, primitive obsession)
  - High-complexity areas (cyclomatic complexity, nesting depth)
  - Duplication patterns and coupling

Step 2: Prioritize by impact and risk
  - Score: High/Medium/Low impact × High/Medium/Low risk
  - Sequence from lowest risk to highest
  - Identify test coverage prerequisites

Step 3: Propose concrete transformations
  - Name specific pattern (Extract Method, Replace Conditional with Polymorphism)
  - Show before/after code
  - Note behavior-preserving constraints

Step 4: Define safe refactoring sequence
  - Order steps for working code at each stage
  - Flag test runs after each step
  - Identify rollback checkpoints

Step 5: Recommend validation approach
  - Characterization tests
  - Regression check strategy
  - Code review checklist
```

---

### 2.4 Doubt-Driven Development Architect
- **Source:** https://github.com/ai-boost/awesome-prompts
- **Based on:** addyosmani/agent-skills (2026, 54.7k+ stars)

**CLAIM → EXTRACT → DOUBT → RECONCILE → STOP Cycle**
```
1. CLAIM:    Isolate the artifact + contract
2. EXTRACT:  Pull out the decision being made
3. DOUBT:    Apply adversarial reasoning (fresh context)
4. RECONCILE: Resolve doubts with evidence
5. STOP:     Bounded doubt theater with cross-model escalation
```

**Key Innovation:** Forbids passing the claim to the reviewer, isolates artifact from reviewer bias

---

### 2.5 Expert Persona Multi-Reviewer System (John Lindquist)
- **Source:** https://gist.github.com/johnlindquist/00dd3f91e8683e41d4881b23b8d5cf05

**12 Expert Personas:**
```
Architecture & Design:
  fowler  → Refactoring, code smells, evolutionary architecture
  grace   → Abstraction integrity, substitutability, SOLID
  dean    → Planet-scale systems, distributed reliability

Performance & Low-Level:
  carmack → Low-level excellence, cache optimization
  perf    → Observability, tracing, data-first analysis
  bjarne  → Performance via abstraction, type safety

Systems & Rigor:
  linus   → Kernel-level rigor, brutally honest feedback
  unix    → Small sharp tools, composability
  rob     → Go/Unix minimalism, concurrency

Type Systems & Languages:
  anders  → Strong typing, TypeScript, API ergonomics
  lattner → Compiler innovation, language interop

Testing & Practices:
  beck    → TDD discipline, rapid feedback loops
  github  → CI/CD, collaboration, documentation
```

---

## TIER 3: SPECIALIZED DIMENSION PROMPTS <a name="tier-3"></a>

### 3.1 Senior Code Reviewer (LogicBalls) - 5 Dimensions
- **Source:** https://logicballs.com/ai-prompt/prompts/senior-code-reviewer
- **2,943 copies, 4.3 rating**

```
Review Framework:
1. Correctness (logical errors, edge cases)
2. Security (SQL injection, XSS, auth, input validation)
3. Performance (time/space complexity, DB optimization, caching, memory leaks)
4. Readability (naming, comments, structure, DRY)
5. Maintainability (modularity, testability, error handling, logging)

Output: 🔴 Critical / 🟡 Recommendations / 🟢 Suggestions / ✅ Good
+ Overall Score X/10
```

---

### 3.2 Comprehensive Code Review - 10 Dimensions
- **Source:** https://github.com/aezizhu/shortcut-mcp (500+ word prompt)

```
1. FUNCTIONALITY & CORRECTNESS
2. CODE QUALITY & READABILITY
3. PERFORMANCE & EFFICIENCY
4. SECURITY CONSIDERATIONS
5. ERROR HANDLING & RESILIENCE
6. TESTING & TESTABILITY
7. ARCHITECTURE & DESIGN PATTERNS
   (SOLID, coupling, cohesion, dependency injection, modularity, scalability)
8. DOCUMENTATION & COMMENTS
9. DEPENDENCIES & COMPATIBILITY
10. MAINTAINABILITY & FUTURE-PROOFING

Output: Critical Issues / Major Concerns / Minor Suggestions / Positive Feedback / Learning Opportunities
```

---

### 3.3 Modularity & Decoupling Prompt - 6 Coupling Types
- **Source:** https://github.com/flickleafy/prompt-engineering-models/blob/main/refactoring/08-modularity-decoupling/prompt.md
- **Size:** 425 lines, 12.9 KB

```
Coupling Types (worst to best):
1. Content Coupling   → One module modifying internal data of another
2. Common Coupling    → Multiple modules sharing global data
3. External Coupling   → Dependency on external format/protocol
4. Control Coupling    → Passing flags to control module behavior
5. Stamp Coupling      → Passing entire data structures when only part needed
6. Data Coupling       → Parameters are simple data types (BEST)

Plus 3 Cohesion Types analyzed:
- Functional, Sequential, Communicational, Procedural, Temporal, Logical, Coincidental
```

---

### 3.4 Verification Specialist (Adversarial Validation)
- **Source:** https://github.com/ai-boost/awesome-prompts/blob/main/prompts/verification_specialist.txt

```
Core Philosophy: "Your job is not to confirm — it's to try to BREAK it"

Verification Strategies by Type:
- Frontend/UI: Browser automation, curl subresources
- Backend/API: Curl endpoints, send bad input
- CLI/Script: Edge-case inputs (empty, very large, malformed)
- Infrastructure: Dry-run commands
- Library/Package: Build, test, import from fresh context
- Bug Fixes: Reproduce original bug first
- Refactoring: Test suite must pass without modification

Universal Steps:
1. Read README for build/test commands
2. Run build (broken = automatic FAIL)
3. Run full test suite (failing = automatic FAIL)
4. Run linters and type-checkers
5. Check regressions in adjacent areas

Adversarial Probes: Run at least one before issuing any PASS
Anti-Rationalization Guards: 6 "if you catch yourself thinking" warnings
```

---

### 3.5 Automated Refactoring Pipeline (FlightVin)
- **Source:** https://github.com/FlightVin/automated-refactoring

```
Pipeline:
1. Cron job triggers periodically
2. Pull main branch
3. Design smell detection (LLM-assisted)
4. Per-file refactoring based on smells
5. Automatic PR creation with:
   - Detected design smells
   - Applied refactoring techniques
   - Relevant metrics
```

---

## TIER 4: PROMPT COLLECTIONS & LIBRARIES <a name="tier-4"></a>

### 4.1 Prompt Engineering Models (flickleafy)
- **Source:** https://github.com/flickleafy/prompt-engineering-models
- **37+ code review prompts, 14 refactoring prompts**

**Refactoring Collection (14 categories):**
```
01. Code Smells Detection
02. SOLID Principles (SRP, OCP, LSP, ISP, DIP)
03. Design Patterns Application
04. Technical Debt Reduction
05. Performance Refactoring
06. Testability Improvement
07. Readability Enhancement
08. Modularity & Decoupling
09. Modernization
10. Security Hardening
11. Language & Stack-Specific (Python, JS/TS, React)
12. Comprehensive Refactoring (holistic, multi-dimensional)
13. Extract & Simplify
14. Legacy Modernization
```

**Code Review Collection (37+ prompts):**
```
General Review Types (10):
  - Comprehensive PR Review, Security-Focused, Performance
  - Architecture & Design, Quick Scan, Test Coverage
  - Breaking Changes & API, Documentation, Cross-File Impact
  - Python-specific

Language-Specific (27):
  - JS/TS Core (6), React Ecosystem (5), Angular (2)
  - Vue (4), Svelte (2), Meta-Frameworks (2)
  - Backend (2), API & GraphQL (1), Testing (1)
```

---

### 4.2 Awesome Prompts (ai-boost) - 8.3k stars
- **Source:** https://github.com/ai-boost/awesome-prompts
- **300+ prompts for GPT store**

**Code-Related Prompts:**
```
🏛 Tech Debt Auditor
🧐 Doubt-Driven Development Architect
🎯 Andrej Karpathy Coding Guidelines
🧰 Coding Agent System Prompt
🏛 Solution Architect
✅ Verification Specialist
🧱 Codebase Knowledge Graph Architect
🏗 Parallel Codegen Architect
⚡ Performance Profiler
🧹 Refactoring Coach
🧠 Emotion-Aware Engineering Partner
📊 Technical Diagram Engineer
🏭 Opinionated Agent Team Designer
🕸 Web Quality Auditor
```

---

### 4.3 Prompt Library (xixu-me) - 109 stars
- **Source:** https://github.com/xixu-me/prompt-library

**Development Prompts:**
```
- architecture-planner.md
- bug-hunter.md
- code-review.md (5 dimensions with priority levels)
- documentation-generator.md
- refactoring-assistant.md (5 phases)
- test-case-generator.md
```

---

## TIER 5: GITHUB OFFICIAL & TOOL-INTEGRATED PROMPTS <a name="tier-5"></a>

### 5.1 GitHub Copilot Official Code Review Prompt
- **Source:** https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/review-code

```
5 Review Areas:
1. Security Issues (input validation, auth, data exposure, injection)
2. Performance & Efficiency (algorithm complexity, memory, DB queries)
3. Code Quality (readability, naming, function size, duplication)
4. Architecture & Design (design patterns, separation of concerns, dependencies)
5. Testing & Documentation (coverage, completeness, comments)

Output: 🔴 Critical Issues / 🟡 Suggestions / ✅ Good Practices
For each: line references, explanation, suggested solution with code example, rationale
```

### 5.2 GitHub Skills - Refactor
- **Source:** https://github.com/github/awesome-copilot

```
refactor: Surgical code refactoring
  - Extract functions, rename variables
  - Break down god functions
  - Improve type safety
  - Eliminate code smells
  - Apply design patterns

refactor-plan: Plan multi-file refactor
  - Investigate first
  - Output plan
  - Wait for confirmation before changes

refactor-method-complexity-reduce:
  - Reduce cognitive complexity
  - Extract helper methods
  - Mandatory test verification
```

### 5.3 Prompter - Multi-Step Refactoring Workflows
- **Source:** https://github.com/baijum/prompter

```
Features:
- Session resumption (context preservation across steps)
- Task-specific system prompts
- Verification commands (auto-pass/fail gates)
- Incremental refactoring sequences

Example Workflow:
  Task 1: Identify code smells
  Task 2: Refactor smell #1 (resume session)
  Task 3: Refactor smell #2 (resume session)
  
System Prompt Patterns:
  - Planning Before Execution
  - Safety-First Approach
  - Code Quality Enforcement (SOLID principles)
  - Learning and Documentation
```

---

## COMPARATIVE ANALYSIS MATRIX <a name="comparative-analysis"></a>

| Prompt | Phases | Dimensions | Scoring | Verification | Coupling/Cohesion | SOLID | Code Metrics |
|--------|--------|------------|---------|--------------|-------------------|-------|-------------|
| Tech Debt Auditor | 3 | 9 | Severity+Effort | Stack tools, file:line citations | Architectural decay | Implicit | Implicit |
| Comprehensive Refactoring | 4 | 9 | ROI analysis | Rollback strategies | Yes (separate) | Explicit | Explicit (cyclomatic) |
| GitHub Copilot Review | 1 | 5 | Traffic light | None | Implicit | Implicit | None |
| Senior Code Reviewer | 1 | 5 | X/10 | None | Implicit | Implicit | None |
| Refactoring Coach | 5 | 6 | Impact×Risk | Before/after, rollback checkpoints | Yes | Explicit (pattern names) | Cyclomatic, nesting |
| Verification Specialist | 1 | 11 types | PASS/FAIL/PARTIAL | Command output required | N/A | N/A | N/A |
| Modularity & Decoupling | 3 | 6 coupling + 7 cohesion | Levels | None | EXTENSIVE | Implicit | Afferent/efferent |
| 10-Dim Code Review | 1 | 10 | Critical/Major/Minor | None | Yes | Yes | None |
| Diffray Multi-Agent | 9 | 6 agents | Rescoring | Tool integration | Yes | Yes | Multiple |
| Doubt-Driven Architect | 5 | Adversarial | N/A | Cross-model escalation | N/A | N/A | N/A |
| Mega-Prompt (PromptsEra) | 2 | Constraint-based | N/A | Cyclomatic analysis | Implicit | Yes (SOLID named) | Cyclomatic |
| Refactoring Assistant | 5 | 5 | N/A | Testing recommendations | Implicit | Explicit | None |

---

## KEY PATTERNS & TECHNIQUES EXTRACTED <a name="key-patterns"></a>

### Most Effective Techniques:

1. **Chain-of-Thought (CoT):** Force the model to explain reasoning before generating code
2. **Constraint Engineering:** Explicitly tell the model what it CANNOT do
3. **Multi-Phase Pipelines:** Separate orient/audit/deliver phases
4. **Adversarial Validation:** "Try to break it" mentality
5. **Expert Personas:** Martin Fowler, Linus Torvalds, etc. for specialized reviews
6. **File:Line Citations:** Mandatory concrete references, no vague claims
7. **Stack-Specific Tooling:** npm audit, ruff, cargo clippy, etc.
8. **Behavior Preservation Constraints:** Explicitly preserve functionality
9. **Before/After Examples:** Concrete transformation demonstrations
10. **Scoring Systems:** X/10, Critical/High/Medium/Low, PASS/FAIL/PARTIAL
11. **"Looks Bad But Fine" Section:** Prevents false positives
12. **Rollback Checkpoints:** Safety mechanisms for multi-step refactoring
13. **Anti-Rationalization Guards:** Prevents the model from skipping checks

### Dimension Taxonomy (All Prompts Combined):

**Structural Quality:**
- Code smells (long methods, god classes, duplication)
- Coupling (6 types) and Cohesion (7 types)
- SOLID principles (5 principles)
- Design patterns (creational, structural, behavioral)
- Modularity and separation of concerns

**Functional Quality:**
- Correctness and logic errors
- Edge case handling
- Error handling and resilience
- Input validation

**Non-Functional Quality:**
- Performance (algorithmic complexity, Big-O)
- Security (OWASP, injection, XSS, auth)
- Testability and test coverage
- Readability and naming
- Documentation completeness
- Technical debt ratio

**Process Quality:**
- Consistency across codebase
- Dependency management
- Configuration hygiene
- Observability and logging
- Modernization level

---

## ALL SOURCE URLS

### Primary Sources:
1. https://github.com/ai-boost/awesome-prompts/blob/main/prompts/tech_debt_auditor.txt
2. https://github.com/flickleafy/prompt-engineering-models/blob/main/refactoring/12-comprehensive-refactoring/prompt.md
3. https://github.com/flickleafy/prompt-engineering-models/blob/main/refactoring/08-modularity-decoupling/prompt.md
4. https://github.com/xixu-me/prompt-library/blob/main/development/refactoring-assistant.md
5. https://github.com/xixu-me/prompt-library/blob/main/development/code-review.md
6. https://github.com/ai-boost/awesome-prompts/blob/main/prompts/refactoring_coach.txt
7. https://github.com/ai-boost/awesome-prompts/blob/main/prompts/verification_specialist.txt
8. https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files/review-code
9. https://github.com/github/awesome-copilot (refactor, refactor-plan skills)
10. https://github.com/baijum/prompter
11. https://github.com/FlightVin/automated-refactoring
12. https://promptsera.com/ai-code-refactoring-prompt/
13. https://diffray.ai/multi-agent-code-review/
14. https://logicballs.com/ai-prompt/prompts/senior-code-reviewer
15. https://github.com/aezizhu/shortcut-mcp
16. https://gist.github.com/johnlindquist/00dd3f91e8683e41d4881b23b8d5cf05
17. https://github.com/agigante80/vibe-coding-prompts
18. https://raw.githubusercontent.com/derek-opdee/subagent-example-script/main/sub-agent-refactor.md
19. https://www.claudepluginhub.com/commands/ai-foundry-core-code-refactoring-plugins-code-refactoring/commands/refactor-clean
20. https://github.com/PaulDuvall/centralized-rules
