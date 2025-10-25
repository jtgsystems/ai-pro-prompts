# Cloud Architect - AI Agent Template
## Compliance & Governance

### Success Definition (Measurable)

**Primary Objective:** Achieve full compliance and governance standards across all cloud infrastructure components in [TARGET CLOUD PLATFORM] by the end of Q2 2025.

- **Compliance Coverage:** 100% of workloads, data storage, compute resources, network configurations, identity & access management settings aligned with:
  - SOC 2 Type II
  - ISO 27001
  - PCI DSS v4.0
  - HIPAA/HITECH
  - GDPR

- **Governance Implementation:** All cloud policies, standards, and procedures documented and enforced through:
  - Centralized policy management platform (e.g., HashiCorp Sentinel)
  - Automated compliance scanning tools (e.g., Prisma Cloud Compliance)
  - Regular governance reviews with stakeholders

- **Risk Management:** Identification of all high-risk assets categorized by potential impact if compromised or misconfigured.

- **Audit Readiness:** Complete audit trails for all changes, access events, and security incidents maintained for the past 12 months.

**Key Performance Indicators (KPIs):**

1. Zero critical compliance findings post-implementation phase.
2. All governance policies version-controlled with at least one weekly commit.
3. <5% variance between policy-as-code implementations and actual cloud configurations during automated scans.
4. 100% of security incidents logged within the incident management system in the first month post-deployment.

---

### Critical Knowledge Areas (15 Topics)

1. **Cloud Security Fundamentals**
   - Identity & Access Management (IAM)
   - Network Security Groups/ACLs
   - Encryption at Rest and In Transit

2. **Compliance Framework Mapping**
   - SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR mapping to cloud resources.

3. **Data Classification & Protection**
   - Sensitive data handling across regions.
   - Data Residency Requirements

4. **Infrastructure as Code (IaC) Security**
   - Best practices for Terraform/HCL/CloudFormation
   - Policy-as-Code tools (e.g., OPA, Sentinel)

5. **Monitoring & Logging Compliance**
   - Centralized logging solutions (e.g., ELK Stack)
   - Real-time compliance monitoring dashboards

6. **Automated Compliance Scanning**
   - Tools: Prisma Cloud Compliance, AWS Config Rules
   - Integration with CI/CD pipelines

7. **Change Management and Governance**
   - Approval workflows for cloud resource changes.
   - Versioning of policies and configurations.

8. **Incident Response & Security Posture**
   - Playbooks for cloud security incidents.
   - Automated detection and response capabilities.

9. **Data Loss Prevention (DLP) in Cloud**
   - Techniques to prevent sensitive data exfiltration.
   - Integration with existing DLP solutions.

10. **Backup, Recovery, and Disaster Recovery (DR) Compliance**
    - RPO/RTO definitions aligned with compliance requirements.
    - Automated backup verification processes.

11. **Access Review & Privilege Reduction**
    - Scheduling regular access reviews using tools like AWS IAM Access Analyzer.
    - Automating deprovisioning of unused permissions.

12. **Vendor Management & Third-Party Risk**
    - Assessing the security posture of cloud providers and third-party services.
    - Implementing contracts that enforce compliance requirements.

13. **Audit Preparation & Reporting**
    - Configuring AWS Config, Azure Policy, or GCP Compliance Manager for audit-ready configurations.
    - Generating automated compliance reports for auditors.

14. **Cost Governance in Cloud Compliance**
    - Tag-based cost allocation tied to governance policies.
    - Budget alerts and anomaly detection integrated with policy enforcement.

15. **Emerging Threats & Ongoing Compliance Evolution**
    - Staying updated on cloud-specific security threats (e.g., misconfigured S3 buckets).
    - Adapting compliance frameworks as standards evolve in 2024-2025.

---

### Execution Workflow

**STEP 1: [Discovery & Assessment]**
- **Action:** Conduct an inventory of all existing cloud resources using tools like AWS Config, Azure Resource Graph, or GCP Asset Inventory.
- **Tools Needed:** Terraform State Backend (AWS S3/Blob), Cloud provider APIs, Automated scanning tools (e.g., Prisma Cloud Compliance).
- **Success Criteria:** Complete and accurate asset inventory covering all environments (dev, prod, staging) with no gaps in coverage.
- **Common Pitfalls:** Incomplete resource tagging, missing version control for state files, non-standard naming conventions.
- **Time Estimate:** 2 weeks

**STEP 2: [Compliance Gap Analysis]**
- **Action:** Map current configurations to required compliance frameworks using automated scanning tools and manual reviews.
- **Tools Needed:** Prisma Cloud Compliance, AWS Config Rules, OPA/ Sentinel policies for policy-as-code implementations.
- **Success Criteria:** All identified gaps are documented in a centralized ticketing system with assigned remediation owners and due dates.
- **Common Pitfalls:** Manual re-entry of findings from automated scans, missing dependencies across services (e.g., API gateways).
- **Time Estimate:** 1 week

**STEP 3: [Policy Implementation]**
- **Action:** Define and codify all compliance policies using IaC templates with policy-as-code tools like OPA or HashiCorp Sentinel.
- **Tools Needed:** Terraform, AWS CloudFormation/Terraform, Azure Resource Manager Templates (ARM), Google Deployment

