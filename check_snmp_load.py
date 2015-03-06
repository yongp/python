#!/usr/bin/python2.4

#_*_ coding: utf-8 _*_



'''

Last Modify: 2014/05/12

Version: 1.1

Description: Monitor CPU Load

Author: Victor

QQ:1409175531

'''



from sys import argv,exit

from decimal import Decimal

from optparse import OptionParser

from netsnmp import snmpwalk



parser = OptionParser('%prog -C <Community> -H <Host> -w <1min,5min,15min> -c <1min,5min,15min>')



parser.add_option('-H', '--HostAddr', action='store', dest='hostaddress', help='指定设备地址')

parser.add_option('-C', '--community', action='store', dest='community', help='指定SNMP团体名')

parser.add_option('-w', '--warning', action='store', dest='warning', help='设定警告阀值')

parser.add_option('-c', '--critical', action='store', dest='critical', help='设定严重警告阀值')



(options, argvs) = parser.parse_args(argv)



desc_name = ['UCD-SNMP-MIB::laNames', 'UCD-SNMP-MIB::laLoad']



if not len(argv) == 9 or not len(options.warning.split(',')) == 3 or not len(options.critical.split(',')) == 3:

    parser.print_help()

    exit(3)



for desc in desc_name:

    data = snmpwalk(desc,Version=2, Community=options.community, DestHost=options.hostaddress)

    if 'UCD-SNMP-MIB::laNames' == desc:

        items = data

    elif 'UCD-SNMP-MIB::laLoad' == desc:

        load = data



warn_list = options.warning.split(',')

crit_list = options.critical.split(',')



seq0 = -1

for threshold in warn_list:

    seq0 += 1

    if float(threshold) > float(crit_list[seq0]):print '-w %s,%s,%s 必须小于或等于 -c %s,%s,%s' % (load[0],load[1],load[2],load[0],load[1],load[2]);exit(3)



status = []

warn_status = []

crit_status = []



seq = -1

for warn in warn_list:

    seq += 1

    if float(load[seq]) < float(warn):status.append(items[seq] + ':' + load[seq])

    elif float(crit_list[seq]) > float(load[seq]) > float(warn): warn_status.append(items[seq] + ':' + load[seq])

    elif float(crit_list[seq]) < float(load[seq]): crit_status.append(items[seq] + ':' + load[seq])



if len(status) == 3:

    print 'OK - 负载正常: %s | OK - 负载正常: %s,%s,%s' % (status,load[0],load[1],load[2]);exit(0)

elif not len(crit_status) == 0:

    if warn_status:

        print 'Critical - 负载严重过高: %s,%s | Critical - 负载严重过高: %s,%s,%s' % (warn_status,crit_status,load[0],load[1],load[2]);exit(2)

    else:

        print 'Critical - 负载严重过高: %s | Critical - 负载严重过高: %s,%s,%s' % (crit_status,load[0],load[1],load[2]);exit(2)

elif not len(warn_status) == 0:

    print 'Critical - 负载过高: %s | Critical - 负载过高: %s,%s,%s' % (warn_status,load[0],load[1],load[2]);exit(1)
