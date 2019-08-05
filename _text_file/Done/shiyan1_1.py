# -*- coding: utf-8 -*-
profit_all = int(input('input your profit(10 thousand)\n'))
bouns = 0
if (profit_all > 100):
    bouns += (profit_all - 100) * 0.01

if (profit_all <= 100 and profit_all > 60):
    bouns += (profit_all - 60) * 0.015

if (profit_all <= 60 and profit_all > 40):
    bouns += (profit_all - 40) * 0.03

if (profit_all <= 40 and profit_all > 20):
    bouns += (profit_all - 20) * 0.05

if (profit_all <= 20 and profit_all > 10):
    bouns += (profit_all - 10) * 0.075

if (profit_all < 10):
    bouns += profit_all * 0.1
print(bouns)
