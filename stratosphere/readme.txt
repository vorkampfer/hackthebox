# HTB Stratosphere
# Linux
# Difficulty: Medium

### Synopsis:
Stratosphere is a super fun box, with an Apache Struts vulnerability that we can exploit to get single command execution, but not a legit full shell. I’ll use the Ippsec mkfifo pipe method to write my own shell. Then there’s a python script that looks like it will give us the root flag if we only crack some hashes. However, we actually have to exploit the script, to get a root shell. ~0xdf

### Skill-set:
1. Apache Struts Exploitation (CVE-2017-5638)
2. Dirtypipe exploit (privesc) attempted
3. Base64 encoding & decoding an exploit
4. Python Library Hijacking (Privilege Escalation)
