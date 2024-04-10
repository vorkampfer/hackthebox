
# HTB Academy
# Linux Easy
### Synopsis:
HackTheBox releases a new training product, Academy, in the most HackTheBox way possible - By putting out a vulnerable version of it to hack on. There’s a website with a vulnerable registration page that allows me to register as admin and get access to a status dashboard. There I find a new virtual host, which is crashing, revealing a Laravel crash with data including the APP_KEY. I can use that to create a serialized payload to submit as an HTTP header or cookie to get execution. From there, I’ll reuse database creds to get to the next user, and then find more creds in auth logs, and finally get root with sudo composer. ~0xdf
