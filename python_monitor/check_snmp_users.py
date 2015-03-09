#!/usr/bin/python

#_*_ coding: utf-8 _*_

#_*_ coding: cp950 _*_



'''

Create date: 2012-10-24

Last update: 2012-10-24

Version: 1.0

Description: Monitor login users

Author: Victor

QQ:1409175531

'''



import sys

import netsnmp

import os



def help():

  print '''Usage:

%s <Community> <Host> <Warning_threold>''' % (sys.argv[0])



oid = netsnmp.Varbind('HOST-RESOURCES-MIB::hrSystemNumUsers.0')

odilist = netsnmp.VarList(oid)



try:

  resultList = netsnmp.snmpget(oid, Version=2, Community=sys.argv[1], DestHost=sys.argv[2])

except IndexError:

  help()

  sys.exit()



result = str(resultList)[2:-3]

c = result.split()



if not len(sys.argv) == 4:

  help()

  sys.exit()

else:

  try:

    if int(c[0]) < int(sys.argv[3]):

      print 'OK - 登录用户数: %s | 登录用户数: %s (报警阀值: %s)' % (c[0], c[0], sys.argv[3])

      sys.exit(0)

    elif c[0] >= int(sys.argv[3]):

      print 'Warning - 登录用户数: %s | 登录用户数: %s (报警阀值: %s)' % (c[0], c[0], sys.argv[3])

      sys.exit(1)

    else:

      print 'Unknown'

      sys.exit(3)

  except ValueError:

    print 'Warning_threold Must be an integer'
