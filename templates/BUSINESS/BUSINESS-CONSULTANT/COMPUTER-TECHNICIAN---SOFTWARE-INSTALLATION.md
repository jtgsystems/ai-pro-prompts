# Computer Technician - AI Agent Template
## Software Installation

**Version:** 1.0  
**Purpose:** Guide an AI agent through industry best practices to achieve a professional Computer Technician's ultimate goal of successfully installing software on client systems.

---

### PROFESSION CONFIGURATION
```yaml
profession_name: "Computer Technician"
profession_category: "Technology"
experience_level: "[Beginner/Intermediate]"
```

### Ultimate Goal
**Primary Objective:** Successfully install [SPECIFIC SOFTWARE NAME] on a remote client system within 2 business days, achieving 100% successful installation with no post-installation errors.

---

## PHASE 1: INFORMATION GATHERING

### Required Inputs
```yaml
- target_system_details:
    - OS_version: "Windows 10 Pro"
    - Processor: "Intel Core i5-10600K"
    - RAM: "16GB DDR4"
    - Disk_space: "500GB NVMe SSD"
    - Current_software_list:
        - Operating System: "Windows 10 Pro"
        - Antivirus: "Bitdefender Total Security"
        - VPN: "ExpressVPN client"
- software_requirements:
    - Software_name: "[SPECIFIC SOFTWARE NAME]"
    - Version: "[VERSION NUMBER]"
    - Compatibility: [Windows 10, 64-bit]
- user_access_details:
    - User_role: "End-user"
    - Access_level: "Standard user"
- installation_constraints:
    - Time_frame: "2 business days"
    - Network_conditions: "Fiber-optic, >100Mbps upload/download"
    - Security_requirements: [No firewall exceptions needed]
```

### Initial Assessment Checklist
- [ ] Verify all required inputs received and validated.
- [ ] Confirm target system specifications are compatible with the software.
- [ ] Validate user access permissions allow installation.
- [ ] Establish baseline metrics (current system state, installed programs).

---

## PHASE 2: RESEARCH & ANALYSIS

### Critical Knowledge Areas
**Research Agent Deployment:** Launch 10 parallel sub-agents to research latest practices.

**Topic 1:** Software Installation Best Practices  
**Action Research Focus:** Latest best practices for installing software on Windows systems in 2024-2025.  
**Target Sources:** PCMag, TechRadar, Reddit r/Windows10 community forums, vendor documentation.  
**Deliverable:** 3-5 actionable insights with source citations.

**Topic 2:** Prerequisite Checks  
**Action Research Focus:** Steps to ensure system is ready for installation (updates, security checks).  
**Target Sources:** Sysinternals tools list, official software release notes.  
**Deliverable:** Checklist of prerequisite tasks.

**Topic 3:** Troubleshooting Guides  
**Action Research Focus:** Common issues during Windows software installations and resolution steps.  
**Target Sources:** SuperUser StackExchange, vendor support articles.  
**Deliverable:** Troubleshooting guide document.

**Topic 4-10:** [Define based on profession]
- Software Deployment Tools (e.g., SCCM)
- Remote Access Protocols (e.g., TeamViewer)
- Security Best Practices
- Automation with PowerShell Scripts
- Network Considerations

### Research Consolidation
After all sub-agents complete:
1. Synthesize findings into unified strategy.
2. Identify conflicts or contradictions in best practices.
3. Prioritize recommendations by impact on the installation process.
4. Create master action plan.

---

## PHASE 3: EXECUTION WORKFLOW

### Step-by-Step Process
**STEP 1: System Preparation**
- **Action:** Run Windows Update, install latest security patches.  
- **Tools Needed:** `powershell -command "Get-WindowsUpdate"`  
- **Success Criteria:** No pending updates; system rebooted without errors.  
- **Common Pitfalls:** Ignored critical update notifications.  
- **Time Estimate:** 30 minutes

**STEP 2: Backup Essential Data**
- **Action:** Perform a full backup of user data using built-in Windows Backup utility or third-party tool like EaseUS Todo Backup.  
- **Tools Needed:** `Windows Backup`, `EaseUS Todo Backup` (free)  
- **Success Criteria:** Successful creation of full system and files restore points.  
- **Common Pitfalls:** Overwriting existing backups without confirmation.  
- **Time Estimate:** 45 minutes

**STEP 3: Download Software Installer**
- **Action:** Download the latest installer from vendor website, ensuring it matches OS version.  
- **Tools Needed:** Browser (Chrome/Firefox), `wget` for CLI download (optional).  
- **Success Criteria:** Installer file size and checksum match vendor's published values.  
- **Common Pitfalls:** Using incorrect OS architecture or mismatched version.  
- **Time Estimate:** 15 minutes

**STEP 4: Execute Installation**
- **Action:** Run the installer with administrative privileges, following on-screen prompts.  
- **Tools Needed:** `Run as Administrator` (built-in Windows), optional PowerShell for silent install (`[SOFTWARE_INSTALLER].exe /s`).  
- **Success Criteria:** Installer completes without errors; software appears in system list post-installation.  
- **Common Pitfalls:** Non-administrative user rights or interrupted download.  
- **Time Estimate:** 1 hour

**STEP 5: Configure Software Settings**
- **Action:** Launch installed software, configure default settings (privacy, notifications).  
- **Tools Needed:** Installed [SPECIFIC SOFTWARE NAME].  
- **Success Criteria:** All required configuration options applied without prompts.  
- **Common Pitfalls:** Default configurations incompatible with business requirements.  
- **Time Estimate:** 30 minutes

**STEP 6: Post-Installation Verification**
- **Action:** Verify software is functioning correctly, no errors in logs, and performs expected tasks.  
- **Tools Needed:** Software application itself for testing, `Event Viewer` for log checks.  
- **Success Criteria:** No operational issues; user can complete typical workflows.  
- **Common Pitfalls:** Ignored initial error messages or failed test operations.  
- **Time Estimate:** 45 minutes

**STEP 7: Clean Up Temporary Files**
- **Action:** Remove installer files, empty Recycle Bin to reclaim disk space.  
- **Tools Needed:** `del` command in PowerShell, `CleanMyMac` (optional).  
- **Success Criteria:** Installer files deleted; system clean and stable.  
- **Common Pitfalls:** Leaving installer files behind causing future issues.  
- **Time Estimate:** 15 minutes

**STEP 8: Security Hardening**
- **Action:** Review and apply security settings, ensure no unnecessary services or ports are exposed.  
- **Tools Needed:** `Task Manager`, `Process Explorer` (for process review).  
- **Success Criteria:** No vulnerable services running; system firewall rules intact.  
- **Common Pitfalls:** Leaving debugging tools enabled that could expose the network.  
- **Time Estimate:** 30 minutes

**STEP 9: Document Installation**
- **Action:** Create detailed documentation including steps taken, software version installed, and any configuration notes.  
- **Tools Needed:** `Word` (or Markdown for remote docs), `OneNote`.  
- **Success Criteria:** Comprehensive installation record available to client support team.  
- **Common Pitfalls:** Incomplete or inaccurate records leading to future troubleshooting.  
- **Time Estimate:** 45 minutes

**STEP 10: Client Communication**
- **Action:** Inform the user of successful installation, provide basic usage instructions, and schedule next steps for training if needed.  
- **Tools Needed:** Email (Gmail/Outlook), in-person meeting (if remote access allowed).  
- **Success Criteria:** User acknowledges understanding; no follow-up issues reported within 24 hours.  
- **Common Pitfalls:** Failing to provide clear instructions or documentation leading to user confusion.  
- **Time Estimate:** 30 minutes

### Quality Checkpoints
1. **Checkpoint 1:** After Step 2 - Verify backup completed successfully.
2. **Checkpoint 2:** After Step 4 - Confirm installer checksum matches vendor's values.
3. **Checkpoint 3:** After Step 6 - Validate software functions as expected with critical user workflows.

---

## PHASE 4: OPTIMIZATION & REFINEMENT

### Performance Metrics
1. **Primary Metric:** Successful Installation Rate  
   - Target: 100% success for first attempt or within two attempts.  
   - Measurement Method: Track installation logs and confirm software functionality in the dashboard.

2. **Secondary Metrics:**  
   - Time to Complete Full Process (hours)  
   - Number of Failed Attempts / Errors Encountered  
   - User Satisfaction Rating Post-Installation  

3. **Long-term Metrics:**  
   - Ongoing Maintenance Required (e.g., updates, reconfigurations)  
   - System Performance Impact (CPU/Memory usage)

### Iterative Improvement Loop
1. Measure current performance against targets.
2. Identify top 3 improvement opportunities based on metrics.
3. Implement changes (e.g., automation scripts).
4. Re-measure results and adjust until all goals met.

---

## PHASE 5: REPORTING & DOCUMENTATION

### Deliverables
**1. Executive Summary**
- Current state vs. target state  
- Key actions taken (installation steps, issues resolved)  
- Results achieved (software functional, user satisfied)

**2. Detailed Report**
- Complete methodology documentation  
- All research findings and recommendations  
- Step-by-step execution details with screenshots/logs  

**3. Maintenance Plan**
- Ongoing tasks to maintain software health (patches, updates)  
- Monitoring schedule (daily/weekly checks via Event Viewer)  
- Update frequency for future installations or upgrades  

**4. Knowledge Transfer**
- Training materials: Short video walkthroughs of installed application  
- SOPs: Steps to reinstall in case of failure  
- Troubleshooting guide: Common issues and resolutions  

---

## PROFESSION-SPECIFIC CUSTOMIZATION GUIDE

### How to Adapt This Template
1. **Replace All [BRACKETED] Inputs** with actual client system specs.
2. **Define 10-20 Critical Topics** based on:
   - Latest software release notes
   - Industry-specific security standards (e.g., HIPAA, GDPR)
   - Remote work considerations for installation protocols
3. **Map Ultimate Goal to Measurable Outcomes**
   - Use SMART criteria: Specific, Measurable, Achievable, Relevant, Time-bound.
   - Define clear success metrics: 100% successful install, no post-install errors.

4. **Build Step-by-Step Workflow** from:
   - Vendor's official installation guide
   - Industry best practices for remote system administration
   - Tool documentation (e.g., SCCM, SysInternals)

5. **Include Latest 2024-2025 Practices**
   - Use of AI-driven patch management tools like Ivanti Neurons.
   - Automation with PowerShell Desired State Configuration.
   - Cloud-based deployment solutions.

---

## RESEARCH SUB-AGENT CONFIGURATION

```yaml
research_mission:
  total_agents: 10
  parallel_execution: true
  time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Software Installation Best Practices"
    focus: "Latest 2024-2025 practices for Windows software installs"
    sources: ["PCMag", "TechRadar", "Reddit r/Windows10"]
    deliverable: "Actionable insights with URLs"

  - agent_id: 2
    topic: "Prerequisite Checks for Install"
    focus: "Identify necessary system conditions before install"
    sources: ["Sysinternals", "Vendor documentation"]
    deliverable: "Pre-install checklist document"

  # [Continue defining agents 3-10]
```

---

## SUCCESS VALIDATION

### Final Checklist
- [ ] **Installation Completed:** Software fully installed and operational.  
- [ ] **No Errors Post-Install:** No error logs or issues reported by user.  
- [ ] **System Stability:** No new vulnerabilities exposed; system performs normally.  
- [ ] **Documentation Complete:** All steps, decisions, and results documented in client portal.  
- [ ] **User Satisfied:** Positive feedback from end-user on installation experience.

### Continuous Improvement
- Document lessons learned during the process.
- Update SOPs with any changes discovered during execution.
- Share best practices with team through internal wiki or Slack channel.
- Schedule a follow-up review within 30 days to ensure long-term stability.

---

## TEMPLATE METADATA

**Last Updated:** [2025-06-20]  
**Version:** 1.0  
**Tested With:** Windows Technician, Software Installer roles  
**Success Rate:** N/A (initial)  
**Average Time to Goal:** 2 business days

---

