
### Objectives:

>>>Outdated

1. Synopsis
Outdated is a Medium Difficulty Linux machine that features a foothold based on the Follina CVE of 2022.
The box further encompasses an Active Directory scenario, where we must pivot from domain user to
domain controller, using an array of tools to leverage the ADs configuration and adjacent edges to our
advantage. The final step includes taking advantage of Windows Server Update Services- WSUS and using its
poor configuration to compromise the domain controller.
>>> Official Objectives
2. Skills Required
Fundamentals of Active Directory
Rudimentary BloodHound setup
3. Skills Learned
Shadow Credentials method
Golden Ticket Attack
Navigating Active Directory
..........................................................
>>> Objectives covered in this walk-through
1. SMB Enumeration
2. Follina Exploitation (CVE-2022-30190) + Nishang PowerShell TCP Shell [Remote Code Execution]
3. SharpHound + BloodHound DC Enumeration
4. Abusing AddKeyCredentialLink Privilege [Invoke-Whisker.ps1 - Shadow Credentials]
5. Getting the users NTLM Hash with Rubeus
6. Abusing WinRM - EvilWinRM
7. Abusing WSUS Administrators Group
8. WSUS Exploitation - Creating a malicious patch for deployment [Privilege Escalation]
