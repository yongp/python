#!/usr/local/bin/python3

import os
import sys
from UserDict import UserDict

msg = "hello world!"
print (msg)

class Myclass:
    def __init__(self):
        self.data = []

    i = 12345

    def f(self):
        return "hello world"

x = Myclass()

print (x)
print (x.i)
print (x.f())

class FileInfo(UserDict):
    "store file metadata"
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename

a = FileInfo()
print (a)
print (a.__init__)