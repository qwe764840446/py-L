# -*- coding:utf-8 -*-
"""
利用python内部集成的tkinter图形库做一个窗口

"""
def mainframe():
    import tkinter
    #窗口对象
    win=tkinter.Tk()
    #标题
    win.title=('put your title here')
    #大小 另一种设置法win.geometry('540x300')
    width=600
    height=400
    #窗口大小是否可变
    win.resizable(width=True,height=True)

    #获取屏幕的信息  长宽
    screenwidth=win.winfo_screenmmwidth()
    screenheight=win.winfo_screenheight()
    print(screenheight,screenwidth)
    #长宽以及显示的位置 让其居中显示
    alignstr='%dx%d+%d+%d'%(width,height,(screenwidth+width)/2,(screenheight-height)/2)
    print(alignstr)
    win.geometry(alignstr)
    # 弹窗
    win.mainloop()
    



mainframe()