#!/usr/bin/python
#coding=utf-8

import os,re
import socket

command_idc_ip = "'{ print $2 }' | awk '{ print $1 }' | sed -n '/^172/p'"
get_idc_ip = os.popen('netstat -ie  | grep "inet addr:" | awk -F ":" %s' % (command_idc_ip)).read().split('\n')[:-1]

str_idc_ip = ''.join(get_idc_ip)

def process_status(pr_name):

	ip_process = {}
	
	if os.system('ps -ef | grep "%s" |grep -v grep > /dev/null' % pr_name) == 0:
		ip_process[pr_name] = 'runing'
	else:
		ip_process[pr_name] = 'stop'

	return ip_process

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

def port_status(port):
	ip_port = {}
	
	if IsOpen(str_idc_ip,port) == True:
		ip_port[port] = 'open'
	else:
		ip_port[port] = 'down'
	
	return ip_port

def conf():
	pr_port = {}
	
	for line in open('../etc/process_and_port.conf'):
		if not line.startswith('#'):
			if re.findall('^\w+\s+\d+',line):
				lines = line.split()
				pr_port[lines[0]] = lines[1]
	return pr_port

def process_port():
	ip_process_port = {}
	for k,v in conf().items():
		ip_process_port[k] = port_status(v),process_status(k)
		#print ip_process_port
		#print port_status(v),process_status(k)
	
	return ip_process_port

if __name__ == '__main__':
	#print conf()
	print process_port()
	#for k,v in process_port().items():
	#	for x,y in v[0].items():
	#		print '%s == %s' %(k,x)
	#		print '%s == %s' %(k,y)
	#	for a,b in v[1].items():
	#		print '%s == %s' %(k,a)
	#		print '%s == %s' %(k,b)
	#print process_port()
	


