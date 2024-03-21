# HTB Traverxec
### Linux Easy

### Synopsis:
Traverxec is an easy Linux machine that features a Nostromo Web Server, which is vulnerable to Remote Code Execution (RCE). 
The Web server configuration files lead us to SSH credentials, which allow us to move laterally to the user `david`. A bash 
script in the user&amp;amp;#039;s home directory reveals that the user can execute `journalctl` as root. This is exploited 
to spawn a `root` shell. 

### Skillset
1. Nostromo Exploitation
2. Abusing Nostromo HomeDirs Configuration
3. Exploiting Journalctl (Privilege Escalation)
