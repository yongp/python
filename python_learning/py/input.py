#!/usr/bin/python3

import os
import sys
import random

#随机获得一个三位数
a = random.randrange(100,999)

print (a)

while True:
    #捕获异常
    try:
        x = int(input("请输入三位数字: "))
#        if len(x) < 3 or len(x) == 0:
#            print ("数字长度不够三位数!")
        if x > a:
            print ("大于数值")
        elif x < a:
            print ("小于数值")
        elif x == a:
            print ("恭喜你答对了")
            break
    #except (EOFError,InterruptedError):
    except ValueError:
        print ("输入的数值不是数字!")
