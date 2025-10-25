# Database Administrator - AI Agent Template
## Replication & Failover

### Success Definition (Measurable)
- **Primary Objective:** Ensure zero data loss during planned downtime, with automatic failover to secondary database within 5 minutes of primary failure detection.
- **Key Performance Indicators:**
  - Mean Time To Recovery (MTTR) ≤ 5 minutes
  - Data integrity verification pass rate ≥ 99.999%
  - Failover success test frequency ≥ 2 times per quarter

### Critical Knowledge Areas for Database Administrator (10-20 Topics)

1. **Database Replication Fundamentals**
   - Types of replication: synchronous vs asynchronous, master-slave vs multi-master
   - Data synchronization mechanisms and latency considerations

2. **Failover Strategies**
   - Active-passive failover procedures
   - Load balancing across replicas for read operations
   - Automated failover using database management system features or third-party tools

3. **Data Synchronization Tools**
   - Built-in replication features (e.g., MySQL Galera, PostgreSQL streaming)
   - Open-source synchronization tools: Bucardo, DeZync, Slony-I
   - Cloud-based replication services (AWS DMS, Azure Database Migration Service)

4. **Monitoring & Alerting**
   - Metrics to monitor: replication lag, connection errors, resource utilization
   - Tools for real-time monitoring and alerting: Prometheus, Grafana, Nagios

5. **Backup and Restore Procedures**
   - Full vs incremental backups
   - Point-in-time recovery mechanisms
   - Backup validation processes

6. **Security Considerations**
   - Network segmentation for replication traffic
   - Encryption at rest and in transit
   - Role-based access control for replica management

7. **Performance Tuning**
   - Identifying performance bottlenecks in replicas
   - Optimizing database parameters for replication workloads
   - Load testing replication setup before production use

8. **Disaster Recovery Planning**
   - Offsite backup strategy
   - RTO/RPO (Recovery Time Objective/Recovery Point Objective) definitions
   - Regular disaster recovery drills and updates

9. **Version Compatibility**
   - Ensuring all replicas are running compatible database versions
   - Handling schema changes across primary and replica databases

10. **Automated Failover Testing**
    - Simulating primary failure scenarios
    - Verifying automatic promotion of replica to primary role
    - Documenting manual failover procedures for emergencies

11. **Integration with Cloud Services (optional)**
    - Using cloud provider managed database services for replication
    - Leveraging managed failover solutions offered by cloud providers

12. **Compliance and Auditing**
    - Ensuring replication and failover processes meet regulatory requirements
    - Providing audit trails of all configuration changes and system events

### Step-by-Step Execution Workflow

#### Step 1: Design Replication Topology (2 weeks)
- **Action:** Define primary-secondary or multi-master replication architecture based on application needs.
- **Tools Needed:** Database design documentation, network diagrams.
- **Success Criteria:** Architecture approved by stakeholders with clear roles for primary and secondary nodes.

#### Step 2: Implement Initial Replication Setup (1 week)
- **Action:** Configure initial data synchronization between primary and replica using chosen tooling (e.g., Bucardo).
- **Tools Needed:** Database configuration scripts, replication setup tools.
- **Success Criteria:** Data successfully replicated in near real-time with minimal lag.

#### Step 3: Configure Monitoring & Alerting (1 week)
- **Action:** Set up monitoring for replication health, connection issues, and performance metrics using Prometheus/Grafana or Nagios.
- **Tools Needed:** Monitoring configuration scripts, alert rules defined.
- **Success Criteria:** Alerts triggered correctly during simulated failover scenarios.

#### Step 4: Establish Backup Strategy (1 week)
- **Action:** Implement automated backup procedures with retention policies. Test restore capabilities at least quarterly.
- **Tools Needed:** Backup software (e.g., Percona XtraBackup), restore scripts.
- **Success Criteria:** Restores completed successfully without data loss.

#### Step 5: Perform Automated Failover Testing (1 week)
- **Action:** Conduct failover drills to validate automatic promotion of replica and application connectivity.
- **Tools Needed:** Test orchestration tools, documentation templates for post-test analysis.
- **Success Criteria:** System meets MTTR ≤ 5 minutes with all data integrity checks passing.

#### Step 6: Optimize Performance (2 weeks)
- **Action:** Analyze replication lag, CPU/memory usage on nodes. Tune database parameters and network settings as needed.
- **Tools Needed:** Benchmarking tools, profiling scripts.
- **Success Criteria:** Replication latency reduced to < 1 minute under peak load.

#### Step 7: Review Security Configuration (1 week)
- **Action:** Harden replication traffic with TLS encryption. Implement role-based access for administrative tasks.
- **Tools Needed:** Firewall rules, IAM policies, network segmentation tools.
- **Success Criteria:** All replication interfaces accessible only to authorized services/roles.

#### Step 8: Disaster Recovery Drill (Biannual)
- **Action:** Simulate catastrophic failure of primary node. Verify automatic failover and data restoration processes.
- **Tools Needed:** DR simulation scripts, post-mortem documentation templates.
- **Success Criteria:** System recovers within RTO/RPO targets without service disruption.

### Recommended Tool Stack

**Primary Tools (Free/Open Source):**
1. **Bucardo** - Robust database replication system for PostgreSQL and other databases
2. **PostGIS** - Spatial extensions for geographic data handling
3. **Prometheus & Grafana** - Monitoring and alerting solution
4. **Nagios** - Comprehensive monitoring tool (optional alternative)
5. **Percona XtraBackup** - InnoDB backup and restore utility

**Alternative Tools (Paid):**
1. **AWS Database Migration Service** - Managed replication service for AWS databases
2. **Azure Database Migration Service** - Similar managed solution for Azure platforms
3. **GoldenGate** - Advanced high-performance binary log shipping tool (paid)
4. **Red Hat Virtualization Manager** - For managing virtualized database environments

### Troubleshooting Common Issues

- **Replication Lag:** Check network latency, disk I/O, and CPU utilization on both nodes.
- **Failover Failure:** Verify firewall rules allow replication traffic, ensure primary node is marked as active in configuration.
- **Data Inconsistency:** Inspect application logs for unexpected shutdowns or reconnections during failover.
- **Performance Degradation:** Monitor resource usage patterns; consider increasing replica instances or adjusting workload.

### Realistic Timeline to Achieve Replication & Failover

**Phase 1 (Weeks 1-4): Design, Setup, and Initial Testing**
- Architecture design
- Initial replication setup
- Monitoring integration
- Backup/Restore verification

**Phase 2 (Weeks 5-8): Optimization and Validation**
- Performance tuning
- Security hardening
- Automated failover testing

**Phase 3 (Ongoing): Maintenance and Improvement**
- Regular monitoring and alerting reviews
- Quarterly backup validation drills
- Semi-annual disaster recovery updates

**Total Time Estimate:** 2 months for initial implementation, with ongoing maintenance required

