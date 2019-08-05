# -*- coding: utf-8 -*-

import time


def use_time(func):
    def wapper():
        star = time.time()
        func()
        endtime=time() - star
        print(endtime,"\n\n")
    return wapper()

@use_time
def pr():
    for i in range(10,20):
        k=22000111111111111111111111111111111111111111111111111**i
        print(k)
time.time_ns()

pr()
