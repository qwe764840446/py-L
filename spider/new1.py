#!/user/bin/env python
# -*- coding:utf-8 -*-

import requests

r = requests.get("https://www.zhihu.com/")
rHead=r.headers
print(rHead)
