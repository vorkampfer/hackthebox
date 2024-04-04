# HTB Calamity
### Linux
### Hard
1. There are 2 actually 3 coding projects from this one box.
2. There is a fake_shell.sh, an autopwnV1.py and an autopwn_upgraded.py.
3. The fake_shell.sh and autopwn_part1.py work great. 
4. The autopwn_part2.py works but you need to mess with it.
5. The stenography portion of this box was a-lot of fun.

Calamity was released as Insane, but looking at the user ratings, it looked more like an easy/medium box. The user path to through the box was relatively easy. Some basic enumeration gives access to a page that will run arbitrary PHP, which provides execution and a shell. There’s an audio steg challenge to get the user password and a user shell. People likely rated the box because there was an unintended root using lxd. I’ve done that before, and won’t show it here. The intended path was a contrived but interesting pwn challenge that involved three stages of input, the first two exploiting a very short buffer overflow to get access to a longer buffer overflow and eventually a root shell. In Beyond Root, I’ll look at some more features of the source code for the final binary to figure out what some assembly did, and why a simple return to libc attack didn’t work. ~0xdf
