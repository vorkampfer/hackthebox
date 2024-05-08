#!/usr/bin/env python3

# Optional code-along for HTB TwoMillion. This is a mini-port scanner.
# Reason for the scanner is the box is too easy. So S4vitar did this code along to make the box more worth while.
# This python script may require sudo because of the try statement flags="S". 
# This is requesting a syn scan which drops the synack. Aka a stealth scan.

from pwn import *
from scapy.all import *
from termcolor import colored

import signal
import sys
import time
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def def_handler(sig, frame):
    print(colored(f"\n\n[!] Exiting...\n", 'red'))
    p1.failure("Scan aborted (Ctrl + c pressed)")
    sys.exit(1)

# CTRL + c
signal.signal(signal.SIGINT, def_handler)
p1 = log.progress("TCP SYN Scanner")
p1.status("Scanning ports...")

def scanPort(ip, port):
    src_port = RandShort()
    try:
        response = sr1(IP(dst=ip)/TCP(sport=src_port, dport=port, flags="S"), timeout=2, verbose=0)
        if response is None:
            return False
        elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
            send(IP(dst=ip)/TCP(sport=src_port, dport=port, flags="R"), verbose=0)
            return True
        else:
            return False
    except Exception as e:
        log.failure(f"Error scanning {ip} on port {port}: {e}")
        sys.exit(1)

def thread_function(ip, port):
    response = scanPort(ip, port)
    if response:
        log.info(f"Port {port} - OPEN")

def main(ip, ports, end_port):
    threads = []
    time.sleep(2)
    for port in ports:
        p1.status(f"Scan progress: [{port}/{end_port}]")
        
        thread = threading.Thread(target=thread_function, args=(ip, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


    p1.success("Scan completed")

if __name__ == '__main__':
    
    if len(sys.argv) !=3:
        print(colored(f"\n\n[!] Usage: {colored('python3', 'blue')} {colored(sys.argv[0], 'green')} {colored('<ip> <ports-range>', 'yellow')}\n", 'red'))
        sys.exit(1)

    target_ip = sys.argv[1]
    portRange = sys.argv[2].split("-")
    start_port = int(portRange[0])
    end_port = int(portRange[1])

    # print(start_port)
    # print(end_port)
    ports = range(start_port, end_port + 1)
    main(target_ip, ports, end_port)


