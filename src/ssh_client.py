#!/usr/bin/env python
# coding: utf-8

import getopt, sys
import pexpect

def ssh_cmd(ip, user, passwd, cmd):
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
    r = ''
    try:
        i = ssh.expect(['password: ', 'continue connecting (yes/no)?'])
        if i == 0 :
			ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes')
    except pexpect.EOF:
        ssh.close()
    else:
        r = ssh.read()
        ssh.expect(pexpect.EOF)
        ssh.close()
        r = "success"+r
    return r

ip = '192.168.1.200'
port = '-p22 '
user = 'ptp'
passwd = '123456'

login = ''
cmd = 'python shell/ssh.py '
if len(sys.argv) > 0: login = sys.argv[1] 
if len(sys.argv) == 3 and 'root' == login: 
	cmd = cmd + login +" "+ sys.argv[2]
if len(sys.argv) == 4 and 'ison' == login:
	cmd = cmd + login +" "+ sys.argv[2] + " " + sys.argv[3]

print ssh_cmd(ip, port+user, passwd, cmd) 



