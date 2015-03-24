#!/usr/bin/python
#coding=utf-8

import os
def getAllitems(host, oid):
        sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')
        return sn1
                                                                     
def getload(host,loid):
        load_oids = '1.3.6.1.4.1.2021.10.1.3.' + str(loid)
        return getAllitems(host,load_oids)[0].split(':')[3]

def load_collect():
        hosts = ['127.0.0.1']
	load_data = {}

        #check_system_load
	for host in hosts:	
		load_data['load(1min)'] = int(float(getload(host, 1)))
		load_data['load(5min)'] = int(float(getload(host, 2)))
		load_data['load(15min)'] = int(float(getload(host, 3)))

	return load_data
                                                                     
#if __name__ == '__main__':
#        hosts = ['127.0.0.1']
        #check_system_load
#        print '==============System Load=============='
#        for host in hosts:
#                load1 = getload(host, 1)
#                load10 = getload(host, 2)
#                load15 = getload(host, 3)
#                print '%s load(1min): %s ,load(10min): %s ,load(15min): %s' % (host,load1,load10,load15)
