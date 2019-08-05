#!/user/bin/env python
# -*- coding:utf-8 -*-

str1='<a class="resule_img_a" href="https://gz.xiaozhu.com/fangzi/14935329803.html" target="_blank">'
with open('content.txt','w') as f:
    f.write(str1)
    f.close()

"""
open(name文件路径,mode打开方式，buf缓冲buffering大小)
文件读取方式：
read（[size]）读取文件size个字节，默认读取全部
readline（[size]）读取一行
readlines([size])读取完文件，返回每一行所组成的列表

写入文件方式：
write（str）将字符串写入文件中
writelines（sequence_of_strings）写多行到文件



"""