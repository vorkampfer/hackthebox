# HTB Jarvis
Room.php is  only page that accepts user input, basic testing for SQL Injection
Using wfuzz  fuzz for special characters 
Showing several  to test for SQL Injection (subtraction and hex())
Examining the query structure. Finding the column that accepts string input.
union statements, into outfile, loadfile, SQL commands explained.
Extracting DBadmin hash and cracking it.
Using GROUP_CONCAT  allow us to return multiple rows within union
Extracting Mysql  then cracking MySQL (mode 300)
Another way  get the password, LOAD_FILE() to view PHP Source Code
PHPMyAdmin 4.8.0  (LFI + Tainted PHP Cookie)
Dropping a  via the PHPMyAdmin exploit
ALTERNATE Way  get Shell:Dropping a file from the SQL Injection
Examining the  Cookie to see what happened with the PHPMyAdmin stuff
Examing the  Script we can execute as pepper with sudo
We can  code with $() but theres bad characters, so drop a bash script to disk
Running find  look for setuid binaries, discover systemctl then check GTFO Bins
Copying our  Scripts out of /tmp then creating our malicious service

