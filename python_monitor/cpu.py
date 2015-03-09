#!/usr/bin/python
import os
def getAllitems(host, oid):
        sn1 = os.popen('snmpwalk -v 2c -c 360buy ' + host + ' ' + oid + '|grep Raw|grep Cpu|grep -v Kernel').read().split('\n')[:-1]
        return sn1
                                                                
def getDate(host):
        items = getAllitems(host, '.1.3.6.1.4.1.2021.11')
                                                                
        date = []
        rate = []
        cpu_total = 0
        #us = us+ni, sy = sy + irq + sirq
        for item in items:
                float_item = float(item.split(' ')[3])
                cpu_total += float_item
                if item == items[0]:
                        date.append(float(item.split(' ')[3]) + float(items[1].split(' ')[3]))
                elif item == item[2]:
                        date.append(float(item.split(' ')[3] + items[5].split(' ')[3] + items[6].split(' ')[3]))
                else:
                        date.append(float_item)
                                                                
        #calculate cpu usage percentage
        for item in date:
                rate.append((item/cpu_total)*100)
                                                                
        mean = ['%us','%ni','%sy','%id','%wa','%cpu_irq','%cpu_sIRQ']
                                                                
        #calculate cpu usage percentage
        result = map(None,rate,mean)
        return result
                                                                
if __name__ == '__main__':
        hosts = ['172.22.213.59']
        for host in hosts:
                print '==========' + host + '=========='
                result = getDate(host)
                print 'Cpu(s)',
                #print result
                for i in range(5):
                        print ' %.2f%s' % (result[i][0],result[i][1]),
                print
                print
