#!/usr/bin/python
'''
#=============================================================================
#     FileName: time.py
#         Desc: 
#       Author: Mike Peng
#        Email: g.pengy@gmail.com
#     HomePage: http://about:config
#      Version: 0.0.1
#   LastChange: 2014-11-20 09:13:59
#      History:
#=============================================================================
'''


import time 
from tqdm import *

for i in tqdm(range(1000)):
    time.sleep(.01)
