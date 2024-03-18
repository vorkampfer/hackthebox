# HTB Photobomb
### Linux Easy
### Objectives:

Difficulty: Easy
IP: 10.10.11.182
1. Synopsis
Photobomb was on the easy end of HackTheBox weekly machines. I’ll find credentials in a JavaScript file, 
and use those to get access to an image manipulation panel. There’s a command injection vulnerability in 
the panel, which I’ll use to get execution and a shell. For privesc, the user can run a script as root, 
and there are two ways to get execution from this. The first is a find command that is called without 
the full path. The second is abusing the disabled Bash builtin .
2. Skills Required
Enumeration
Source Code Analysis
Linux CLI Usage
3. Skills Learned
Command Injection
Exploiting UNIX PATH variables
Enumeration
