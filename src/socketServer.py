#!/usr/bin/env python
# coding: utf-8

import os
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
			buf = connection.recv(1024)
			bufs = buf.split("|")
			for bf in bufs:
				host,dir= bf.split(",")
				tmp = os.popen('python ssh.py '+host+ ' ' +dir).readlines()
				connection.send(str(tmp))
		except socket.timeout:  
			print 'time out'  
		connection.close()


