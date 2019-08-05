# -*- coding:utf-8 -*-



import os
import re
import time


def get_path():
    os.chdir('D:\\security\\WooYun漏洞、知识库收集(超详细版)\\WooYun_Bugs(漏洞库)\\bugs')
    path=os.getcwd()
    files = os.listdir()
    print(path)
    for i in files:
        isfile = os.path.splitext(i)[-1]
        if (isfile == '.html'):
            # 提取文件html的标题
            rename=get_filename(path,i)
            # 改文件名
            rename = rename + '.html'
            # time.sleep(0.1)
            try:
                os.renames(i,rename)
                if(rename.split('.')[-1]!='html'):
                    print(rename)
            except FileExistsError:
                continue
            except OSError:
                continue




def get_filename(path,file):
    pos=path+'\\'+file
    with open(pos, encoding='utf-8') as f:
        content = f.read()
        # bug_type
        pa_type = re.compile(r'<h3 class=\'wybug_type\'.+</h3>')
        ma_type = re.findall(pa_type, content)
        bug_tyep = ma_type[0][23:-5].replace('\t', '')

        # bug_name
        pa_name = re.compile(r'<h3 class=\'wybug_title\'>.*')
        ma_name = re.findall(pa_name, content)
        bug_name = ma_name[0].replace('\t', '').replace(' ', '>').split('>')[2].split('：')[-1]

        filename = bug_tyep + '----' + bug_name
        return filename

if __name__ == '__main__':
    get_path()


