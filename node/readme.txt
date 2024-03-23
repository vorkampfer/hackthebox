# HTB Node
### Linux
### Difficulty: Medium

### Synopsis:
Node is about enumerating a Express NodeJS application to find an API endpoint that shares too much data., including user password hashes. 
To root the box, there’s a simple return to libc buffer overflow exploit. I had some fun finding three other ways to get the root flag, 
as well as one that didn’t work out. ~0xdf

### Skill-set:
1. Information Leakage
2. API Enumeration
3. Cracking Hashes
4. Cracking ZIP file
5. Backup Download - Stored credentials
6. MongoDB Enumeration
7. Mongo Task Injection - Command Injection [User Pivoting]
8. SUID Backup Binary Exploitation - Dynamic Analysis (1st way)
9. SUID Backup Binary Exploitation - Buffer Overflow 32 bits [NX Bypass + ASLR / Ret2libc] (2nd way)
