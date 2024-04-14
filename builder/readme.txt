
# HTB Builder
### Linux
### Difficulty: Medium <<< I think it was actually a hard level box.

### Synopsis:
Builder is a neat box focused on a recent Jenkins vulnerability, CVE-2024-23897. It allows for partial file read and can lead to remote code execution. I’ll show how to exploit the vulnerability, explore methods to get the most of a file possible, find a password hash for the admin user and crack it to get access to Jenkins. From in Jenkins, I’ll find a saved SSH key and show three paths to recover it. First, dumping an encrypted version from the admin panel. Second, using it to SSH into the host and finding a copy there. And third by having the pipeline leak the key back to me. ~0xdf

### Skills
1.  Advisory 3314 (CVE-2024-23897), has a File Read vulnerability in the CLI.
2. Playing with Tshark
3. Lots of enumeration
4. I go through 3 different versions of this exploit before finding the right one. 
5. I use docker to pull the latest version of Jenkins, in order to see how it stores credentials
6. Extracting the  Hash for Jennifer and cracking it to get logged into Jenkins [hashcat hashmode 3200]
7. Showing Jenkins  Console, a fun way to get code execution on Jenkins. 
8. Advanced Enumeration >>> Finding the encoded ssh key. Go into  Credentials Store for Jenkins, discovering a SSH Key is there. In order to export the key you need to login as jennifer. Then open up the DOM inspector. Right click on the credential store page. Drill down until you find the base64 encoded key. Lastly, export it and then use the Script Console to decrypt it
9. Log in as ssh root.
