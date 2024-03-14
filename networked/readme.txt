# Another very fun box from HTB Networked
1. File inclusion 
2. Payload injection into jpeg image. Only way to avoid this is to not allow image upload and or use a WAP.
3. Badly coded bash script with sudo -l privilege allows for the execution of check_attack.php to executed by guly in an insecure way. If bash is passed to command and run with sudo. Bash will be executed as root.
4. Abusing weak filtering
