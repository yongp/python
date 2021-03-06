#!/usr/bin/python
#coding=utf-8

import os
def getAllitems(host, oid):
        sn1 = os.popen('snmpwalk -v 2c -c public ' + host + ' ' + oid).read().split('\n')[:-1]
        return sn1
                                                                            
def getSwapTotal(host):
        swap_total = getAllitems(host, 'UCD-SNMP-MIB::memTotalSwap.0')[0].split(' ')[3]
        return swap_total
                                                                            
def getSwapUsed(host):
        swap_avail = getAllitems(host, 'UCD-SNMP-MIB::memAvailSwap.0')[0].split(' ')[3]
        swap_total = getSwapTotal(host)
        #swap_used = str(round(((float(swap_total)-float(swap_avail))/float(swap_total))*100 ,2)) + '%'
        swap_used = int(round(((float(swap_total)-float(swap_avail))/float(swap_total))*100))
        return swap_used
                                                                            
def getMemTotal(host):
        mem_total = getAllitems(host, 'UCD-SNMP-MIB::memTotalReal.0')[0].split(' ')[3]
        return mem_total
                                                                            
def getMemUsed(host):
        mem_total = getMemTotal(host)
        mem_avail = getAllitems(host, 'UCD-SNMP-MIB::memAvailReal.0')[0].split(' ')[3]
        #mem_used = str(round(((float(mem_total)-float(mem_avail))/float(mem_total))*100 ,2)) + '%'
        mem_used = int(round(((float(mem_total)-float(mem_avail))/float(mem_total))*100))
        return mem_used

def mem_collect():
        hosts = ['127.0.0.1']
	mem_data = {}
        for host in hosts:
                mem_used = getMemUsed(host)
                swap_used = getSwapUsed(host)
		mem_data['Mem_Used'] = mem_used
		mem_data['Swap_Used'] = swap_used
                #print mem_data
                return mem_data
                                                                            
#if __name__ == '__main__':
#        hosts = ['127.0.0.1']
#        print "Monitoring Memory Usage"
#        for host in hosts:
#                mem_used = getMemUsed(host)
#                swap_used = getSwapUsed(host)
#                print '==========' + host + '=========='
#                print 'Mem_Used = %-15s   Swap_Used = %-15s' % (mem_used, swap_used)
#                print
