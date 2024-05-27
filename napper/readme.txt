# HTB Napper
# Windows
# Difficulty: Hard

### Note: The coding part was the hardest part of this box.

### Synopsis:
 Napper presents two interesting coding challenges wrapping in a story of real malware and a custom LAPS alternative. I’ll start by finding a username and password in a blog post, and using it to get access to an internal blog. This blog talks about a real IIS backdoor, Naplistener, and mentions running it locally. I’ll find it on Napper, and write a custom .NET binary that will run when passed to the backdoor to get a shell. On the box, I’ll find a draft blog post about a new internally developed solution to replace LAPS, which stores the password in a local Elastic Search DB. I’ll write a Go program to fetch the seed and the encrypted blob, generate the key from the seed, and use the key to decrypt the blob, resulting in the password for a user with admin access. I’ll use RunasCs.exe to bypass UAC and get a shell with administrator privileges. In Beyond Root, I’ll explore the automations for the box, including the both how the password is rotated every 5 minutes, and what changes are made to the real malware for HTB ~0xdf

### Skill-set:
1. IIS Web Server Enumeration
2. Subdomain Enumeration
3. Information Leakage 
4. Abusing NAPLISTENER BackDoor
5. Creating a reverse shell payload in C#
6. Creating an executable from C# code with mcs
7. Elasticsearch Enumeration
8. Binary Analysis with GHIDRA
9. Creation of script in GO-Lang <<< The code along with S4vitar was amazing.
10. Using script to decrypt a message
11. Abusing seed phrase [Privilege Escalation to Root]
