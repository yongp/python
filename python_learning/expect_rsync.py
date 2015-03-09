#!/usr/bin/python
'''
#=============================================================================
#     FileName: rsync.py
#         Desc: 
#       Author: Mike Peng
#        Email: g.pengy@gmail.com
#     HomePage: http://about:config
#      Version: 0.0.1
#   LastChange: 2014-11-10 16:11:42
#      History:
#=============================================================================
'''

import pexpect
import sys

username=""
password=""
ip="127.0.0.1"
src_path=""
dst_path=""
tishi="Are you sure you want to continue connecting (yes/no)?"

child=pexpect.spawn('/usr/bin/rsync -avz %s %s@%s:%s' %(src_path, username, ip, dst_path))
child.logfile = sys.stdout

index = child.expect([tishi, 'password: ', pexpect.EOF, pexpect.TIMEOUT])
if index == 0:
    child.sendline('yes')
    child.expect ('password: ')
    child.sendline(password)
    child.expect ("total size is.*")
elif index == 1:
    child.sendline(password)
    child.expect ("total size is.*")
elif index == 2:
    pass
elif index == 3:
    pass

child.close()
