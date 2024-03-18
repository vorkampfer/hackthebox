# HTB Mentor
### Linux Medium

### Objectives:
1. Synopsis - Mentor is a medium difficulty Linux machine whose path includes pivoting through four different usersbefore arriving at root. After scanning an SNMP service with a community string that can be brute forced,plaintext credentials are discovered which are used for an API endpoint, which proves to be vulnerable toblind remote code execution and leads to a foothold on a docker container. Enumerating the containersnetwork reveals a PostgreSQL service on another container, which can be leveraged into RCE by authenticating using default credentials. Examining an old database backup on the PostgreSQL container
reveals a hash, which once cracked is used to SSH into the machine. Finally, by examining the configuration files on the host, the attacker is able to retrieve a password for user james , who is able run the /bin/sh command with sudo privileges, thereby instantly forfeiting root privileges.
2. Skills to be covered.
> Virtual Hosting
> Subdomain Enumeration
> API Enumeration
> ABUSING API
> SNMP Enumeration (snmp walk && snmpbulkwalk) + Community String Brute Force
> Information Leakage
> Abusing Jason Web Token (JWT)
> API Exploitation (Command Injection)
> Chisel Tunnel + Postgresql Service Enumeration + Information Leakage
> Abusing Sudoers Privilege (Privilege Escalation)
