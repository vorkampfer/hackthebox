# HTB Horizontall
# Linux Easy

### Synopsis:
Horizonatll was built around vulnerabilities in two web frameworks. First there’s discovering an instance of strapi, where I’ll abuse a CVE to reset the administrator’s password, and then use an authenticated command injection vulnerability to get a shell. With a foldhold on the box, I’ll examine a dev instance of Laravel running only on localhost, and manage to crash it and leak the secrets. From there, I can do a deserialization attack to get execution as root. In Beyond Root, I’ll dig a bit deeper on the strapi CVEs and how they were patched. ~0xdf

### Skill-set:
1. Information Leakage
2. Port Forwarding
3. Strapi CMS Exploitation
4. Laravel Exploitation
