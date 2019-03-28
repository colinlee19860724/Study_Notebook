#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script Name   : 20190326_practice07.py
# Author        : ColinLee
# QQ:           : 517999276
# URL:          : https://github.com/colinlee19860724
# Created       : 2019/3/28
# Last Modified : 2019/3/28
# Version       : 1.0.1
# Modifications : Add last modification details
#               : [Version ID] Add modification details
#
# Description   : Just describe your script, you may write it later.

# 第7题 求 1 到 5 的阶乘之和

n = int(input("Please input a number: "))
factorial = 1
sum = 0

# 计算从 1 到 num 的阶乘
for i in range(1, n + 1):
    # 得到　num 的阶乘　n! = (n-1)! * n
    factorial = factorial * i
    print("factorial of %d is: %d" %(i, factorial))
    # 将每次阶乘得到的值存入 sum 进行累加
    sum = sum + factorial
    print("sum is : ", sum)
    print("---------------------------------")

# 将最后累加得到的值打印出来
print("Sum of factorial is:　", sum)

