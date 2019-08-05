# -*- coding:utf-8 -*-
"""
@author: jim

"""
import requests
import re


pa_name=re.compile(r'Your Login name:.*<br>')
pa_pwd=re.compile(r'Your Password:.*</font>')

url='http://127.0.0.1/sqli/Less-1/index.php'
url_parameter='?id=2'

#url=input('input url without parameter\n')
#url_parameter=input('input your url parameter\n')
url_get=url+url_parameter
r=requests.get(url_get)

print(r.text)

try:
    print(re.search(pa_name,r.text).group())
    print(re.search(pa_pwd,r.text).group())
except AttributeError:
    print('not found')








