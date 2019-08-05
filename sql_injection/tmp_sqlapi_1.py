# -*- coding:utf-8 -*-
"""
@author: jim

"""
import json


a=(898,123,3434,756,756,756,123,74567,4)



json1=json.dumps(a)
print(json1)
json2=json.load(json1)
print(json2)
print(type(json2))
