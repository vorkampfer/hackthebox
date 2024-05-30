# HTB Bizness
# Linux
# Difficulty: Easy

### Synopsis:
1. This is a detailed walkthrough of “Bizness” machine on HackTheBox platform that is based on Linux operating system and categorized as “Easy” by difficulty (in reality, HtB staff has their own understading of difficulty levels, so this one can’t be defined as “Easy” in the literal sense of the word!). The machine involves exploitation of CVE-2023-49070 - “Authentication Bypass Vulnerability in Apache OfBiz”. ~HTB

2. HTB wrote that this box `can not be defined as easy`. I definitely agree. This box was not easy. Should be rated medium. The concept was easy but finding the hash and decrypting it was more of a medium to hard level of difficulty.

3. Bizness is all about an Apache OFBiz server that is vulnerable to CVE-2023-49070. I’ll exploit this pre-authentication remote code execution CVE to get a shell. To esclate, I’ll find the Apache Derby database and exfil it to my machine. I’ll show how to enumerate it using the ij command line too, as well as DBeaver. Once I find the hash, I’ll need to reformat it to something hashcat can process, crack it, and get root. ~0xdf

### Skill-set:
1. Apache OFBiz Exploitation (Authentication Bypass)
2. Analysis of OFBiz code to understand the hashed storage mechanism
3. Adapting found hashes to a crackable format
4. Cracking Hashes [Privilege Escalation]
