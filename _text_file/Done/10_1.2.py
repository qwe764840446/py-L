# -*- coding:utf-8 -*-
"""
@author: jim

"""


import os


#编写代码将当前工作目录修改为“C:\”并验证，最后将当前工作目录恢复为原来的目录

'''保存当前工作路径'''
oldpwd=os.getcwd()
'''修改成c盘'''
os.chdir('C:\\')
print('前工作路径',os.getcwd())
'''恢复原来路径'''
os.chdir(oldpwd)
print('前工作路径',os.getcwd(),'\n\n\n**************************')




#编写程序，用户输入一个目录和一个文件名，搜索该目录机器子目录中是否存在该文件
import os.path as ph

# input_pwd='G:\\phpstudy'
# input_file='index.php'

input_pwd=input('input pwd\n')
input_file=input('file name\n')
searchfile=input_pwd+'\\'+input_file
print(searchfile)
#深度遍历
def Depthscan(input_pwd,input_file):
    #遍历
    for subPath in os.listdir(input_pwd):
        #提取所有文件和文件夹
        path = ph.join(input_pwd, subPath)
        #是文件就判断是否含有要找的文件
        if ph.isfile(path):
            if(input_file in path):
                print(path)
        #否则就是路径继续遍历
        elif ph.isdir(path):
            Depthscan(path,input_file)



Depthscan(input_pwd,input_file)




