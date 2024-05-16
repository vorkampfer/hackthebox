# HTB SteamCloud
# Linux 
# Difficulty: Easy "Note: I would rate this to a medium or hard if you had not been exposed to Kubernetes before."

### Synopsis:
>>> Note: There was a-lot of kubernetes terminology I had to look up on this box. Which turned out to be very interesting putting it all together.
--------------------------------------------------------------------------------------------------------
SteamCloud just presents a bunch of Kubernetes-related ports. Without a way to authenticate, I can’t do anything with the Kubernetes API. But I also have access to the Kubelet running on one of the nodes (which is the same host), and that gives access to the pods running on that node. I’ll get into one and get out the keys necessary to auth to the Kubernetes API. From there, I can spawn a new pod, mounting the host file system into it, and get full access to the host. I’ll eventually manage to turn that access into a shell as well. ~0xdf

### Skill-set:
1. Kubernetes API Enumeration (kubectl)
2. Kubelet API Enumeration (kubeletctl)
3. Command Execution through kubeletctl on the containers
4. Cluster Authentication (ca.crt/token files) with kubectl
5. Creating YAML file for POD creation
6. Executing commands on the new POD
7. Reverse Shell through YAML file while deploying the POD
