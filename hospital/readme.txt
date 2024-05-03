# HTB Hospital
# Windows
# Difficulty: Medium

### Synopsis:
Hospital is a Windows box with an Ubuntu VM running the company webserver. I’ll bypass upload filters and disable functions to get a PHP webshell in the VM and execution. I’ll escalate using kernel exploits, showing both CVE-2023-35001 and GameOver(lay). As root on the webserver, I’ll crack the password hashes for a user, and get credentials that are also good on the Windows host and the RoundCube webmail. In the mail, I’ll reply to another user who is waiting for a EPS file to exploit a vulnerability in Ghostscript and get execution. To escalate, I’ll show four ways, including the intended path which involves using a keylogger to get the user typing the admin password into RoundCube. In Beyond Root, I’ll look at the automations for the Ghostscript phishing step. ~0xdf

### Skill-set:
1. SMB Enumeration
2. Abusing File Upload (.phar extension + Python Scripting ) <<< Three versions of the same python script. The 3rd version is the essential one.
3. Abusing PHP Disable_Functions in order to RCE
4. GamerOver(lay) Exploitation (Privilege Escalation)
5. Cracking Hashes
6. Enumerating domain users (rpcclient)
7. Testing ASREP Roastable Accounts (GetNPUsers)
8. Fraudulent sending of eps file by mail through RoundCube Framework
9. Abusing XAMPP for final privilege escalation to root.
