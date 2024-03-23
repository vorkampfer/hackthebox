# HTB Shocker <<< on TJ Null's List
### Linux Easy
*This is probrably one of the easiest boxes on TJ Null's List. Below is a synopsis by 0xdf on this box.

The name Shocker gives away pretty quickly what I’ll need to do on this box. There were a couple things to look out for along the way. First, I’ll need to be careful when directory brute forcing, as the server is misconfigured in that the cgi-bin directory doesn’t show up without a trailing slash. This means that tools like gobuster and feroxbuster miss it in their default state. I’ll show both manually exploiting ShellShock and using the nmap script to identify it is vulnerable. Root is a simple GTFObin in perl. In Beyond Root, I’ll look at the Apache config and go down a rabbit hole looking at what commands cause execution to stop in ShellShock and try to show how I experimented to come up with a theory that seems to explain what’s happening. ~0xdf

# Skillset:
1. ShellShock Attack (User-Agent)
2. Abusing Sudoers Privilege (Perl)
3. EXTRA: We create our own CTF in Docker that demos the ShellShock exploit.
