#!/bin/bash
# This decryptor is for HTB Hawk, but can be used as a general purpose file decryptor with some mods.
function ctrl_c(){
    echo -e "\n\n${redColour}[+]${endColour} ${yellowColour}Exiting the function...${endColour}\n"
    tput cnorm; exit 1
}

# Ctrl+C
trap ctrl_c SIGINT

# Global Variables

# Colors
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"



# for cipher in ${cipher_modes[@]}; do
#     echo "[+] Trying with encryption algorithm: $cipher"
# done
tput civis
for password in $(cat /home/shadow42/hax0r1if3/servmon/passwdlst.lst); do 
    openssl aes-256-cbc -d -in drupal.enc -out drupal.decrypted -pass:$password &>/dev/null

    if [ "$(echo $?)" == "0" ]; then
        echo -e "\n[+] The password is $password\n"
        exit 0
    fi
done
tput cnorm

# /home/shadow42/hax0r1if3/hawk/drupal.enc
