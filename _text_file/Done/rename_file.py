#!/user/bin/env python
# -*- coding:utf-8 -*-

import os

oldname=""
newname=""
dir=""
dir=input("dir:\n")
oldname=input("oldename:\n")
newname=input("newname:\n")



os.listdir(dir)
os.renames(oldname,newname)




