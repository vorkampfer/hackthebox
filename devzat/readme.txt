# HTB DevZat
# Linux
# Difficulty: Medium

## Devzat was a really fun box. I recommend it. A-lot of fuzzing. I fixed and rsa-ssh error. I added 2 lines to the ssh_config file to fix that. I also ran into an error when copying over the id_rsa. I used a cut command that I thought cleaned it up but then had to manually clean up the file using vim.

### Synopsis:
Devzat is centered around a chat over SSH tool called Devzat. To start, I can connect, but there is at least one username I can’t access. I’ll find a pet-themed site on a virtual host, and find it has an exposed git repository. Looking at the code shows file read / directory traversal and command injection vulnerabilities. I’ll use the command injection to get a shell. From localhost, I can access the chat for the first user, where there’s history showing another user telling them about an influxdb instance. I’ll find an auth bypass exploit to read the db, and get the next user’s password. This user has access to the source for a new version of Devzat. Analysis of this version shows a new command, complete with a file read vulnerability that I’ll use to read root’s private key and get a shell over SSH. ~0xdf

### Skill-set:
1. Fuzzing Directory .git (GIT Project Recomposition)
2. Web Injection (RCE)
3. Abusing InfluxDB (CVE-2019-20933)
4. Abusing Devzat Chat /file command (Privilege Escalation)
