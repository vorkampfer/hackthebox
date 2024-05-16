# HTB Antique
# Linux
# Difficulty: Easy

1. I get stuck on enumerating SNMP until I figure out that the response is in hexidecimal. Which can be easily decoded. Overall, I would give this 5 stars. I really enjoyed this box.

### Synopsis:
Antique released non-competitively as part of HackTheBox’s Printer track. It’s a box simulating an old HP printer. I’ll start by leaking a password over SNMP, and then use that over telnet to connect to the printer, where there’s an exec command to run commands on the system. To escalate, I’ll abuse an old instance of CUPS print manager software to get file read as root, and get the root flag. In Beyond Root, I’ll look at two more CVEs, another CUPS one that didn’t work because no actual printers were attached, and PwnKit, which does work. ~0xdf

### Skill-set:
1. SNMP Enumeration
2. Network Printer Abuse
3. CUPS Administration Exploitation (ErrorLog)
4. EXTRA -> (DirtyPipe) [CVE-2022-0847]
