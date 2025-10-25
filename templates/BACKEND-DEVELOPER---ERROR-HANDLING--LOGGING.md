# Backend Developer - AI Agent Template
## Error Handling & Logging

### Success Definition (Measurable)
- **Primary Objective:** Achieve a system where 99.9% of errors are automatically captured, logged, analyzed, and resolved within 2 hours of occurrence.
- **Key Metrics:**
  - **Error Capture Rate:** ≥ 99.95%
  - **Mean Time to Detect (MTTD):** ≤ 30 minutes
  - **Mean Time to Resolve (MTTR):** ≤ 2 hours for critical errors, ≤ 6 hours for non-critical
  - **Logging Quality Score:** Minimum 4 out of 5 on completeness checklist

### Critical Knowledge Areas (Specific to Backend Development)

1. **Error Classification**
   - Types: Syntax, Logic, External Service, Database, Performance, Security
2. **Centralized Logging Architecture**
   - Tools: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk Cloud, Graylog
3. **Structured Logging Formats**
   - JSON vs CSV vs Custom formats
4. **Error Propagation & Breadcrumbs**
   - Libraries: Winston, Bunyan, Rollbar, Sentry
5. **Root Cause Analysis (RCA) Techniques**
   - Five Whys, Fishbone Diagrams, Post-Mortem Documentation
6. **Alerting Systems**
   - Tools: PagerDuty, Opsgenie, Slack Notifications via Webhooks/API
7. **Data Retention & Compliance**
   - GDPR, HIPAA, PCI-DSS requirements for logs
8. **Monitoring vs Logging Distinction**
   - Real-time Monitoring (Prometheus, Grafana) vs Historical Analysis
9. **Microservices Error Handling**
   - Service-specific logging, correlation IDs, circuit breakers
10. **Automated Log Shipping**
    - Docker Logs, Fluentd, Shipper Tools like Filebeats
11. **Performance Logging Metrics**
    - Latency histograms, throughput counters, error rate metrics
12. **Security Logging Best Practices**
    - Audit trails for access control, data breaches detection
13. **Logging Performance Considerations**
    - Minimizing I/O bottlenecks, log file rotation strategies
14. **Multi-Environment Log Management**
    - Development vs Staging vs Production logging configurations
15. **Log Aggregation & Search Capabilities**
    - Faceted search, timestamp filtering, anomaly detection

### Execution Workflow (Remote/Computer-Based)

**STEP 1: Centralized Logging Infrastructure Setup**
- **Action:** Deploy Elasticsearch + Kibana stack using Docker Compose or Kubernetes Helm chart.
- **Tools Needed:** Docker/Kubernetes for containerization, Terraform/Helm for infrastructure as code.
- **Success Criteria:** Logs from all services are being collected and searchable in Kibana within 2 hours of setup.
- **Common Pitfalls:** Misconfigured log pipelines leading to incomplete data ingestion.
- **Time Estimate:** 4 hours

**STEP 2: Implement Structured Logging**
- **Action:** Refactor existing monolithic or microservice codebase to use structured JSON logging via Winston/Bunyan.
- **Tools Needed:** Node.js/Python/Ruby logging libraries, linters for consistency.
- **Success Criteria:** All log messages include timestamp, level (info/warn/error), service name, and request ID.
- **Common Pitfalls:** Developers fall back to plain text logs or inconsistent formatting.
- **Time Estimate:** 8 hours

**STEP 3: Add Error Tracking Integrations**
- **Action:** Integrate error tracking libraries like Sentry/Rollbar into all services.
- **Tools Needed:** Sentry SDK, Rollbar client library compatible with your language/framework.
- **Success Criteria:** First critical error is automatically reported and viewable in the integration's UI within 30 minutes of occurrence.
- **Common Pitfalls:** Misconfigured API keys or service instances causing errors to not be reported.
- **Time Estimate:** 2 hours

**STEP 4: Define Alerting Thresholds**
- **Action:** Configure alerts for critical error patterns using PagerDuty/Opsgenie.
- **Tools Needed:** Alert definitions in PagerDuty, integration with log search for dynamic thresholds.
- **Success Criteria:** Test alerts fire correctly based on simulated error conditions.
- **Common Pitfalls:** Alerts are too generic leading to alert fatigue or not specific enough causing delayed response.
- **Time Estimate:** 2 hours

**STEP 5: Implement RCA Framework**
- **Action:** Define process for root cause analysis of critical errors, including documentation and follow-up actions.
- **Tools Needed:** Confluence/Wiki for RCA documentation, JIRA tickets for corrective tasks.
- **Success Criteria:** At least one full RCA documented within a week of a critical error occurrence.
- **Common Pitfalls:** Lack of consistent documentation leading to incomplete or lost investigations.
- **Time Estimate:** 3 hours

**STEP 6: Set Up Data Retention Policies**
- **Action:** Configure log retention policies based on compliance requirements (e.g., 30 days for sensitive logs, 1 year for operational).
- **Tools Needed:** Kibana index lifecycle manager or Elasticsearch rollup indices.
- **Success Criteria:** Log data is automatically deleted after configured retention period without manual intervention.
- **Common Pitfalls:** Retention policies not aligned with business needs leading to storage concerns.
- **Time Estimate:** 1 hour

**STEP 7: Implement Performance Metrics Logging**
- **Action:** Add metrics for latency, error rates, and throughput to the logging system.
- **Tools Needed:** Prometheus exporters, Grafana dashboards for real-time monitoring.
- **Success Criteria:** Dashboards show trends in error rates correlating with outages or performance issues.
- **Common Pitfalls:** Metrics not being collected due to incorrect exporter configuration.
- **Time Estimate:** 3 hours

**STEP 8: Security Logging Enhancements**
- **Action:** Log all security-relevant events (access control failures, data breaches attempts).
- **Tools Needed:** Audit log collectors, SIEM integration for threat detection.
- **Success Criteria:** Security logs are being ingested and searchable in the centralized logging system.
- **Common Pitfalls:** Overlooking critical access logs leading to blind spots in security monitoring.
- **Time Estimate:** 2 hours

**STEP 9: Implement Log Shipping from Containers**
- **Action:** Configure Docker/Kubernetes log drivers (e.g., json-logger, fluentd) to ship logs to centralized system.
- **Tools Needed:** Fluent Bit or Fluentd for containerized environments.
- **Success Criteria:** Logs from all containers are visible in the central logging UI within 30 minutes of restart.
- **Common Pitfalls:** Misconfigured log drivers leading to loss of logs at startup/shutdown.
- **Time Estimate:** 2 hours

**STEP 10: Optimize Log Storage and Query Performance**
- **Action:** Tune Elasticsearch indices for optimal storage, implement efficient search queries.
- **Tools Needed:** Kibana Dev Tools, Elasticsearch query DSL.
- **Success Criteria:** Queries to retrieve logs under specific error conditions return within 500ms.
- **Common Pitfalls:** Under-provisioned ES nodes leading to degraded performance or timeouts.
- **Time Estimate:** 3 hours

### Troubleshooting Common Issues
1. **Logs Not Appearing in Central System**
   - Verify log shipping is configured correctly (check Fluentd/Docker logs).
   - Ensure Elasticsearch indices are being refreshed regularly.
2. **High Latency When Querying Logs**
   - Check Elasticsearch node resource utilization (CPU, memory).
   - Optimize Kibana query DSL for performance.
3. **Alerts Not Firing**
   - Verify alert thresholds and conditions in PagerDuty/Opsgenie settings.
4. **Logs Are Inconsistent or Missing Fields**
   - Ensure all services are using the same logging library and format (JSON).
5. **Retention Policies Not Applied**
   - Check index lifecycle manager configurations in Elasticsearch.

### Recommended Tool Stack
- **Primary Tools (Free/Open Source):**
  - Elasticsearch + Kibana: [ELK]
  - Prometheus + Grafana: [Prometheus/Grafana Cloud]
  - Fluentd: [Fluentd OSS]
  - Sentry/Rollbar: [Sentry Free Tier/ Rollbar Free Plan]
- **Optional Premium Alternatives:**
  - Splunk (Pro): [Enterprise Search & Analytics]
  - Datadog (AIOps): [Advanced Monitoring & Alerting]
  - PagerDuty Pro: [Comprehensive Incident Management]

### Realistic Timeline to Achieve Error Handling & Logging

**Phase 1:** Research and Planning (2-3 weeks)
- Define logging architecture, choose tools
- Set up centralized log aggregation pipeline

**Phase 2:** Implementation of Centralized Logging (4-6 weeks)
- Deploy ELK stack
- Refactor code for structured JSON logs
- Integrate error tracking SDKs

**Phase 3:** Alerting and RCA Process Setup (1 week)
- Configure alerts based on critical errors
- Document RCA process with templates

**Phase 4:** Performance, Security Logging & Retention Policies (2 weeks)
- Add performance metrics to logs
- Implement security logging enhancements
- Set up data retention policies

**Phase 5:** Optimization and Testing (1-2 weeks)
- Fine-tune query performance
- Validate log completeness with synthetic tests
- Perform disaster recovery testing of logs

