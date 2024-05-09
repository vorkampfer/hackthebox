# HTB Broker
# Linux
# Difficulty: Easy

### Synopsis:
Broken is another box released by HackTheBox directly into the non-competitive queue to highlight a big deal vulnerability that’s happening right now. ActiveMQ is a Java-based message queue broker that is very common, and CVE-2023-46604 is an unauthenticated remote code execution vulnerability in ActiveMQ that got the rare 10.0 CVSS imact rating. I’ll exploit this vulnerability to get a foothold, and then escalate to root abusing the right to run nginx as root. I’ll stand up a rogue server to get file read. Then I’ll add PUT capabilities and write an SSH key for root. I’ll also show a method that was used to exploit a similar Zimbra miconfiguration (CVE-2022-41347). In this case, I’ll poison the LD preload file by running nginx with its error logs pointing at that file, and then load a malicious shared object. ~0xdf

### Skill-set:
1. Credential guessing
2. ActiveMQ Exploitation - Deserialization Attack CVE-2023-46604 [RCE]
3. Abusing Sudoers privilege (nginx) [Privilege Escalation]
