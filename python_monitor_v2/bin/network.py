#!/usr/bin/python
#coding=utf-8

import re
import os
#get SNMP-MIB2 of the devices
def getAllitems(host,oid):
        sn1 = os.popen('snmpwalk -v 2c -c 360buy ' + host + ' ' + oid).read().split('\n')[:-1]
        return sn1
                                                                                          
#get network device
def getDevices(host):
        device_mib = getAllitems(host,'RFC1213-MIB::ifDescr')
        device_list = []
        for item in device_mib:
                #if re.search('eth',item):
                        #device_list.append(item.split(':')[3].strip())
                #elif re.search('bond',item):
                        #device_list.append(item.split(':')[3].strip())
                device_list.append(item.split(':')[3].strip())
        return device_list
                                                                                          
#get network date
def getDate(host,oid):
        #date_mib = getAllitems(host,oid)[1:]
        date_mib = getAllitems(host,oid)
        date = []
        for item in date_mib:
                byte = float(item.split(':')[3].strip())
                #date.append(str(round(byte/1024,2)) + ' KB')
                date.append(str(round(byte/1024,2)))
        return date

def network_collect():
        hosts = ['127.0.0.1']
	network_in = {}
	network_out = {}
        for host in hosts:
                device_list = getDevices(host)
                                                                                          
                inside = getDate(host,'IF-MIB::ifHCInOctets')
                outside = getDate(host,'IF-MIB::ifHCOutOctets')
                                                                                          
                for i in range(len(inside)):
                        network_in[device_list[i]] = inside[i]
                        network_out[device_list[i]] = outside[i]
                return network_in, network_out 
                print
	
                                                                                          
#if __name__ == '__main__':
#        hosts = ['127.0.0.1']
#        for host in hosts:
#                device_list = getDevices(host)
#                                                                                          
#                inside = getDate(host,'IF-MIB::ifHCInOctets')
#                outside = getDate(host,'IF-MIB::ifHCOutOctets')
#                                                                                          
#                print '==========' + host + '=========='
#                for i in range(len(inside)):
#                        print '%s : in: %-15s   out: %s ' % (device_list[i], inside[i], outside[i])
#                print
