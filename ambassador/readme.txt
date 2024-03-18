# HTB Ambassador
### Linux Medium
### Objectives:

Ambassador starts off with a Grafana instance. I’ll exploit a directory traversal / file 
read vulnerability to read the config and get the password for the admin. From the Grafana 
admin panel, I’ll get creds to the MySQL instance. Logging into that leaks credentials for 
a developer and I can get a shell with SSH. This developer has access to a git repo that 
leaks a token used for Consul in an old commit. I’ll use that to interact with Consul 
and get execution as root. We only hack manually here. This is a no metasploit zone.
