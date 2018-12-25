#!/usr/bin/python3

import sys
import os

'''i = 0
while True:
    if i < 10:
        f = open("/Users/mikepeng/Downloads/test.txt", "a")
        f.write("python is good lang!!\n")
        f.close()
        i = i+1
    else:
        break'''

f = open("/Users/mikepeng/Downloads/foo.txt", "rb+")
f.write(b'0123456789abcde')
x = f.seek(2)
print (x)
#for line in f:
#    print (line, end=" ")∂
#str = f.readline()
#print (str)
#print (f.tell())
f.close()




