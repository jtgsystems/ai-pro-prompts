# Computer Technician - AI Agent Template

## Network Configuration

### Critical Knowledge Areas:
1. Networking Fundamentals (TCP/IP, OSI model)
2. Network Topologies (Bus, Ring, Star, Mesh)
3. Switching and Routing Concepts
4. Subnetting and CIDR Notation
5. Firewalls and Access Control Lists (ACLs)
6. Virtual Private Networks (VPNs)
7. Wireless Networking (IEEE 802.11 standards)
8. Network Security Best Practices
9. Troubleshooting Techniques
10. Network Performance Monitoring

### Execution Steps:
1. **Assessment**: Gather requirements, understand the client's needs, and assess existing network infrastructure.
2. **Planning**: Create a detailed plan outlining the desired network configuration, including topologies, subnetting schemes, security measures, and performance metrics.
3. **Design**: Develop a schematic of the proposed network layout using tools like Lucidchart or draw.io (free).
4. **Implementation**:
   - Configure network devices (switches, routers) using command-line interfaces (CLIs). Use GNS3 (free) for simulation before deployment.
   - Set up VLANs and trunking as needed.
   - Implement firewall rules and ACLs.
5. **Testing**: Verify connectivity, performance, and security measures through protocols like ping, traceroute, and Nmap (free).
6. **Documentation**: Update network diagrams, configuration guides, and maintenance records.
7. **Training**: Educate the client or end-users on new network features and best practices for maintaining a secure connection.
8. **Monitoring**: Set up monitoring tools to track network performance and security incidents.

### Specific Tools, Software, and Platforms:
- **Network Protocols**: Ping, Traceroute (built-in), Nmap
- **Simulation**: GNS3 (free)
- **Documentation**: Lucidchart, draw.io, or similar diagramming tools
- **Monitoring**: Nagios Core (free), Zabbix (free), PRTG Network Monitor (optional premium)
- **Security**: Wireshark (free), OpenVAS (free)

### Success Criteria:
- **Connectivity**: 99.9% uptime over a 30-day period.
- **Performance**: Average latency of <50ms for critical applications and <100ms for the rest.
- **Security**: No unauthorized access detected; no malware or suspicious traffic identified.
- **Compliance**: Meets industry security standards (e.g., ISO/IEC 27001).

### Troubleshooting Common Issues:
1. **Loss of Connectivity**:
   - Verify physical connections and test network cables.
   - Check IP configuration (DHCP, DNS).
   - Review logs for any errors or alerts.
2. **Slow Performance**:
   - Conduct bandwidth tests using ping/traceroute.
   - Look for bottlenecks in the topology or congestion on links.
3. **Security Breach**:
   - Verify firewall rules and ACLs are correctly applied.
   - Check for unauthorized access logs.
4. **Wireless Interference**:
   - Use tools like inSSIDer (free) to identify interference sources.
   - Consider changing wireless channels.

### Recommended Tool Stack:
- **Free Tools**:
  - VS Code (or Sublime Text)
  - Wireshark
  - GNS3
  - Lucidchart or draw.io for network diagrams
  - Nagios Core, Zabbix
  - OpenVAS
- **Paid/Optional Alternatives**:
  - PRTG Network Monitor ($149 trial available)
  - SolarWinds Network Performance Manager (optional)

### Realistic Timeline:
1. **Planning and Design**: 2 weeks
2. **Implementation**: 3-4 weeks, depending on network size.
3. **Testing**: 1 week
4. **Documentation and Training**: 1 week
5. **Monitoring Setup**: Ongoing

**Total Estimated Time**: Approximately 6-8 weeks for a medium-sized network configuration.

### Best Practices and AI Integration (2024-2025):
- **Automation**: Integrate Network Configuration Management Automation (NCMA) tools like Ansible or Puppet to streamline processes.
- **AI-Powered Monitoring**: Utilize AI-driven monitoring solutions that can predict failures and suggest optimizations based on historical data.
- **Continuous Learning**: Use platforms like Coursera, Udemy, or free resources on edX for staying updated with the latest network technologies and security practices.

By following this comprehensive template, a Computer Technician can effectively configure networks while leveraging both traditional tools and emerging AI-integrated solutions to ensure robust performance, security, and scalability.

