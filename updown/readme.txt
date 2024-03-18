## HTB UpDown
### Linux Medium
Synopsis:

1. UpDown is a medium difficulty Linux machine with SSH and Apache servers exposed. 
On the Apache server a web application is featured that allows users to check if a 
webpage is up. A directory named `.git` is identified on the server and can be downloaded 
to reveal the source code of the `dev` subdomain running on the target, which can only 
be accessed with a special `HTTP` header. Furthermore, the subdomain allows files to be 
uploaded, leading to remote code execution using the `phar://` PHP wrapper. The Pivot 
consists of injecting code into a `SUID` `Python` script and obtaining a shell as the 
`developer` user, who may run `easy_install` with `Sudo`, without a password. This can 
be leveraged by creating a malicious python script and running `easy_install` on it, 
as the elevated privileges are not dropped, allowing us to maintain access as `root`.
2. A great machine for learning to manipulate PHP code. Also recommend to do the box 
'HTB Crimestopper'. It is like this box.
