#!/usr/bin/env python
# coding: utf-8
# client code

#import os
import socket
#import time 

if __name__ == '__main__':  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(('192.168.77.200', 8001))
        #time.sleep(2)  
        sock.send('skin.ptp.cn,dev/skin.ptp.cn')  
        bufs = sock.recv(1024)
        i=0
        for buf in bufs.split(","):
            i=i+1
            if 3>=i: continue
            print buf.replace('\\r\\n', '').replace('\\n', '').replace('\'', '').replace('[', '').replace(']', '')
            #os._exit(0)
    except socket.error, arg:
        (errno, err_msg) = arg
        print "Connect server failed: %s, errno=%d" % (err_msg, errno)
    sock.close()  