#!/usr/bin/env bash
# Script to enumerate the ports on HTB Goodgames
# There are 65535 ports

function ctrl_c(){
    echo -e "\n\n${redColour}[+] ${endColour} ${yellowColour}Exiting the function...${endColour}\n"
    tput cnorm; exit 1
}

# CTRL + c
trap ctrl_c INT

# Colors
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

tput civis
for port in $(seq 1 1000); do
    timeout 1 bash -c "echo '' > /dev/tcp/172.19.0.1/$port" 2>/dev/null && echo "[+] Port $port - Open" &
done; wait
tput cnorm