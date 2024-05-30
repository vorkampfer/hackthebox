# HTB Backend
# Linux
# Difficulty: Medium

### Synopsis:
Backend was all about enumerating and abusing an API, first to get access to the Swagger docs, then to get admin access, and then debug access. From there it allows execution of commands, which provides a shell on the box. To escalate to root, I’ll find a root password in the application logs where the user must have put in their password to the name field. ~0xdf

### Skill-set:
1. API Enumeration
2. Abusing API - Registering a new user
3. Abusing API - Loggin in as the created user
4. Enumerating FastAPI Endpoints through Docs
5. Abusing FastAPI - We managed to change the admin password.
6. Abusing FastAPI - We get the ability to read the files from the machine (Source Analysis)
7. Creating our own privilege JWT
8. Abusing FastAPI - We achieved remote command execution through the exec endpoint.
9. Information Leakage [Privilege Escalation to Root]
