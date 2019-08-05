#!/user/bin/env python
# -*- coding:utf-8 -*-

# 统计一个字符串中大写、小写字母和数字的个数
def String_count():
    """
    digit   数字个数
    alpha   小写字母个数
    ALPHA   大写字母个数
    """
    digit, alpha, ALPHA = 0, 0, 0
    x = input('Please input a String\n')  # 输入字符串
    list1 = list(x)  # 单个字符传入list1列表
    for i in list1:
        if (i.isdigit()):  # 是否为数字
            digit += 1
        if (i.isalpha() and i.isupper()):  # 是否大写字母
            ALPHA += 1
        if (i.isalpha() and i.islower()):  # 是否小写字母
            alpha += 1
    print('\t该字符串有' + str(digit) + '个数字')  # 输出
    print('\t该字符串有' + str(alpha) + '个小写字母')
    print('\t该字符串有' + str(ALPHA) + '个大写字母')


# 主函数
if __name__ == '__main__':
    String_count()