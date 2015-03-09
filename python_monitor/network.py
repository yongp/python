#!/usr/bin/python
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
                if re.search('eth',item):
                        device_list.append(item.split(':')[3].strip())
        return device_list
                                                                                          
#get network date
def getDate(host,oid):
        date_mib = getAllitems(host,oid)[1:]
        date = []
        for item in date_mib:
                byte = float(item.split(':')[3].strip())
                date.append(str(round(byte/1024,2)) + ' KB')
        return date
                                                                                          
if __name__ == '__main__':
        hosts = ['127.0.0.1']
        for host in hosts:
                device_list = getDevices(host)
                                                                                          
                inside = getDate(host,'IF-MIB::ifInOctets')
                outside = getDate(host,'IF-MIB::ifOutOctets')
                                                                                          
                print '==========' + host + '=========='
                for i in range(len(inside)):
                        print '%s : RX: %-15s   TX: %s ' % (device_list[i], inside[i], outside[i])
                print
