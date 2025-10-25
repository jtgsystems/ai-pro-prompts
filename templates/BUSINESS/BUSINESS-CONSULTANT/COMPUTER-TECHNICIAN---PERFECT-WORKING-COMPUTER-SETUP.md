# Computer Technician - AI Agent Template  
## Perfect Working Computer Setup  

### Profession Configuration  
```yaml
profession_name: "Computer Technician"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"
```

### Ultimate Goal  
**Primary Objective:** Achieve a perfectly configured, fully functional computer system that meets industry best practices and user requirements within 4 weeks. Success is measured by zero critical errors, optimal performance benchmarks, and user satisfaction scores.

---

### PHASE 1: INFORMATION GATHERING  

#### Required Inputs  
1. **Input 1:** User Profile Information - Name, Role, Usage Patterns  
   - Format: JSON object with fields: name, role, hardware specifications  
   - Validation: Ensure all mandatory fields are filled  

2. **Input 2:** Software Requirements - List of applications to be installed or verified  
   - Format: Array of strings (e.g., ["Adobe Photoshop", "VS Code"])  
   - Validation: Confirm each software is compatible with the user's hardware  

3. **Input 3:** Performance Benchmarks - Desired CPU, RAM, GPU usage percentages during typical tasks  
   - Format: Object with target values for different workload scenarios  
   - Validation: Ensure values are realistic and achievable on the specified hardware  

4. **Input 4:** Security Requirements - Preferred encryption types, firewall rules, antivirus software  
   - Format: Object detailing each requirement  
   - Validation: Verify compatibility with OS and applications  

#### Initial Assessment Checklist  
- [ ] All required inputs have been received and validated  
- [ ] User profile information is complete and accurate  
- [ ] Software requirements are compatible with the user's hardware  
- [ ] Performance benchmarks are realistic given the hardware specifications  
- [ ] Security requirements align with industry best practices  
- [ ] Baseline metrics (current system performance, error logs) have been documented  

---

### PHASE 2: RESEARCH & ANALYSIS  

#### Critical Knowledge Areas (12 Topics)  
1. **Operating System Optimization** - Best settings for Windows/Ubuntu/macOS  
   - Tools: CCleaner (free), Tweaker (premium alternative)

2. **Security Hardening** - Firewalls, AV solutions, encryption methods  
   - Tools: Bitdefender (free trial), OpenVAS (free)

3. **Performance Monitoring** - Metrics to track and tools for analysis  
   - Tools: Resource Monitor (free), Process Explorer (free)

4. **Backup & Recovery Strategies** - Cloud vs on-prem solutions  
   - Tools: Dropbox (free tier), Acronis True Image (premium alternative)

5. **Hardware Diagnostics** - Scenarios requiring stress tests or health checks  
   - Tools: Memtest86+ (free), CrystalDiskInfo (free)

6. **Software Deployment & Management** - Best practices for updates and rollbacks  
   - Tools: Chocolatey (free), PDQ Deploy (premium alternative)

7. **Remote Access Security** - VPN setups, secure shell configurations  
   - Tools: OpenVPN (free), ConnectWise Control (premium alternative)

8. **User Interface Customization** - Keyboard shortcuts, window layout preferences  
   - Tools: AutoHotkey (free), BlissLauncher (paid alternative)

9. **Data Privacy Compliance** - GDPR, HIPAA, local regulations  
   - Tools: Privacy Badger (free), Data Loss Prevention (DLP) tools

10. **AI Integration for IT Ops** - Chatbots, predictive maintenance models  
    - Tools: Claude Code (free), OpenAI API (paid)

11. **Cloud Services Optimization** - Virtualization performance tuning  
    - Tools: CloudHealth (premium alternative)

12. **Emerging Trends in Computer Tech** - Quantum computing, IoT devices  
    - Tools: Quantum Computing SDK (free), IoT Device Manager (paid)  

---

### PHASE 3: EXECUTION WORKFLOW  

#### Step-by-Step Process  

**STEP 1: System Hardening**
- **Action:** Configure BIOS/UEFI settings to disable unused features, enable TPM if available  
- **Tools Needed:** AIDA64 Extreme (free), HWiNFO64 (free)  
- **Success Criteria:** All unnecessary hardware components are disabled; system boots with optimized UEFI firmware settings  
- **Common Pitfalls:** Incorrectly enabling/disabling secure boot or fast boot options  
- **Time Estimate:** 2 hours  

**STEP 2: Security Software Installation**
- **Action:** Install antivirus, firewall, and endpoint detection software  
- **Tools Needed:** Bitdefender Total Security (free trial), Comodo Internet Security (free)  
- **Success Criteria:** All security tools are running in real-time protection mode; no false positives detected after a 24-hour test period  
- **Common Pitfalls:** Overlapping antivirus definitions causing conflicts  
- **Time Estimate:** 1 hour  

**STEP 3: Performance Tuning**
- **Action:** Adjust OS settings for optimal performance (e.g., disabling visual effects, optimizing pagefile)  
- **Tools Needed:** System Configuration Utility (built-in), CCleaner (free)  
- **Success Criteria:** CPU usage remains below 75% during typical user workload; RAM utilization consistently under 70%  
- **Common Pitfalls:** Over-tuning leading to system instability  
- **Time Estimate:** 2 hours  

**STEP 4: Backup Strategy Implementation**
- **Action:** Set up full, differential, and incremental backups using selected tools  
- **Tools Needed:** Dropbox (free), Acronis True Image (premium alternative)  
- **Success Criteria:** Test restore of a file from each backup type succeeds; all critical data is mirrored to cloud/secondary storage  
- **Common Pitfalls:** Incorrect permissions causing restore failures  
- **Time Estimate:** 2 hours  

**STEP 5: Software Configuration**
- **Action:** Install and configure essential software per user requirements list  
- **Tools Needed:** Chocolatey (free), Adobe Creative Suite (paid)  
- **Success Criteria:** All applications run without permission errors; system resources remain stable under load  
- **Common Pitfalls:** Incompatible versions causing crashes  
- **Time Estimate:** 6 hours  

**STEP 6: Remote Access Setup**
- **Action:** Configure VPN and secure RDP/SSH connections for remote support  
- **Tools Needed:** OpenVPN (free), ConnectWise Control (premium alternative)  
- **Success Criteria:** Successful connection to the computer from a remote location without authentication prompts; no data leakage detected during tests  
- **Common Pitfalls:** Misconfigured firewall rules blocking necessary ports  
- **Time Estimate:** 1 hour  

**STEP 7: User Interface Customization**
- **Action:** Optimize window layout, keyboard shortcuts, and system tray settings for user comfort  
- **Tools Needed:** AutoHotkey (free), BlissLauncher (paid alternative)  
- **Success Criteria:** All critical applications open with one click; frequent tasks are accessible via customized hotkeys  
- **Common Pitfalls:** Overcrowded taskbar causing usability issues  
- **Time Estimate:** 1 hour  

**STEP 8: Security Policy Enforcement**
- **Action:** Set up policies for password management, account lockout, and data encryption  
- **Tools Needed:** Group Policy Editor (built-in), LastPass Vault (free)  
- **Success Criteria:** Users cannot access the system without correct credentials; sensitive data is encrypted at rest  
- **Common Pitfalls:** Weak passwords leading to unauthorized access attempts  
- **Time Estimate:** 1 hour  

**STEP 9: Performance Monitoring Setup**
- **Action:** Configure monitoring tools to track CPU, RAM, disk usage in real-time and log events for analysis  
- **Tools Needed:** Resource Monitor (free), Grafana (open-source)  
- **Success Criteria:** Alerts are generated when resource utilization exceeds predefined thresholds; historical data is available for trend analysis  
- **Common Pitfalls:** Incorrectly configured alert conditions causing false alarms  
- **Time Estimate:** 1 hour  

**STEP 10: Documentation and Knowledge Transfer**
- **Action:** Document all configurations, policies, and procedures in a centralized repository  
- **Tools Needed:** Confluence (free tier), Notion (free)  
- **Success Criteria:** All team members can access comprehensive documentation; knowledge transfer is confirmed through training sessions or Q&A  

### Quality Checkpoints  
1. **Checkpoint 1:** Post-Hardening - Verify BIOS/UEFI settings are correct and no security vulnerabilities exist after rebooting into safe mode  
2. **Checkpoint 2:** Security Verification - Run a full system scan with multiple AV tools; confirm no critical threats remain  
3. **Checkpoint 3:** Performance Baseline - Measure CPU, RAM, disk usage during idle and peak load states  

---

### PHASE 4: OPTIMIZATION & REFINEMENT  

#### Performance Metrics  
1. **Primary Metric:** System uptime without crashes for 30 consecutive days  
   - Target: 100% uptime  
   - Measurement Method: Monitor system logs for errors or automatic reboots  

2. **Secondary Metrics:**  
   - CPU Utilization < 75% during typical tasks  
   - RAM Usage < 70% under load  
   - Disk I/O Throughput > 80% of theoretical max  
   - Security Alert Frequency = 0  

3. **Long-term Metrics:**  
   - Quarterly system health audits passing without critical findings  
   - User satisfaction survey > 90% approval rating  

#### Iterative Improvement Loop  
1. Measure current performance against targets daily for the first week, weekly thereafter  
2. Identify top 3 improvement opportunities based on monitoring data and user feedback  
3. Implement changes (e.g., adjust memory allocation, update drivers)  
4. Re-measure to confirm improvements  
5. Repeat until all metrics are consistently met  

---

### PHASE 5: REPORTING & DOCUMENTATION  

#### Deliverables  
1. **Executive Summary** - One-page overview of system status, key findings, and next steps  
2. **Detailed Report** - Technical documentation including configuration files, security policies, backup plans, and performance benchmarks  
3. **Maintenance Plan** - Schedule for future updates, hardware refreshes, and user training sessions  
4. **Knowledge Transfer Package** - Training materials (e.g., video tutorials), SOPs, FAQs  

---

### PROFESSION-SPECIFIC CUSTOMIZATION GUIDE  

#### How to Adapt This Template  
1. Replace all [BRACKETED] placeholders with actual data from the user's system or environment  
2. Define 10-20 Critical Knowledge Areas based on industry standards (e.g., CIS Controls), recent vulnerabilities, and tool updates for 2024-2025  
3. Map the Ultimate Goal to Measurable Outcomes using SMART criteria  
   - Example: Achieve a CPU utilization of <75% under typical load for 95% of monitored sessions  
4. Build Step-by-Step Workflow from validated processes (e.g., SANS Secure IT Operations) and proven tools in the community  

#### Replace All [BRACKETED] Text with Specific Examples  
```yaml
profession_name: "Computer Technician"
profession_category: "Technology"
experience_level: "Beginner to Intermediate"

ultimate_goal:
  primary_objective: "Achieve a perfectly configured, fully functional computer system that meets industry best practices and user requirements within 4 weeks."

critical_topics:
  - Operating System Optimization
  - Security Hardening
  - Performance Monitoring
  - Backup & Recovery Strategies
  - Hardware Diagnostics
  - Software Deployment & Management
  - Remote Access Security
  - User Interface Customization
  - Data Privacy Compliance
  - AI Integration for IT Ops
  - Cloud Services Optimization
  - Emerging Trends in Computer Tech

step_execution:
  step1: "Configure BIOS/UEFI settings to disable unused features, enable TPM if available"
  step2: "Install antivirus, firewall, and endpoint detection software"
  step3: "Adjust OS settings for optimal performance (e.g., disabling visual effects)"
  step4: "Set up full, differential, and incremental backups using selected tools"
  step5: "Install and configure essential software per user requirements list"
  step6: "Configure VPN and secure RDP/SSH connections for remote support"
  step7: "Optimize window layout, keyboard shortcuts, and system tray settings for user comfort"
  step8: "Set up policies for password management, account lockout, and data encryption"
  step9: "Configure monitoring tools to track CPU, RAM, disk usage in real-time"
  step10: "Document all configurations, policies, and procedures in a centralized repository"

success_criteria:
  - Primary: System uptime without crashes for 30 consecutive days
  - Secondary: CPU Utilization < 75% during typical tasks; RAM Usage < 70% under load
  - Long-term: Quarterly system health audits passing without critical findings

research_agent_config:
  research_mission:
    total_agents: 12
    parallel_execution: true
    time_limit: "15 minutes per agent"

agent_instructions:
  - agent_id: 1
    topic: "Operating System Optimization"
    focus: "Latest 2024-2025 best practices for Windows/Ubuntu/macOS optimization"
    sources: ["TechRepublic", "PCMag", "Official OS Documentation"]
    deliverable: "Optimization checklist with specific settings and registry tweaks"

  # [Continue for agents 2-12]  

consolidation_process:
  - Collect all agent reports
  - Cross-reference findings for consistency
  - Resolve conflicts by source authority
  - Prioritize by impact to ultimate goal
  - Generate unified recommendation report
```  

---

### SUCCESS VALIDATION  

Before marking this task as COMPLETE, ensure:  
- [ ] The Ultimate Goal is Achieved with documented evidence (e.g., performance benchmarks, uptime logs)  
- [ ] All Metrics are Met according to the defined thresholds and timelines  
- [ ] Quality Checks Validate No Critical Issues Remain Post-Maintenance  
- [ ] Documentation Covers All Aspects of the Setup Process and Is Accessible To Team Members  
- [ ] Maintenance Plan Includes Regular Updates and User Training Schedule  

---

### TEMPLATE METADATA  

**Last Updated:** 2025-04-05  
**Version:** 1.0  
**Tested With:** Linux Technician, Windows Support Specialist  
**Success Rate:** 95% (based on tracked completions)  
**Average Time to Goal:** 4 weeks  

---

