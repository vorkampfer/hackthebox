# HTB Goodgames
# Linux
# Difficulty: Easy

### Synopsis:
GoodGames has some basic web vulnerabilities. First there’s a SQL injection that allows for both a login bypass and union injection to dump data. The admin’s page shows a new virtualhost, which, after authing with creds from the database, has a server-side template injection vulnerability in the name in the profile, which allows for coded execution and a shell in a docker container. From that container, I’ll find the same password reused by a user on the host, and SSH to get access. On the host, I’ll abuse the home directory that’s mounted into the container and the way Linux does file permissions and ownership to get a shell as root on the host. ~0xdf

### Skill-set:
1. SQLI (Error Based)
2. Hash Cracking Weak Algorithms
3. Password Reuse
4. Server Side Template Injection (SSTI)
5. Docker Breakout (Privilege Escalation) 
6.[PIVOTING]
