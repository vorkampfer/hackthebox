# HTB Manager
# Windows
# Difficulty: Medium

### NOTE: Everything was going great up to the PrivESC using certipy. When I went to authenticte with the administrator.pfx file I got the famous `clock-skew is too great error`. I try several apps including ntpdate to sync my time with the server to no avail. I end up learning how to sync the time manually using timedatectl.

### Synopsis:
Manager starts with a RID cycle or Kerberos brute force to find users on the domain, and then a password spray using each user’s username as their password. When the operator account hits, I’ll get access to the MSSQL database instance, and use the xp_dirtree feature to explore the file system. I’ll find a backup archive of the webserver, including an old config file with creds for a user. As that user, I’ll get access to the ADCS instance and exploit the ESC7 misconfiguration to get access as administrator. ~0xdf

### Skill-set:
1. SMB Enumeration
2. User enumeration [1st way] RID Cycling Attack (rpcclient)
3. User enumeration [2nd way] RID Cycling Attack (CrackMapExec)
4. User enumeration [3rd way] Kerberos User Enumeration (Kerberos)
5. LDAP Enumeration (ldapdomaindump)
6. Credentials Brute Force (CrackMapExec)
7. MSSQL Enumeration (mssqlclient.py) [Impacket framework]
8. Abusing MSSQL (xp_dirtree)
9. Information leakage
10. Abusing WinRM to get an interactive console
11. DC Enumeration (ADpeas) - Powershell tool to automate AD enumeration
12. Abusing Active Directory Certificate Services (ADCS)
13. ESC7 Exploitation case with certipy [Privilege Escalation to NT Authority]
