#!/usr/bin/python3

import subprocess
import cgi

print("content-type: text/html")
print()
# To differentiate between header and body...



f = cgi.FieldStorage()
cmd = f.getvalue('x')

# convert "cmd" in lower case
cmd = cmd.lower()

#if else code to convert english into docker command....
if ( ("run" in cmd) and ("docker" in cmd) and ( ("os" in cmd) or ("container" in cmd) ) ):
    output = subprocess.getoutput( "sudo  " + "docker run -t --name apniImage centos:latest")
    print(output)
elif ( ("container" in cmd) and ("docker" in cmd) or ( ("os" in cmd) or ("container" in cmd) ) ):
    output = subprocess.getoutput( "sudo  " + "docker ps")
    print(output)





"""
1. systemctl stop firefox
2. systemctl start docker
3. systemctl start httpd
4. setenforce 0 (stop selinux)
4. vim /etc/group (set apache id to 0)
5. vim /etc/sudoers (set apache ALL=(ALL) NOPASSWD: ALL)


"""
