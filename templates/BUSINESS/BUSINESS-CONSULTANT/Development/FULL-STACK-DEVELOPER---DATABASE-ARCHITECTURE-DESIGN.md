# Full Stack Developer - AI Agent Template

## Database Architecture Design

### 1. Critical Knowledge Areas

1. **Database Fundamentals**: Understanding relational vs. NoSQL databases, ACID properties, normalization, and denormalization.
2. **Data Modeling**: Entity-relationship diagrams (ERDs), object-relational mapping (ORM), and database schema design.
3. **SQL/NoSQL Query Optimization**: Writing efficient queries, indexing strategies, and query performance tuning.
4. **Transaction Management**: ACID transactions, distributed transactions, and locking mechanisms.
5. **Data Storage & Caching**: Understanding different storage options (disk vs. memory), caching layers (Redis, Memcached), and their roles in database architecture.
6. **Security Best Practices**: Encryption at rest and in transit, secure authentication mechanisms, role-based access control, and data masking.
7. **Scalability & Performance**: Designing for horizontal scaling, load balancing, sharding strategies, and read/write replication.
8. **Backup & Disaster Recovery**: Implementing backup solutions (e.g., AWS RDS snapshots), disaster recovery plans, and database version control.
9. **Monitoring & Alerting**: Tools for monitoring database health, performance metrics, alert configurations, and automated failover mechanisms.
10. **Cloud Database Services**: Understanding managed cloud databases (e.g., Amazon RDS, Google Cloud SQL) vs. self-managed solutions.

### 2. Execution Steps

1. **Requirement Analysis**:
   - Gather functional requirements for data storage.
   - Identify non-functional requirements (performance, scalability, security).

2. **Data Modeling**:
   - Create ERDs to visualize the database schema.
   - Define tables, columns, data types, and relationships.

3. **Database Selection**:
   - Choose between relational (e.g., PostgreSQL) or NoSQL databases based on application needs.
   - Consider factors like ACID compliance, scalability requirements, and query complexity.

4. **Schema Design**:
   - Normalize the database schema to minimize redundancy and ensure data integrity.
   - Implement denormalization where necessary for performance optimization.

5. **Query Optimization**:
   - Analyze common queries and their impact on performance.
   - Add indexes to improve query execution speed.
   - Consider using ORM tools (e.g., Sequelize, Django ORM) for efficient database interaction in the application code.

6. **Security Implementation**:
   - Encrypt sensitive data both at rest and in transit.
   - Implement role-based access control mechanisms.
   - Use secure authentication methods (e.g., OAuth2).

7. **Scalability Planning**:
   - Design the database to handle expected growth in data volume and transaction throughput.
   - Plan for horizontal scaling by distributing data across multiple nodes.

8. **Backup Strategy**:
   - Implement automated backup solutions.
   - Test regular restoration of backups to ensure reliability.

9. **Monitoring Setup**:
   - Configure monitoring tools to track key performance indicators (KPIs) such as response times, error rates, and resource utilization.
   - Set up alerts for critical issues that require immediate attention.

10. **Disaster Recovery Plan**:
    - Document a comprehensive disaster recovery plan including steps for data restoration in case of catastrophic failures.
    - Regularly test the disaster recovery process to ensure its effectiveness.

### 3. Tools, Software, and Platforms

- **Primary Tool (free)**: PostgreSQL
  - A powerful, open-source relational database system with robust support for ACID transactions and advanced querying capabilities.

- **Alternative Tool (paid, optional)**: MongoDB Atlas (Cloud Managed Service)
  - Offers a fully-managed NoSQL database service hosted on the cloud with automatic scaling, backup, and high availability features.

- **Version Control**: Git (GitHub/GitLab/Bitbucket)
  - Essential for tracking changes in your database schema migrations and application code.

- **IDE**: Visual Studio Code (free)
  - A lightweight yet powerful IDE that supports multiple programming languages including SQL.

- **Database Query Tool**: pgAdmin (free) or MongoDB Compass
  - GUI tools to interact with PostgreSQL and MongoDB databases respectively, for easier data modeling and query testing.

### 4. Success Criteria

- **Scalability**: Database can handle increased load without degradation in performance.
- **Security Compliance**: All sensitive data is encrypted and access controls are properly enforced.
- **Performance**: Average response times for database queries remain within acceptable limits even under peak loads.
- **Reliability**: The database service uptime meets the SLA (Service Level Agreement) targets.

### 5. Troubleshooting Common Issues

1. **High CPU/IO Usage**:
   - Check query performance and optimize as needed.
   - Review indexing strategy to ensure queries are efficient.

2. **Connection Failures**:
   - Verify database server is running.
   - Ensure firewall rules allow traffic on the DB port (default 5432 for PostgreSQL).

3. **Data Corruption**:
   - Use backup restoration procedures to recover from corrupted data.
   - Implement periodic integrity checks using database-specific tools.

4. **Security Breaches**:
   - Review access logs and revoke unauthorized credentials immediately.
   - Update encryption keys if necessary to mitigate risks associated with compromised credentials.

### 6. Recommended Tool Stack (2024-2025 Best Practices)

- **Primary Database**: PostgreSQL
- **Database Management Platform**: pgAdmin or MongoDB Compass
- **Version Control System**: Git with GitHub/GitLab/Bitbucket
- **IDE**: Visual Studio Code
- **CI/CD Pipeline**: Jenkins, GitHub Actions, or CircleCI (optional)
- **Monitoring & Alerting**: Prometheus + Grafana, Datadog (optional), New Relic (premium alternative)

### 7. Realistic Timeline

1. **Weeks 1-2**: Requirement Analysis and Initial Data Modeling
   - Focus on gathering requirements and creating initial ERDs.

2. **Weeks 3-4**: Database Selection, Schema Design, and Security Implementation
   - Choose the database type and design the schema with security best practices in mind.

3. **Weeks 5-6**: Query Optimization and Performance Tuning
   - Write efficient queries and optimize performance through indexing and other techniques.

4. **Weeks 7-8**: Backup Strategy, Monitoring Setup, and Disaster Recovery Planning
   - Implement backup solutions and configure monitoring tools for real-time insights into database health.

### 8. Conclusion

By following this comprehensive template, a full stack developer can design an efficient, secure, and scalable database architecture that meets the application's requirements while adhering to modern best practices in 2024-2025. The emphasis on using primarily free/open-source tools ensures cost-effectiveness without compromising quality or performance.

---

