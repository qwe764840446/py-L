# -*- coding:utf-8 -*-

import requests
import re


#网页请求头部
head={
    'Host':'127.0.0.1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://127.0.0.1/dvwa/login.php',
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length':'87',
    'Connection':'close',
    'Cookie': 'security=impossible; PHPSESSID=k0hu49e868kkk7qrhsqun32oe0',
    'Upgrade-Insecure-Requests': '1'
}

#请求登陆的页面
url='http://127.0.0.1/dvwa/login.php'



"""without cookie post payload to get cookies"""
payload_get_cookies={
    'username':'admin',
    'password':'password',
    'Login':'Login'
}


with requests.Session() as c:#requests.Session()会自动保存cookie 在请求的时候会带上
    r=c.get(url=url,)
    '''get_request return a page with cookie'''
    u_token=re.search("user_token'\s*value='(.*?)'", r.text).group(1)

    """get that cookie and add to payload"""
    payload_get_cookies['user_token']=u_token

    """post cookie than retuen a page named index.php which alread login in"""
    p = c.post(url,payload_get_cookies)
    print(p.text)
    #print('\n\n\n\n\n\n\n\n\n')

    r=c.get('http://127.0.0.1/dvwa/vulnerabilities/exec')
    print(r.text)

    #更改难度级别


































"""
head={
    'Host':'127.0.0.1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://127.0.0.1/dvwa/login.php',
    'Content-Type':'application/x-www-form-urlencoded',
    'Content-Length':'87',
    'Connection':'close',
    'Cookie': 'security=impossible; PHPSESSID=k0hu49e868kkk7qrhsqun32oe0',
    'Upgrade-Insecure-Requests': '1'
}

proxy={
    'http':'http://127.0.0.1:9999'
}
user_token='7f7e121717ca4ebb89eb8b246548d04e'
data={
    'username':'admin',
    'password':'password',
    'Login':'Login',
    'user_token':user_token
}

url='http://127.0.0.1/dvwa/login.php'
r=requests.post(headers=head,url=url,proxies=proxy,data=data)


cookie=r.cookies
pa_token=re.compile(r'user_token.+\'')

pa=re.compile(r'<Cookie.+>')
se=re.findall(pa,str(cookie))

ssid=se[0][18:45]
security=se[0][79:89]
new_user_token=re.search(pa_token,r.text).group()[19:-1]
COOKIE={
    'Cookie PHPSESSID':ssid,
    'Cookie security':security,
    'user_token':new_user_token
}


url1='http://127.0.0.1/dvwa/index.php'
resp=requests.post(url=url1,cookies=COOKIE)
print(resp.text)
"""



