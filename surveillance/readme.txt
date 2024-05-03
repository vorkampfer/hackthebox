# HTB Surveillance
# Linux
# Difficulty: Medium

### Synopsis:
Surveillance is one of those challenges that has gotten significantly easier since it’s initial release. It features vulnerabilities that had descriptions but not public POCs at the time it was created, which made for an interesting challenge. It starts with an instance of Craft CMS. I’ll exploit an arbitrary object injection vulnerability to get RCE and a shell. I’ll find a password hash for another user in a database backup and crack it. That user can log into a ZoneMinder instance running on localhost, and I’ll exploit a vulnerability in it to get access as the zoneminder user. For root, I’ll show two ways to abuse the zoneminder user’s sudo privileges - through the ZoneMinder LD_PRELOAD option, and via command injection in one of their scripts. ~0xdf

### Skill-set:
Skills: 
1. CraftCMS Exploitation (CVE-2023-41892) RCE
2. Information Leakage
3. Cracking Hashes
4. ZoneMinder + Sudoers Exploitation (Privilege Escalation)
