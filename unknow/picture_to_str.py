#!/user/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image

ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
# 是我们的字符画所使用的字符集，一共有 70 个字符，字符的种类与数量可以自己根据字符画的效果反复调试的

WIDTH = 284  # 字符画的宽
HEIGHT = 177  # 字符画的高


# 将256灰度映射到70个字符上，也就是RGB值转字符的函数：

def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]  # 不同的灰度对应着不同的字符


# 通过灰度来区分色块


if __name__ == '__main__':
    img = 'C:\\pystrfile\\5.png'  # 图片所在位置
    im = Image.open(img)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))  # 获得相应的字符
        txt += "\n"
    print(txt)

    with open("C:\\pystrfile\\str_photo5.txt", 'w') as f:
        f.write(txt)
