# HTB OpenAdmin
# Linux
# Difficulty: Easy

### Synopsis:
OpenAdmin provided a straight forward easy box. There’s some enumeration to find an instance of OpenNetAdmin, which has a remote coded execution exploit that I’ll use to get a shell as www-data. The database credentials are reused by one of the users. Next I’ll pivot to the second user via an internal website which I can either get code execution on or bypass the login to get an SSH key. Finally, for root, there’s a sudo on nano that allows me to get a root shell using GTFObins. ~0xdf

### Skill-set:
1. Basic Enumeration
2. Basic Pivoting
3. Abusing SUID privileges
