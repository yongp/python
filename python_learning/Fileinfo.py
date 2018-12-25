#!/usr/bin/python

import os
import sys
from UserDict import UserDict

class FileInfo(UserDict):
    "store file metadata"
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename

a = FileInfo()
print (a)
print (a.__init__)
