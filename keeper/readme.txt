# HTB KEEPER
### LINUX, EASY

### Synopsis:
Keeper is a relatively simple box focused on a helpdesk running Request Tracker and with an admin using KeePass. I’ll use default creds to get into the RT instance and find creds for a user in their profile. That user is troubleshooting a KeePass issue with a memory dump. I’ll exploit CVE-2022-32784 to get the master password from the dump, which provides access to a root SSH key in Putty format. I’ll convert it to OpenSSH format and get root access. ~0xdf

### Skill-set:
1. Abusing request tracket
2. Information leakage
3. Obtaining KeePass password through memory dump [PrivESC]
