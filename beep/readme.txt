# HTB Beep
# Linux Easy

### Synopsis:
Even when it was released there were many ways to own Beep. I’ll show five, all of which were possible when this box was released in 2017. Looking a the timestamps on my notes, I completed Beep in August 2018, so this writeup will be a mix of those plus new explorations. The box is centered around PBX software. I’ll exploit an LFI, RCE, two different privescs, webmin, credential reuse, ShellShock, and webshell upload over SMTP. ~0xdf

### Skill-set:
1. Elastix 2.2.0 Exploitation - Local File Inclusion (LFI)
2. Information Leakage
3. Vtiger CRM Exploitation - Abusing File Upload (1st way) [RCE]
4. Shellshock Attack (2nd way) [RCE]
