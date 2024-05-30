# HTB DevVortex
# Linux
# Difficulty: Easy

### Synopsis:
DevVortex starts with a Joomla server vulnerable to an information disclosure vulnerability. I’ll leak the users list as well as the database connection password, and use that to get access to the admin panel. Inside the admin panel, I’ll show how to get execution both by modifying a template and by writing a webshell plugin. I’ll pivot to the next user after cracking their hash from the DB. For root, I’ll abuse a pager vulnerability in apport-cli that allows escaping to a root shell when run with sudo. ~0xdf

### Skill-set:
1. Subdomain Enumeration
2. Enumeration and abusing Joomla
3. Joomla exploit (CVE-2023-23752)
4. Customizing administration template to achieve RCE
5. Database Enumeration + User Pivoting
6. Abusing sudoers privilege (apport-cli) [Privilege Escalation to Root]
