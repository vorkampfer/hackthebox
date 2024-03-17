# Super easy Linux box
### Synopsis:
1. Mirai, is a piece-of-cake Linux OS machine on HackTheBox, runs on RaspberryPi 
device and has Pi-Hole application installed. The default username and password 
for the device are still active via SSH 'pi raspberry' . The user has sudo privileges 
for all which gave us a root shell 'sudo su' . There is a bit of a catch at the end.
I have to recover the deleted root flag from a usb drive '# strings /dev/sdb'.
