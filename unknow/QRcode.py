#!/user/bin/env python
# -*- coding:utf-8 -*-
import qrcode

# example  qrcode.run_example(data='https://blog.csdn.net/shijichao2/article/details/51228408')

"""
生成二维码的步骤： 
1. 创建QRCode对象 
2. add_data()添加数据 
3. make_image()创建二维码（返回im类型的图片对象） 
4. 自动打开图片，im.show()


练习1：简单调用
将网站URL地址生成二维码图片，以.png的形式保存图片到本地，自动显示生成结果。

import qrcode

data = 'http://write.blog.csdn.net/'
img_file = r'D:\py_qrcode.png'

img = qrcode.make(data)
# 图片数据保存至本地文件
img.save(img_file)
# 显示二维码图片
img.show()

此处并没有使用add_data()添加数据，make_image()生成二维码，而是使用qrcode.make(data)的方式获取im对象。qrcode.make()是qrcode提供简单调用接口。

qrcode.make()函数实现中封装qrcode对象创建、添加数据、生成im对象的操作。

源代码如下：

def make(data=None, **kwargs):
    qr = QRCode(**kwargs)
    qr.add_data(data)
    return qr.make_image()




练习2：生成参数
文章开头提到qrcode可以选择不同的纠错级别，生成不同大小的二维码图片，只需要在实例化QRCode设置不同的参数，就能满足要求。

import qrcode

data = 'http://write.blog.csdn.net/'
img_file = r'D:\py_qrcode.png'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
img.save(img_file)
img.show()



QRCode参数详细说明：

version: 一个整数，范围为1到40，表示二维码的大小（最小值是1，是个12×12的矩阵），如果想让程序自动生成，将值设置为 None 并使用 fit=True 参数即可。
error_correction: 二维码的纠错范围，可以选择4个常量： 
ERROR_CORRECT_L 7%以下的错误会被纠正 
ERROR_CORRECT_M (default) 15%以下的错误会被纠正 
ERROR_CORRECT_Q 25 %以下的错误会被纠正 
ERROR_CORRECT_H. 30%以下的错误会被纠正
boxsize: 每个点（方块）中的像素个数
border: 二维码距图像外围边框距离，默认为4，而且相关规定最小为4
"""

text = '把你的头发剪成你最喜欢最舒服的样子,不要管别人的意见'
img = qrcode.make(text)
img.save('C:\pystrfile\qrcode.jpg')
