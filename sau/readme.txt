# HTB SAU
### Linux Easy
This is an easy-level linux machine that has a SSRF vulnerability in the request-basket application that requires you to utilize verb-tampering to upload a shell successfully. Once you have a shell on the box you need to exploit improperly set permissions on the systemctl binary to get root.
1. Requests-baskets 1.2.1 Exploitation (SSRF - Server Side Request Forgery)
2. Mailtrail 0.53 Exploitation (RCE - Username Injection)
3. Abusing sudoers privilege (systemctl) [Privilege Escalation]
