#!/usr/bin/env python

import os
import socket

command_idc_ip = "'{ print $2 }' | awk '{ print $1 }' | sed -n '/^172/p'"
get_idc_ip = os.popen('netstat -ie  | grep "inet addr:" | awk -F ":" %s' % (command_idc_ip)).read().split('\n')[:-1]

str_idc_ip = ''.join(get_idc_ip)

def IsOpen(ip,port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
	    s.connect((ip,int(port)))
	    s.shutdown(2)
	    #print '%d is open' % port
	    return True
	except:
	    #print '%d is down' % port
	    return False

def port_collect():
	port_data = {}
        port_list = []
	port_conf = open('../etc/port_list.conf')

	for line in port_conf.readlines():
                port_list.append(line.strip('\n'))
	
	for port in port_list:
		if IsOpen(str_idc_ip,port) == True:
			port_data[port] = 'open'
		elif IsOpen('127.0.0.1',port) == False:
			port_data[port] = 'down'

	return port_data

#if __name__ == '__main__':
#	print open_collect()
