
# HTB Previse
# Linux Easy
### Synopsis:
Previse is a easy machine that showcases Execution After Redirect (EAR) which allows users to retrieve the contents and make requests to `accounts.php` whilst unauthenticated which leads to abusing PHP `exec()` function since user inputs are not sanitized allowing remote code execution against the target, after gaining a www-data shell privilege escalation starts with the retrieval and cracking of a custom MD5Crypt hash which consists of a unicode salt and once cracked allows users to gain SSH access to the target then abusing a sudo executable script which does not include absolute paths of the functions it utilises which allows users to perform PATH hijacking on the target to compromise the machine. ~HTB
