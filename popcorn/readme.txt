# HTB Popcorn
# Linux Medium Level Box
Synopsis:
Popcorn was a medium box that, while not on TJ Null’s list, felt very OSCP-like to me. 
Some enumeration will lead to a torrent hosting system, where I can upload, and, 
bypassing filters, get a PHP webshell to run. From there, I will exploit CVE-2010-0832, 
a vulnerability in the linux authentication system (PAM) where I can get it to make my 
current user the owner of any file on the system. There’s a slick exploit script, but 
I’ll show manually exploiting it as well. I’ll quickly also show DirtyCow since it does work here.
~0xdf
