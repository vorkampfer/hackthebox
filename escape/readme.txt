# HTB Escape
Escape is a very Windows-centeric box focusing on MSSQL Server and Active Directory Certificate Services (ADCS). 
I’ll start by finding some MSSQL creds on an open file share. With those, I’ll use xp_dirtree to get a Net-NTLMv2
challenge/response and crack that to get the sql_svc password. That user has access to logs that contain the next
user’s creds. To get administrator, I’ll attack active directory certificate services, showing both certify and 
certipy. In Beyond Root, I’ll show an alternative vector using a silver ticket attack from the first user to get 
file read as administrator through MSSQL. ~0xdf
