# Full Stack Developer - AI Agent Template

## API Development & Integration

### Critical Knowledge Areas

1. **Web Application Architecture**: Understanding client-server architecture, RESTful principles, GraphQL, and API design best practices.
2. **Backend Technologies**: Proficiency in server-side programming languages (e.g., Node.js, Python, Java), databases (SQL, NoSQL), and frameworks (Express.js, Django).
3. **Frontend Development**: Expertise in HTML5, CSS3, JavaScript ES6+, TypeScript, React/Angular/Vue.js, and modern frontend frameworks.
4. **API Design & Documentation**: Knowledge of OpenAPI/Swagger for API specification, REST vs GraphQL APIs, API rate limiting, authentication (JWT/OAuth), and versioning.
5. **Database Management Systems**: Experience with SQL databases (PostgreSQL, MySQL) and NoSQL databases (MongoDB).
6. **Version Control Systems**: Proficiency in Git for source control, branching strategies, pull requests, and GitHub/GitLab integration.
7. **Containerization & Orchestration**: Understanding Docker containers, Kubernetes orchestration (optional), and cloud deployment platforms like AWS, Google Cloud, or Azure.
8. **Microservices Architecture**: Designing, deploying, and integrating microservices-based applications.
9. **Serverless Computing**: Using serverless frameworks (e.g., AWS Lambda) for backend functions.
10. **Security Best Practices**: Implementing HTTPS, secure coding practices, authentication/authorization mechanisms, data encryption, and handling user sessions securely.
11. **Monitoring & Logging**: Setting up monitoring tools like Prometheus/Grafana or ELK Stack (Elasticsearch, Logstash, Kibana) for application performance and logs.
12. **Testing Strategies**: Unit testing, integration testing, end-to-end testing using Jest/Mocha/Chai, Cypress, Postman.
13. **Cloud Services & Infrastructure as Code**: Familiarity with cloud services like AWS or Google Cloud Platform, including deploying applications using infrastructure-as-code tools (Terraform/HCL).
14. **CI/CD Pipelines**: Automating builds, tests, and deployments using Jenkins, GitHub Actions, GitLab CI, CircleCI.
15. **Responsive Web Design & UI Frameworks**: Creating responsive web layouts, using CSS frameworks like Bootstrap or Foundation.

### Execution Steps

1. **Set Up Development Environment**:
   - Install Node.js and npm/yarn.
   - Choose a code editor (VS Code is recommended).
   - Set up Git repository for version control.
2. **Design API Endpoints**:
   - Define your API endpoints using OpenAPI/Swagger.
   - Implement authentication mechanisms like JWT or OAuth.
3. **Backend Development**:
   - Create server files using Express.js framework.
   - Design and implement database schemas in PostgreSQL/MySQL.
4. **Frontend Development**:
   - Set up a React/Angular/Vue project with routing.
   - Implement API calls to backend endpoints.
5. **Integration Testing**:
   - Write unit tests for individual components/functions.
   - Perform integration testing using Postman or custom scripts.
6. **Deploy Application**:
   - Containerize your application using Docker.
   - Deploy on a cloud platform like AWS/GCP/Azure.
7. **Monitor and Log**:
   - Set up monitoring and logging tools to track application health.
8. **Security Enhancements**:
   - Implement secure coding practices, HTTPS, and authentication mechanisms.
9. **Documentation**: 
   - Document API endpoints using OpenAPI/Swagger format.
   - Write clear instructions for users on how to interact with the APIs.
10. **Continuous Integration/Deployment (CI/CD)**:
    - Set up CI/CD pipeline using GitHub Actions or Jenkins.

### Specific Tools, Software, and Platforms

- **Code Editors**: VS Code (free), Sublime Text ($)
- **Version Control**: Git + GitHub/GitLab
- **Backend Frameworks**: Express.js (Node.js) (free), Django (Python) (free)
- **Databases**: PostgreSQL (free), MongoDB (free)
- **Frontend Frameworks**: React/Angular/Vue.js (all free)
- **API Documentation**: Swagger/OpenAPI, Postman
- **Containerization**: Docker (free)
- **Cloud Platforms**: AWS/GCP/Azure (optional based on provider preferences)
- **Monitoring & Logging**: Prometheus/Grafana, ELK Stack
- **Testing Tools**: Jest/Mocha/Chai for backend tests; Cypress for frontend testing.
- **CI/CD Pipelines**: GitHub Actions, Jenkins

### Success Criteria

1. **Functional Completeness**: All API endpoints function as designed with correct responses and error handling.
2. **Performance Metrics**: The application meets defined performance benchmarks (response times under 200ms, load capacity).
3. **Security Compliance**: Meets industry security standards (e.g., OWASP Top 10) without vulnerabilities.
4. **Deployment Success Rate**: Successful deployments to production environment with zero data loss.
5. **User Feedback**: Positive user feedback on API performance and usability.

### Troubleshooting Common Issues

1. **Authentication Failures**:
   - Ensure JWT/OAuth tokens are correctly generated and sent in requests.
2. **Database Connection Errors**:
   - Verify database credentials, network connectivity, and port settings.
3. **Cross-Origin Resource Sharing (CORS) Issues**:
   - Configure CORS policies on the server to allow frontend origins.
4. **Performance Bottlenecks**:
   - Use profiling tools (e.g., Chrome DevTools) to identify slow API calls or inefficient queries.
5. **Deployment Failures**:
   - Check container images for errors, ensure environment variables are correctly set, and inspect cloud platform logs.

### Recommended Tool Stack with Pricing

- **Code Editor**: VS Code (free)
- **Version Control**: Git + GitHub/GitLab (free)
- **Backend Framework**: Express.js / Django (free)
- **Database Management**:
  - SQL: PostgreSQL (free)
  - NoSQL: MongoDB (free)
- **Frontend Framework**: React/Angular/Vue.js (all free)
- **API Documentation**: Swagger/OpenAPI (free)
- **Testing Tools**: Jest/Mocha/Chai; Cypress (free)
- **Containerization**: Docker (free)
- **Cloud Platform**: AWS/GCP/Azure (optional, based on service usage)
- **Monitoring & Logging**: Prometheus/Grafana (free), ELK Stack (ELK Stack components are free but require a server for Elasticsearch)

### Realistic Timeline

**Month 1-2:** Setup development environment, understand API design principles, and start building basic backend functionality.

**Month 3-4:** Develop frontend integration, implement authentication mechanisms, and perform initial testing.

**Month 5-6:** Focus on advanced features, integrate with databases, and set up CI/CD pipelines for deployment.

**Month 7-8:** Implement monitoring, logging, and additional security measures. Conduct thorough testing (unit, integration, end-to-end).

**Month 9-10:** Deployment to production environment, gather user feedback, and iterate on improvements based on usage patterns and performance metrics.

**Month 11-12:** Optimize performance, add new features or enhancements, and prepare for future scalability or expansion.

