# HTB Backdoor
# Linux
# Difficulty: Easy <<< actually hard imo

### Synopsis:
Backdoor starts by finding a WordPress plugin with a directory traversal bug that allows me to read files from the filesystem. I’ll use that to read within the /proc directory and identify a previously unknown listening port as gdbserver, which I’ll then exploit to get a shell. To get to root, I’ll join a screen session running as root in multiuser mode. ~0xdf

### Skill-set:
1. WordPress Local File Inclusion Vulnerability (LFI) 
2. LFI to RCE (Abusing /proc/PID/cmdline) Gdbserver RCE Vulnerability 
3. Abusing Screen (Privilege Escalation) [Session synchronization]
