#!/usr/local/bin/python3

import json


data = {
    "Runoob": 1,
    'name': 'runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)

print ('python原始数据', repr(data))
print ('json数据', json_str)

