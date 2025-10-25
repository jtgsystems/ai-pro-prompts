# Network Administrator - AI Agent Template
## Documentation

### Success Definition (Measurable)

**Ultimate Goal:** Achieve 100% completeness and accuracy in network documentation across all systems, configurations, and procedures within a quarter.

- **Primary Metric:** All critical components of the network have been documented with no missing entries.
- **Timeframe for Achievement:** Within 90 days from project start.
- **Quality Assurance:** Documentation reviewed and approved by at least two senior network administrators.
- **Accessibility Criteria:** All documentation accessible via secure, shared repository within the corporate network.

### Critical Knowledge Areas (10-20 Topics)

1. **Network Topology & Architecture**  
   - Research Focus: Current physical and logical layout of the network including VLANs, subnetting, and routing tables.  
   - Target Sources: Network diagrams from ITSM tools like ServiceNow, Cisco Prime.

2. **Device Configuration Standards**  
   - Research Focus: Standard configurations for routers, switches, firewalls, and load balancers.  
   - Target Sources: Manufacturer documentation, internal configuration templates.

3. **Change Management Process**  
   - Research Focus: Procedures for documenting changes to network infrastructure including approvals and rollback strategies.  
   - Target Sources: ITIL framework documents, internal SOPs.

4. **Security Protocols & Policies**  
   - Research Focus: Current security measures such as firewall rules, intrusion detection systems (IDS), and access control policies.  
   - Target Sources: Security policy documents, network scanning reports from tools like OpenVAS or Nessus.

5. **Backup & Recovery Procedures**  
   - Research Focus: How data is backed up, where backups are stored, and the recovery process for various types of incidents.  
   - Target Sources: Backup software documentation (e.g., Veeam, Commvault), disaster recovery plans.

6. **Monitoring & Alerting Systems**  
   - Research Focus: Tools used for monitoring network performance and health such as Nagios, Zabbix, or SolarWinds.  
   - Target Sources: Vendor documentation, internal monitoring reports.

7. **Service Level Agreements (SLAs)**  
   - Research Focus: Defined SLAs for uptime, response times, and service availability across different services.  
   - Target Sources: Service level agreement documents within ITSM systems.

8. **Vendor Management & Contractual Obligations**  
   - Research Focus: Key dates for renewals, support contracts, and any technical constraints from vendors.  
   - Target Sources: Vendor portals, contract management systems (e.g., SAP Business Network).

9. **Disaster Recovery Planning**  
   - Research Focus: Strategies for recovering critical network functions in the event of a disaster.  
   - Target Sources: DR plans, business continuity planning documents.

10. **Compliance Requirements**  
    - Research Focus: Regulatory requirements such as GDPR, HIPAA, or industry-specific standards impacting documentation and security practices.  
    - Target Sources: Compliance frameworks, legal databases.

11. **Incident Management Process**  
    - Research Focus: Steps to document incidents including initial reports, investigations, resolutions, and post-mortem analyses.  
    - Target Sources: Incident management SOPs, ticketing system logs (e.g., JIRA).

12. **Network Segmentation & Security Zones**  
    - Research Focus: How the network is divided into segments for security purposes and what access controls are in place between them.  
    - Target Sources: Network segmentation diagrams, ACL configurations.

13. **User Account Management**  
    - Research Focus: How user accounts are created, modified, and deleted across the network including any automated tools used.  
    - Target Sources: Active Directory documentation, account management policies.

14. **Documentation Standards & Formats**  
    - Research Focus: Preferred formats (e.g., Markdown, Word) and styles for documenting various aspects of the network.  
    - Target Sources: Style guides within the organization, industry best practices.

15. **Automation Tools Integration**  
    - Research Focus: How automation tools like Ansible or Puppet are used to manage configurations across devices.  
    - Target Sources: Automation scripts repositories, configuration management documentation.

16. **Capacity Planning & Forecasting**  
    - Research Focus: Methods and tools used for planning future network capacity based on growth projections.  
    - Target Sources: Capacity planning reports, usage analytics dashboards.

17. **Vendor Technical Support Processes**  
    - Research Focus: How technical support from vendors is documented including escalation paths and response procedures.  
    - Target Sources: Vendor documentation portals, internal support SOPs.

18. **Documentation Review & Revision Process**  
    - Research Focus: How often documentation is reviewed for accuracy and completeness, who is responsible, and how updates are tracked.  
    - Target Sources: Documentation governance policies, version control systems (e.g., GitLab).

19. **Network Architecture Evolution**  
    - Research Focus: Any recent changes or planned upgrades to the network architecture such as cloud migration or SDN implementations.  
    - Target Sources: Project plans, architectural review boards.

20. **Incident Response Drills & Exercises**  
    - Research Focus: How frequently and what types of drills are conducted to test incident response procedures.  
    - Target Sources: Training records, exercise logs.

### Execution Steps with Specific Actions

#### Step 1: Inventory Collection
- **Action:** Run a comprehensive scan using tools like Nmap or OpenVAS to identify all devices on the network.
- **Tools Needed:** Nmap, OpenVAS, Cisco Prime, ServiceNow ITSM.
- **Success Criteria:** All active and inactive devices are listed in a spreadsheet with IP addresses, MAC addresses, and device types.

#### Step 2: Documentation of Network Topology
- **Action:** Create diagrams showing physical and logical network topology using tools like Lucidchart or Draw.io.
- **Tools Needed:** Lucidchart (free), Draw.io (free).
- **Success Criteria:** All networks are visualized with accurate connections between devices.

#### Step 3: Configuration Documentation
- **Action:** Export configuration settings from routers, switches, and firewalls into a standardized format.
- **Tools Needed:** Cisco IOS CLI tools, Linux command line for scripting, Ansible playbooks (optional).
- **Success Criteria:** All configurations are documented with clear versions and timestamps.

#### Step 4: Security Policy Documentation
- **Action:** Compile all security policies including firewall rules, IDS signatures, and access control lists.
- **Tools Needed:** Firewall management consoles, IDS configuration tools.
- **Success Criteria:** No security vulnerabilities identified in the documentation review process.

#### Step 5: Change Management Workflow
- **Action:** Document the change management workflow from proposal to implementation and post-mortem analysis.
- **Tools Needed:** JIRA for tracking changes, Confluence for collaborative editing.
- **Success Criteria:** All changes are tracked with approval signatures and rollback procedures defined.

#### Step 6: Backup Procedures Documentation
- **Action:** List all backup locations, schedules, and restore procedures.
- **Tools Needed:** Backup software dashboards (e.g., Veeam UI), ticketing system logs.
- **Success Criteria:** Restores from backups are successful without data loss.

#### Step 7: Review & Approve Documentation
- **Action:** Have senior network administrators review all documentation for completeness and accuracy.
- **Tools Needed:** Confluence, Teams meetings.
- **Success Criteria:** All documents receive at least two approvals and no critical feedback remains unresolved.

#### Step 8: Version Control Setup
- **Action:** Implement version control using tools like GitLab or Bitbucket to track changes in documentation over time.
- **Tools Needed:** GitLab (free), Bitbucket (free).
- **Success Criteria:** All versions of documents are tracked with clear change logs and revert points.

#### Step 9: Training & Knowledge Transfer
- **Action:** Conduct training sessions for new network administrators on how to maintain documentation.
- **Tools Needed:** Teams, PowerPoint presentations, Confluence pages for handouts.
- **Success Criteria:** Trainees can independently update or modify documentation based on updates in the network.

#### Step 10: Establish Maintenance Schedule
- **Action:** Set a quarterly review schedule for all documentation to ensure it remains up-to-date and relevant.
- **Tools Needed:** Calendar invites, Teams reminders.
- **Success Criteria:** Quarterly reviews are scheduled and documented with action items assigned.

### Troubleshooting Common Issues

**Issue 1: Incomplete Device Scans**
- **Cause:** Network devices not responding or firewall rules blocking scans.
- **Solution:** Use Nmap scripts designed for stealth scanning (e.g., `-sS -O`) and ensure network access to all VLANs.

**Issue 2: Version Control Conflicts**
- **Cause:** Multiple users editing the same document leading to conflicts.
- **Solution:** Implement a clear workflow where only one user edits at a time or use Git's merge conflict resolution features.

**Issue 3: Documentation Not Accessible**
- **Cause:** Files stored on personal drives inaccessible from corporate network.
- **Solution:** Ensure all files are stored in the corporate shared drive (e.g., SharePoint, Teams) with appropriate permissions.

**Issue 4: Security Policy Gaps**
- **Cause:** Changes made without updating security policies or procedures.
- **Solution:** Integrate change management process to automatically trigger policy updates during documentation review.

### Recommended Tool Stack

#### Primary Tools (Free/Open Source)

1. **Nmap** - Network scanning and discovery tool
2. **OpenVAS** - Vulnerability scanner for identifying potential threats
3. **Lucidchart** - Free network diagramming tool with collaboration features
4. **Draw.io** - Free online drawing tool for diagrams
5. **GitLab** - Version control system for tracking documentation changes
6. **Confluence** - Collaborative wiki platform for storing and sharing documents
7. **JIRA** - Issue tracking software to manage tasks and approvals
8. **Teams/Slack** - Communication tools for team collaboration

#### Alternative Tools (Paid/Premium)

1. **Cisco Prime Infrastructure** - Centralized management tool for Cisco devices
2. **Veeam Backup & Recovery** - Enterprise backup solution with advanced features
3. **SolarWinds Network Performance Monitor** - Comprehensive monitoring suite
4. **Ansible Automation Platform** - For automating configuration across multiple systems

### Timeline and Success Criteria

- **Month 1:** Inventory Collection, Initial Diagrams, Basic Configuration Documentation (30% completion)
- **Month 2:** Detailed Topology Mapping, Security Policy Documenting, Change Management Workflow Setup (60% completion)
- **Month 3:** Backup Procedures Documented, Documentation Review Process in Place, Version Control Established (80% completion)
- **Month 4:** Training Sessions Conducted, Maintenance Schedule Set, Final Reviews Completed (100% completion)

**Success Criteria:**
- Complete documentation of all network components.
- All critical documents reviewed and approved by senior administrators within the stipulated timeline.
- No significant gaps identified in security policies or change management processes during internal audits.

By following this detailed template with specific actions tailored for Network Administrators, you can achieve comprehensive and accurate network documentation that meets industry best practices.

