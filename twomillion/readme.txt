### Synopsis:
TwoMillion is a special release from HackTheBox to celebrate 2,000,000 HackTheBox members. It released directly to retired, so no points and no bloods, just for run. It features a website that looks like the original HackTheBox platform, including the original invite code challenge that needed to be solved in order to register. Once registered, I’ll enumerate the API to find an endpoint that allows me to become an administrator, and then find a command injection in another admin endpoint. I’ll use database creds to pivot to the next user, and a kernel exploit to get to root. In Beyond Root, I’ll look at another easter egg challenge with a thank you message, and a YouTube video exploring the webserver and it’s vulnerabilities ~0xdf

### Skill-set:
1. Building a Python3 Stealth port scanner with Scapy module.
2. Abusing delcared Javascript functions from teh browser console.
3. Abusing the API to generate a valid invite code.
4. Abusing the API to elevate our privilege to administrator.
5. Command Injection via poorly designed API functionality.
6. Information Leakage
7. Privilege Escalation via Kernel Exploitation (CVE-2023-0386) OverlayFS Vulnerability.
