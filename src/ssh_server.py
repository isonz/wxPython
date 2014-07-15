#!/usr/bin/env python
# coding: utf-8

#use : python ssh.py ison dev.skin.ptp.cn dev/skin.ptp.cn
#use : python ssh.py root stop

import getopt, sys, time, os
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
		r = "ok" + r
	return r

ip = '127.0.0.1'
port = '-p22 '
user = sys.argv[1]
cmds = "ls /tmp"

if 'root'==user : 
	passwd='123456'
	type = sys.argv[2]
	if 'stop' == type:
		cmds = "/etc/init.d/tomcat stop"
	elif 'backup' == type:
		if os.path.isfile('/opt/tomcat/webapps/ROOT.war'): cmds = "mv /opt/tomcat/webapps/ROOT.war /wdata/webBak/java/ROOT.war."+time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
	elif 'build' == type:
		if os.path.isfile('/www/ftp/sso.war'): cmds = "mv /www/ftp/sso.war /opt/tomcat/webapps/ROOT.war && rm -rf /opt/tomcat/webapps/ROOT"
	elif 'start' == type:
		cmds = "/etc/init.d/tomcat start"
	else:
		cmds = "/etc/init.d/tomcat restart"

if 'ison'==user : 
	passwd='123456'
	site = sys.argv[2]
	dir = site
	if len(sys.argv) >=4 : dir = sys.argv[3]
	cmds = "cd /www/"+dir+" && git pull origin master"
 
for cmd in cmds.split(","):
	print ssh_cmd(ip, port+user, passwd, cmd) 



