# HTB Shoppy
# Linux Easy <<< actually more like hard

### Objectives:

Shoppy was one of the easier HackTheBox weekly machines to exploit, though identifying the exploits 
for the initial foothold could be a bit tricky. I’ll start by finding a website and use a NoSQL 
injection to bypass the admin login page, and another to dump users and hashes. With a cracked hash, 
I’ll log into a Mattermost server where I’ll find creds to the box that work for SSH. From there, 
I’ll need the lighest of reverse enginnering to get a static password from a binary, which gets me 
to the next user. This user is in the docker group, so I’ll load an image mounting the host file 
system, and get full disk access. I’ll show two ways to get a shell from that. In Beyond Root, a 
video walkthrough of the vulnerable web-server code, showing how the injections worked, and fixing 
them. ~0xdf
