# HTB NunChucks
# Linux
# Difficulty: Easy

### Synopsis:
October’s UHC qualifying box, Nunchucks, starts with a template injection vulnerability in an Express JavaScript application. There are a lot of templating engines that Express can use, but this one is using Nunchucks. After getting a shell, there’s what looks like a simple GTFObins privesc, as the Perl binary has the setuid capability. However, AppArmor is blocking the simple exploitation, and will need to be bypassed to get a root shell. ~0xdf

### Skill-set:
1. NodeJS SSTI (Server Side Template Injection)
2. AppArmor Profile Bypass (Privilege Escalation)
