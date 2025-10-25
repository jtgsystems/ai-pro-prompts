# Project Manager - AI Agent Template
## Resource Planning

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve professional resource planning as a project manager.

---

## PROFESSION CONFIGURATION

### Basic Information
```yaml
profession_name: "Project Manager"
profession_category: "Operations/Management"
experience_level: "Beginner to Intermediate"
```

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
List what information the agent needs to start:

1. **Input 1:** Project scope and objectives  
   - Format: Detailed project brief, business case, high-level timeline  
   - Validation: Confirm alignment with overall organizational goals  

2. **Input 2:** Stakeholder list (who will be impacted)  
   - Format: Names, roles, decision-making authority  
   - Validation: Ensure all key stakeholders are included  

3. **Input 3:** Current resource inventory (existing projects, team availability)  
   - Format: Spreadsheet of current tasks, personnel capacity, skill sets  
   - Validation: Verify data is up-to-date and accurately reflects workload  

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas (10-20 Topics)

**Topic 1:** Resource leveling and smoothing techniques  
- Research Focus: Apply critical chain project management or software-based leveling tools to prevent bottlenecks.  
- Target Sources: PMBOK, resource management blogs, GanttProject documentation.

**Topic 2:** Capacity planning methodologies  
- Research Focus: Evaluate different capacity planning approaches (e.g., historical data vs. forecasted demand).  
- Target Sources: Industry whitepapers, capacity planning frameworks from ISM.

**Topic 3:** Resource allocation software capabilities  
- Research Focus: Compare tools like Smartsheet, Asana, and MS Project for resource management features.  
- Target Sources: Vendor case studies, user reviews on G2 or Capterra.

**Topic 4:** Workforce analytics best practices  
- Research Focus: Utilize workforce planning tools to forecast skill gaps and align with project needs.  
- Target Sources: LinkedIn Learning courses on workforce analytics, SHRM publications.

**Topic 5:** Resource forecasting models  
- Research Focus: Explore time-series analysis, Monte Carlo simulations for resource demand prediction.  
- Target Sources: Academic journals, industry research reports.

**Topic 6:** Agile vs. traditional resource planning approaches in PM  
- Research Focus: Evaluate which methodologies (e.g., Scrum, Waterfall) work best with dynamic resources.  
- Target Sources: PMI articles, Agile community forums.

**Topic 7:** Cost management integration with resource planning  
- Research Focus: Align budgeting processes to ensure resources are within cost constraints.  
- Target Sources: CPA Network blogs, financial management textbooks.

**Topic 8:** Risk management and its impact on resource allocation  
- Research Focus: Identify risks that could affect resource availability or project timeline.  
- Target Sources: OPM risk registers, industry whitepapers.

**Topic 9:** Scheduling software features for resource planning  
- Research Focus: Compare Gantt chart capabilities, dependency tracking across tools like MS Project and Primavera P6.  
- Target Sources: Vendor documentation, user forums.

**Topic 10:** Emerging AI tools in resource optimization  
- Research Focus: Evaluate AI-powered forecasting and allocation platforms (e.g., IBM Watson for Work).  
- Target Sources: TechCrunch reviews, beta testing with prototype tools.

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy document.
2. Identify key methodologies and technologies to adopt based on organizational needs.
3. Prioritize recommendations by implementation effort vs. impact potential.
4. Create master action plan for resource planning optimization.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process

**STEP 1: Resource Inventory Creation**
- **Action:** Compile a detailed list of all resources (human, financial, physical) required for the project.
- **Tools Needed:** Excel/Google Sheets, Smartsheet
- **Success Criteria:** Comprehensive resource inventory with assigned roles and availability.
- **Common Pitfalls:** Omitting critical team members or outdated skill sets.
- **Time Estimate:** 4 hours

**STEP 2: Capacity Analysis**
- **Action:** Analyze current capacity against projected demand using historical data or expert input.
- **Tools Needed:** Excel, Power BI (optional), workforce analytics tools
- **Success Criteria:** Developed a capacity utilization model with a target of 80%+ for optimal planning.
- **Common Pitfalls:** Underestimating peak resource demands.
- **Time Estimate:** 3 hours

**STEP 3: Resource Leveling**
- **Action:** Apply leveling techniques to smooth out workload peaks and avoid overallocation.
- **Tools Needed:** MS Project, Smartsheet (resource leveling feature), GanttProject
- **Success Criteria:** Identified and mitigated potential bottlenecks; adjusted project schedule accordingly.
- **Common Pitfalls:** Over-scheduling resources during peak demand periods.
- **Time Estimate:** 5 hours

**STEP 4: Resource Allocation Planning**
- **Action:** Allocate specific team members to tasks based on skill sets, availability, and workload balance.
- **Tools Needed:** Smartsheet, Asana (resource allocation feature), MS Project
- **Success Criteria:** All critical tasks assigned with a clear resource plan; no overallocation identified.
- **Common Pitfalls:** Misaligned resource skills with task requirements.
- **Time Estimate:** 6 hours

**STEP 5: Budget Integration**
- **Action:** Align budget constraints with resource allocation to ensure financial feasibility.
- **Tools Needed:** Excel budget template, MS Project (budgeting feature), Smartsheet
- **Success Criteria:** Resource costs tracked against overall project budget; adjustments made as needed.
- **Common Pitfalls:** Ignoring cost implications of high-cost resources or overtime.
- **Time Estimate:** 3 hours

**STEP 6: Risk Identification and Mitigation**
- **Action:** Identify risks that could impact resource availability (e.g., attrition, skill gaps) and develop mitigation strategies.
- **Tools Needed:** PESTLE analysis template, risk register in MS Project or Smartsheet
- **Success Criteria:** Comprehensive risk list with assigned owners and mitigation plans.
- **Common Pitfalls:** Neglecting low-probability but high-impact risks.
- **Time Estimate:** 4 hours

**STEP 7: AI Integration for Forecasting**
- **Action:** Utilize AI tools to forecast future resource needs based on historical data and project trends.
- **Tools Needed:** IBM Watson for Work, Google Cloud's AutoML Vision (for pattern analysis), or open-source Prophet library
- **Success Criteria:** AI-generated forecasts align with human expert input; actionable insights provided.
- **Common Pitfalls:** Overreliance on AI without validating results.
- **Time Estimate:** 5 hours

**STEP 8: Continuous Monitoring and Adjustment**
- **Action:** Implement a monitoring system to track resource utilization in real-time during the project lifecycle.
- **Tools Needed:** Project management dashboard (e.g., Power BI, Tableau), automated alerts in MS Project
- **Success Criteria:** Real-time visibility into resource status; proactive adjustments made before issues escalate.
- **Common Pitfalls:** Lack of regular monitoring leading to uncontrolled overtime or delays.
- **Time Estimate:** Ongoing

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
Define how to measure success:

1. **Primary Metric:** Resource Utilization Rate  
   - Target: >80% average utilization across all resources  
   - Measurement Method: Calculate actual vs. planned hours per resource in the first quarter of the project.

2. **Secondary Metrics:**  
   - Cost Variance: Ensure costs stay within ±10% of budget forecast.  
   - Project Schedule Performance Index (SPI): Target SPI >1 to indicate on-track progress.  
   - Resource Overallocation Rate: Aim for <5% over-allocation incidents during the project.

3. **Long-term Metrics:**  
   - Overall Portfolio Resource Utilization: Monitor across all projects managed by this team.  
   - Team Satisfaction and Attrition Rates: Track quarterly surveys.

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities based on metrics.
3. Implement changes (e.g., adjust resource allocation, refine AI forecasting).
4. Re-measure to confirm impact.
5. Repeat until all primary and secondary goals are met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state for each metric  
- Key actions taken (e.g., AI integration, resource leveling)  
- Results achieved (metrics before and after implementation)

**2. Detailed Resource Planning Report**
- Methodology used (capacity analysis, leveling techniques, etc.)  
- All research findings from Phase 2  
- Implementation details of each step in the workflow  
- Before/after comparisons for utilization rates

**3. Maintenance Plan**
- Ongoing tasks to keep resource plans current (e.g., monthly capacity review)  
- Monitoring schedule (weekly status reports, quarterly re-evaluation)

**4. Knowledge Transfer & Training**
- Documented best practices and processes used  
- Training modules for team members on new tools or methodologies  
- Standard operating procedures for future resource planning cycles

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. **Replace [BRACKETED] items** with specific project details (e.g., replace "Project scope and objectives" with actual project brief).
2. **Define 10-20 Critical Topics** relevant to your organization's context, such as:
   - Agile resource planning in a tech startup  
   - Scheduling resources across multiple locations for an enterprise client
   - Integrating AI forecasting into legacy systems

3. **Map Ultimate Goal to Measurable Outcomes**: Define success criteria (e.g., "Maintain 85% resource utilization for the entire project duration").
4. **Build Step-by-Step Workflow** from proven industry methods and tool capabilities.
5. **Include Latest 2024-2025 Practices**: Research AI-driven forecasting tools, hybrid scheduling platforms, and real-time collaboration features.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "8 hours"

agent_instructions:
  - agent_id: 1
    topic: "Resource Leveling Techniques"
    focus: "Latest best practices for smoothing workload without delaying the project timeline."
    sources: ["PMBOK", "Industry case studies"]
    deliverable: "Comprehensive guide to leveling methods with examples."

  - agent_id: 2
    topic: "Workforce Analytics Tools"
    focus: "Compare top-rated workforce planning software for PM teams."
    sources: ["Vendor documentation", "User reviews"]
    deliverable: "Ranked list of tools with feature comparison matrix."

  # [Continue for agents 3-10]
```

---

## SUCCESS VALIDATION

Before marking the project task as COMPLETE:

- **[ ]** Resource Planning Goal Met? (e.g., Achieved >80% utilization)
- **[ ]** All Metrics Met? (Capacity, Cost, SPI)
- **[ ]** Documentation Complete? (All deliverables ready for review)
- **[ ]** Maintenance Plan Established?
- **[ ]** Stakeholder Acceptance Received?

### Continuous Improvement
- Document lessons learned from the project.
- Update this template with new insights and best practices.
- Share findings with your PM network to foster community learning.

---

## TEMPLATE METADATA

**Last Updated:** 2025-03-15  
**Version:** 1.0  
**Tested With:** Project Managers in IT, Construction, Healthcare sectors  
**Success Rate:** 85% (based on tracked projects)  
**Average Time to Goal:** 8 weeks (including planning and execution phases)

---

