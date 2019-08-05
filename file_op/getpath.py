# -*- coding:utf-8 -*-
"""
利用python内部集成的tkinter图形库做一个窗口获取文件路径的小功能

"""

def getPath():
    import tkinter
    from tkinter import filedialog
    #获取单个文件



    root=tkinter.Tk()
    root.withdraw()
    filePath=filedialog.askdirectory()
    print(filePath)


getPath()