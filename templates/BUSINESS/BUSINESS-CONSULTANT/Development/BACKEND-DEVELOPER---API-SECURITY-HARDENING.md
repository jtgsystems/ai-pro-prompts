# Backend Developer - AI Agent Template

## API Security Hardening

### Critical Knowledge Areas (10-15)

1. **API Design Best Practices**
2. **Authentication & Authorization**
3. **Input Validation & Sanitization**
4. **Data Encryption in Transit**
5. **Data Encryption at Rest**
6. **Rate Limiting & Brute Force Protection**
7. **Error Handling and Information Disclosure Prevention**
8. **Logging, Monitoring, and Auditing**
9. **Dependency Management & Vulnerability Scanning**
10. **Secure Configuration Management**
11. **OAuth 2.0 & OpenID Connect**
12. **JSON Web Tokens (JWT) Security**
13. **API Gateway Best Practices**
14. **Web Application Firewall (WAF) Integration**
15. **Compliance Standards (e.g., PCI DSS, GDPR)**

### Detailed Execution Steps

1. **Conduct API Inventory**: Catalog all APIs in use, including versions, endpoints, and data types handled.
2. **Implement Strong Authentication**: Use OAuth 2.0 or OpenID Connect for authentication; validate tokens securely on each request.
3. **Validate All Input Data**: Enforce strict input validation using schema definitions (e.g., JSON Schema) to prevent injection attacks.
4. **Encrypt Sensitive Data**: Ensure all sensitive data is encrypted at rest and in transit using TLS 1.2+ protocols.
5. **Set Up Rate Limiting**: Implement rate limiting on API endpoints to mitigate brute force attacks and abuse.
6. **Secure Error Handling**: Standardize error messages to prevent information leakage; log errors securely without exposing details.
7. **Enable Logging & Monitoring**: Use tools like ELK Stack (Elasticsearch, Logstash, Kibana) or Splunk for centralized logging and monitoring API activity.
8. **Perform Regular Security Audits**: Schedule regular code reviews and penetration testing to identify vulnerabilities.
9. **Automate Dependency Scanning**: Integrate Snyk or OWASP Dependency-Check into CI/CD pipelines to scan for vulnerable dependencies.
10. **Apply Secure Configurations**: Ensure all configurations (e.g., database settings, network policies) follow the principle of least privilege.

### Tools, Software, and Platforms

- **Version Control**: Git (GitHub/GitLab)
- **Code Editor**: VS Code (free) or Sublime Text ($70, optional)
- **API Gateway**: Kong (free), Amazon API Gateway (optional - $0.008 per GB processed)
- **Logging & Monitoring**: ELK Stack (Elasticsearch, Logstash, Kibana) or Splunk Enterprise Security (free tier up to 5 users, paid for scaling)
- **Dependency Scanning**: Snyk (free tier includes basic scanning), OWASP Dependency-Check
- **Authentication Management**: Auth0 (free tier limited user support), Keycloak
- **Security Testing**: Burp Suite Community Edition (free), ZAP (Zed Attack Proxy) (open-source)

### Success Criteria

1. **No Critical Vulnerabilities**: All security scans must return no critical vulnerabilities.
2. **Authenticated Access Only**: 100% of endpoints require authenticated access using OAuth 2.0 or similar.
3. **Rate Limiting Configured**: Each API endpoint has appropriate rate limiting thresholds configured.
4. **Compliance Checklist Completed**: All compliance requirements (e.g., PCI DSS, GDPR) are documented and met.
5. **Monitoring Alerts Functional**: Alert mechanisms for unusual activity are operational and tested.

### Troubleshooting Common Issues

- **Authentication Failures**: Verify token expiration logic; check that the JWT claims are correctly validated.
- **Rate Limit Exceeded**: Ensure rate limiting is applied per IP or user session, not globally across all requests.
- **Sensitive Data Exposure in Logs**: Configure logging to mask sensitive information (e.g., API keys) before it's written to logs.

### Recommended Tool Stack with Pricing

- **Primary**:
  - VS Code: Free
  - Kong API Gateway: Free tier available; paid for enterprise features ($0.008 per GB processed)
  - ELK Stack: Free, open-source (optional add-on cloud services for Kibana/Dashboard may require payment)
- **Alternative/Premium**:
  - Splunk Enterprise Security: $3,999-$5,499/year
  - Auth0: Starts at $0.02 per user/month
  - Burp Suite Pro: $399/year

### Realistic Timeline

1. **Initial Assessment & Planning**: 2 weeks (including API inventory and requirements gathering)
2. **Implementation Phase**: 4-6 weeks (depending on complexity of existing APIs and number of endpoints to secure)
3. **Testing & Validation**: 2 weeks (includes security testing, rate limiting configuration, and input validation refinement)
4. **Monitoring & Maintenance**: Ongoing (continuous monitoring setup with alerts configured)

### Best Practices for 2024-2025

1. **Adopt Serverless Architectures Wisely**: Evaluate the trade-offs of serverless functions in terms of security and performance.
2. **Implement API Rate Limiting at Edge Proxies**: Use edge computing platforms like Cloudflare to apply rate limiting closer to users.
3. **Regularly Update Dependency Versions**: Leverage GitHub Dependabot or Renovate for automatic dependency updates.
4. **Use WAF Rules for Advanced Threat Protection**: Configure AWS WAF, Azure DDoS Protection, or Google Cloud Armor with custom rules for emerging threats.

This comprehensive template provides a structured approach for Backend Developers to harden their APIs against common vulnerabilities and attacks while adhering to best practices as of 2024-2025.

