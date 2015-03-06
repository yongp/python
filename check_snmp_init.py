#!/usr/bin/python



#_*_coding: utf-8_*_



'''

Create date: 2012-10-29

Last update: 2012-10-29

Version: 1.0

Description: Monitor interface status

Author: Victor

QQ:1409175531

'''



import sys

import netsnmp



def help():

  print '''Usage:

sys.argv[0] <Community> <Host> <interface>'''



try:

  session = netsnmp.Session(Version=2, Community=sys.argv[1], DestHost=sys.argv[2])

except IndexError:

  help()

  sys.exit()



oid01 = netsnmp.Varbind('ifOperStatus')

oid02 = netsnmp.Varbind('ifDescr')

oidlist01 = netsnmp.VarList(oid01)

oidlist02 = netsnmp.VarList(oid02)

rl01 = session.walk(oidlist01)

rl02 = session.walk(oidlist02)



'''1=>UP,2=>DOWN,3=>TESTING,4=>UNKNOWN,5=>DORMANT,6=>NotPresent,7=>lowerLayerDown'''



try:



  status = dict(zip(rl02,rl01))[sys.argv[3]]



  if status == '1':

    print '%s is UP ' % (sys.argv[3])

    sys.exit(0)

  elif status == '2':

    print '%s is DOWN' % (sys.argv[3])

    sys.exit(2)

  elif status == '3':

    print '%s is TESTING' % (sys.argv[3])

    sys.exit(1)

  elif status == '4':

    print '%s is UNKNOWN' % (sys.argv[3])

    sys.exit(1)

  elif status == '5':

    print '%s is DORMANT' % (sys.argv[3])

    sys.exit(1)

  elif status == '6':

    print '%s is NotPresent' % (sys.argv[3])

    sys.exit(1)

  elif status == '7':

    print '%s is lowerLayerDown' % (sys.argv[3])

    sys.exit(1)

  else:

    print 'UNKNOWN'

    sys.exit(3)



except:

  sys.exit()
