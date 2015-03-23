#!/usr/bin/python
#coding=utf-8

import os
import re

def ping_collect():
	ping_data = {}
	host_list = []
        ip_list = open('../etc/ping_ip.conf')

        for line in ip_list.readlines():
		if not line.startswith('#'):
			if re.findall('^\d+.\d+.\d+.\d+',line):
                		host_list.append(line.strip('\n'))

	#print host_list

	for ip in host_list:
		if os.system('ping -c2 -W 1 %s > /dev/null 2>&1' % ip) == 0:
			ping_data[ip] = 'ok'
		else:
			ping_data[ip] = 'timeout'

	return ping_data	

#if __name__ == '__main__':
	#print ping_collect()
