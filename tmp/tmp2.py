# -*- coding:utf-8 -*-
"""
@author: jim

"""

import os
#新建文件位置
pos='H:\\'
#文件夹名字
name='Git'

new=pos+name

print(os.getcwd())
os.chdir(pos)
print(os.getcwd())
os.mkdir(new)


