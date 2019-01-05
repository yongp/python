#!/usr/local/bin/python3

import datetime
import time

now = datetime.datetime.now()

#tomrror
day1 = now - datetime.timedelta(days=1)
print (day1.strftime("%Y-%m-%d %H:%M:%S"))