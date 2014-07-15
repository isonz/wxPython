#!/usr/bin/env python
# coding: utf-8

import os
import time 
from socket import *
import socket


if __name__ == '__main__':  
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	sock.bind(('0.0.0.0', 8001))  
	sock.listen(5)  
	while True:  
		connection,address = sock.accept()  
		try:  
			connection.settimeout(5)  
			buf = connection.recv(10024)
			bufs = buf.split("|")
			user  = ''
			tmp = ''

			if len(bufs)>0 : user  = bufs[0]
			if 'root' == user and len(bufs)>1:
				tmp = str(os.popen('python ssh.py root '+bufs[1]).readlines())
			else:
				#bufs.pop(0)
				for bf in bufs:
					host,dir= bf.split(",")
					tmp = tmp + str(os.popen('python ssh.py ison '+host+ ' ' +dir).readlines())
					#time.sleep(10)
			if tmp: 
				connection.send(tmp)
			else:
				print 'No command(s)'
		except socket.timeout:  
			print 'time out'  
		connection.close()


