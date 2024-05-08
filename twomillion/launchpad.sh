#!/bin/bash

# simple script to automate finding the launchpad OS version. For example Focal, jammy, Xenial, Buster, Bionic etc...
# Keep in mind even looking this up manually we can get the wrong OS version information because
# the server may be in a container or it may say it is a Jammy and it really is a Focal etc...
# This is grepping the output of an NMAP port scan. You provide the path,
# NOTE: It requires ddgr and html2text to be installed.
# NOTE: This script will only work on UBUNTU or DEBIAN servers
# NOTE: This is using the nmap output of -oN nmap/path/to/file.nmap. Some people like using -oG. I do not think it matters.
# Does not matter what extension your nmap file has. Does not need one.
# If you are planning on using this script a-lot of the time then you might want to
# hardcode the path to your nmap output file.
# if [ "$val1" == "$val2" ]; then <<< If you get an error with the curly brackets just remove them for variables val1 and val2.


function ctrl_c(){
    echo -e "\n\n${redColour}[+] Exiting the function...${endColour}\n"
    exit 1
}

# Ctrl+C
trap ctrl_c SIGINT

# Colors
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"




if [ -z "$1" ]; then
    /usr/bin/python2.7 /home/shadow42/python_projects/launchpad_banner.py
    echo -e "${redColour}Usage:${endColour} ${greenColour}./launchpad.sh${endColour} ${yellowColour}run${endColour}"
    exit 1
fi

read -p "Enter the path of your nmap scan output file: " mypath
#echo "The path is : $mypath"
sleep 2

# Global Variables
launchpad=$(cat $mypath | grep -i openssh | awk '{print $2}' FS="ack" | sed 's/^[ \t]*//' | cut -d'(' -f1)
myurl=$(cat ~/Documents/launchpad_url.txt)
val1=$(cat $mypath | grep -i openssh | cut -c 1-2)
val2=22

if [ "${val1}" == "${val2}" ]; then 
    echo ""
else
    echo -e "${redColour}ERROR: ${endColour} ${grayColour}There is no port 22 OpenSSH found in the nmap scan provided. Quitting! ${endColour}"
    exit 1
fi

sleep 2

if [ "${1}" = 'run' ]; then
    echo
    /usr/bin/ddgr -x $launchpad --np 2>/dev/null | grep -i "launchpad.net" | awk '!($3="")' | sed '/^[[:space:]]*$/d' | awk 'FNR == 1 {print}' | grep -oP 'https://\K\S+' > ~/Documents/launchpad_url.txt
    sleep 2
    echo -e "${greenColour}==> [+] ${endColour} ${blueColour}Here is the launchpad OS version ${endColour}"
    /usr/bin/curl -s https://$myurl | html2text | grep -A4 "## Changelog" | grep open | sed 's/^[ \t]*//'
    echo
    echo -e "${grayColour}==> [+] ${endColour} ${blueColour}Here is the Launchpad url it was scrapped from. ${endColour}"
    echo "https://$myurl"
else
    echo -e "${redColour}==>[!] ${endColour} ${blueColour} Something went wrong. Make sure to supply a valid path. Is port 22 open? ${endColour}" >&2
    exit 1
fi

