# System Administrator - AI Agent Template
## Stable Server Environment

### Success Definition (Measurable)
**Stable Server Environment Defined:** A system where all servers operate at 99.9% uptime, critical services are restored within 15 minutes of failure, and security vulnerabilities are patched weekly with zero successful breaches over a quarter.

**Key Metrics:**
- **Uptime:** ≥ 99.9%
- **Mean Time to Recovery (MTTR):** ≤ 15 minutes
- **Weekly Patch Compliance:** ≥ 100%
- **Security Incidents per Quarter:** 0

### Critical Knowledge Areas for System Administrator
1. **Operating Systems Fundamentals** - Mastery of Linux distributions (Ubuntu, CentOS), Windows Server administration.
2. **Network Configuration & Security** - TCP/IP, DNS, DHCP, Firewalls (iptables, UFW), VPNs.
3. **Virtualization Technologies** - KVM/QEMU for virtual machines, Docker/Kubernetes orchestration.
4. **Backup & Recovery Strategies** - Rsync, BTRFS snapshots, cloud storage integration (AWS S3).
5. **Monitoring Tools** - Prometheus, Grafana, Nagios/Zabbix, ELK Stack.
6. **Automation & Scripting** - Bash/Python scripting for provisioning, Ansible/Puppet/Chef configuration management.
7. **Capacity Planning & Performance Tuning** - iostat, vmstat, top, tuning kernel parameters.
8. **Change Management Systems** - GitLab CI/CD pipelines, Jenkins for automated deployments.
9. **Security Best Practices** - Regularly scanning with OpenVAS/Nessus, implementing Fail2Ban.
10. **Incident Response Protocols** - Playbooks for common issues (service down, data leakage).
11. **Log Management & Analysis** - Logrotate configurations, Splunk/ELK analysis.
12. **Cloud Infrastructure Fundamentals** - AWS EC2, RDS, EFS; GCP Compute Engine, Kubernetes on Cloud.
13. **Compliance Standards** - PCI-DSS, HIPAA for server environments.
14. **Database Administration** - MySQL/MariaDB, PostgreSQL tuning, replication setups.
15. **Container Orchestration** - Deployment strategies using Docker Swarm/Kubernetes.

### Execution Steps with Specific Actions

#### Step 1: Environment Assessment
- **Action:** Inventory all servers (IP, OS version, services running).
- **Tools Needed:** `nmap`, AWS Directory Service, Azure Resource Explorer.
- **Success Criteria:** Complete inventory report within 24 hours.
- **Common Pitfalls:** Missing hidden services or containers.
- **Time Estimate:** 2 days

#### Step 2: Implement Secure Access Controls
- **Action:** Harden SSH (disable root login), enforce multi-factor authentication (MFA).
- **Tools Needed:** Fail2Ban, PAM configurations.
- **Success Criteria:** No unauthorized access attempts logged for a week.
- **Common Pitfalls:** Incorrect firewall rules allowing brute-force attacks.
- **Time Estimate:** 1 day

#### Step 3: Configure Automated Backups
- **Action:** Set up daily incremental backups to AWS S3 using Rclone.
- **Tools Needed:** Rclone, cron jobs, AWS IAM roles.
- **Success Criteria:** Backup integrity verified weekly; restores successful within 30 minutes.
- **Common Pitfalls:** Disk full due to lack of rotation policy.
- **Time Estimate:** 1 day

#### Step 4: Implement Monitoring Stack
- **Action:** Deploy Prometheus for metrics collection and Grafana for dashboards.
- **Tools Needed:** Prometheus, Grafana, Loki logging.
- **Success Criteria:** Real-time monitoring alerts configured; system stability graphed over a month.
- **Common Pitfalls:** Alerts not firing due to incorrect thresholds.
- **Time Estimate:** 2 days

#### Step 5: Set Up Automated Patch Management
- **Action:** Configure unattended upgrades on Debian/Ubuntu servers using Unattended-Upgrades.
- **Tools Needed:** Unattended-Upgrade, apt-cron.
- **Success Criteria:** Weekly patch compliance ≥ 100% without manual intervention.
- **Common Pitfalls:** Dependencies breaking due to major version changes.
- **Time Estimate:** 1 day

#### Step 6: Containerize Applications
- **Action:** Refactor critical services into Docker containers and deploy on Kubernetes cluster.
- **Tools Needed:** Docker, Helm charts, K8s manifests.
- **Success Criteria:** Zero downtime during migration; rollback possible within 5 minutes.
- **Common Pitfalls:** Resource limits causing service crashes.
- **Time Estimate:** 3 days

#### Step 7: Implement Failover Solutions
- **Action:** Set up DNS failover with Cloudflare, configure load balancing on NGINX/HAProxy.
- **Tools Needed:** Cloudflare API, HAProxy configuration files.
- **Success Criteria:** Automatic traffic rerouting tested during simulated outages; <5 minutes downtime.
- **Common Pitfalls:** Misconfigured health checks triggering unnecessary failovers.
- **Time Estimate:** 2 days

#### Step 8: Configure Logging and Alerting
- **Action:** Centralize logs using Fluentd to Elasticsearch, set up alert rules in Prometheus.
- **Tools Needed:** Fluentd, Elastic Stack (Kibana), Alertmanager.
- **Success Criteria:** Log integrity maintained; alerts triggered for critical events within minutes.
- **Common Pitfalls:** Logs not forwarding correctly due to firewall restrictions.
- **Time Estimate:** 1 day

#### Step 9: Implement Role-Based Access Control (RBAC)
- **Action:** Define roles based on job functions and assign permissions via LDAP/Active Directory integration.
- **Tools Needed:** OpenLDAP, Active Directory Federation Services.
- **Success Criteria:** Audits show no overprivileged accounts; changes logged automatically.
- **Common Pitfalls:** Inconsistent application of permissions due to manual account creation.
- **Time Estimate:** 1 day

#### Step 10: Conduct Regular Security Assessments
- **Action:** Run vulnerability scans (OpenVAS) and penetration tests monthly using Metasploit.
- **Tools Needed:** OpenVAS, Nmap, Metasploit Framework.
- **Success Criteria:** No critical vulnerabilities remain unpatched; security score ≥ A+.
- **Common Pitfalls:** False positives leading to unnecessary delays in deployment.
- **Time Estimate:** 1 month (ongoing)

#### Step 11: Implement Change Management Workflow
- **Action:** Use GitLab CI/CD pipelines for deployments, integrate with Slack notifications.
- **Tools Needed:** GitLab CI, Slack API webhook.
- **Success Criteria:** All changes undergo automated testing and approval; deployment failures <5%.
- **Common Pitfalls:** Manual overrides bypassing approvals leading to drift.
- **Time Estimate:** 2 days

#### Step 12: Document Processes & Knowledge Transfer
- **Action:** Write SOPs for each critical process, create training materials for new hires.
- **Tools Needed:** Confluence, Markdown docs, Loom videos.
- **Success Criteria:** New team members can follow documented processes to resolve issues independently within a week.
- **Common Pitfalls:** Outdated documentation not reviewed regularly.
- **Time Estimate:** 1 month (ongoing)

### Tools & Software Stack

#### Primary Tools (Free/Open Source)
- **Version Control:** GitLab, GitHub
- **Automation/Orchestration:** Ansible, Terraform (IaC), Jenkins, Docker
- **Container Orchestration:** Kubernetes (EKS/AKS/GKE), Helm
- **Monitoring:** Prometheus + Grafana, Loki for logs, Alertmanager
- **Security Scanning:** OpenVAS, Nmap, Fail2Ban
- **Backup:** Rclone, AWS S3
- **CI/CD:** Jenkins (self-hosted)
- **Documentation:** Confluence, Markdown docs on GitHub

#### Alternative Tools (Paid/Premium)
- **Cloud Services:** AWS Management Console, Azure Portal (optional), GCP Cloud Shell
- **Load Balancing:** AWS Route 53 DNS failover (premium add-on)
- **Incident Response:** Splunk Enterprise Security Suite (paid tier)
- **Container Orchestration Add-ons:** Red Hat Ansible Tower for enterprise management

### Troubleshooting Common Issues

#### Issue: Server Crashes on Startup
1. Check system logs (`/var/log/syslog`, `/var/log/kern.log`).
2. Ensure kernel version compatibility.
3. Verify Docker/Kubernetes health status.

#### Issue: Persistent Connection Drops
1. Test network latency and packet loss with `ping`, `traceroute`.
2. Review firewall rules (iptables/UFW) for connection limits.
3. Check VPN client configuration if applicable.

#### Issue: Resource Exhaustion (CPU/Memory)
1. Monitor resource usage via `top`, `htop`, or Prometheus metrics.
2. Identify long-running processes causing spikes.
3. Adjust Docker/Kubernetes resource requests/limits.

#### Issue: Security Breach Detected
1. Review alert logs in ELK Stack for recent anomalies.
2. Scan system with OpenVAS/Nessus immediately after incident.
3. Rotate all passwords and revoke compromised accounts.

### Recommended Tool Stack (2024-2025)

| Category | Primary Tool (Free) | Alternative (Paid/Premium) |
|----------|---------------------|----------------------------|
| Version Control | GitLab, GitHub | SourceTree (paid GUI), SmartGit |
| Automation | Ansible, Terraform | Red Hat Ansible Tower, CloudBees Jenkins |
| Container Orchestration | Kubernetes, Docker Swarm | Helm Charts for K8s add-ons |
| Monitoring | Prometheus + Grafana, Loki | Splunk Enterprise Security Suite |
| Security Scanning | OpenVAS, Nmap | Qualys Vulnerability Manager (paid) |
| Backup & Storage | Rclone, AWS S3 | Backblaze B2 (cloud storage), Veeam Backup |
| CI/CD | Jenkins, GitHub Actions | GitLab CI Premium Add-ons |

### Timeline to Achieve Stable Server Environment

**Month 1:**  
- Complete environment assessment and inventory.
- Harden access controls and configure MFA.
- Set up automated backups with initial test restore.

**Month 2:**  
- Deploy monitoring stack and verify alerts.
- Implement automated patch management.
- Containerize one critical service and deploy to K8s cluster.

**Month 3:**  
- Roll out DNS failover solution and load balancers for high availability.
- Centralize logs and set up alerting system.
- Document processes and conduct knowledge transfer sessions with team members.

**Months 4-5:**  
- Conduct regular security assessments (weekly scans, monthly penetration tests).
- Implement RBAC and integrate LDAP/AD for user management.
- Refactor remaining services into containers or microservices as needed.

**Month 6+:**  
- Optimize performance tuning based on metrics.
- Continue training new hires through documented processes.
- Review and update all policies annually to ensure compliance with industry standards.

