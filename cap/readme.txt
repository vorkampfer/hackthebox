# HTB Cap
# Linux Easy

### Synopsis:
Cap provided a chance to exploit two simple yet interesting capabilities. First, there’s a website with an insecure direct object reference (IDOR) vulnerability, where the site will collect a PCAP for me, but I can also access other user’s PCAPs, to include one from the user of the box with their FTP credentials, which also provides SSH access as that user. With a shell, I’ll find that in order for the site to collect pcaps, it needs some privileges, which are provided via Linux capabilities, including one that I’ll abuse to get a shell as root. ~0xdf

### Skill-set:
1. Testing IDOR Vulnerability
2. Tshark analysis of the Downloaded pcap through the IDOR Vulnerability to find FTP Creds
3. SSHing into  box with the credentials from FTP
4. Enumeration using getcap to find that python3.8 has the ability to set SUID
5. Using the python console to open up a bash shell
