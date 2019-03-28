#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script Name   : 20190326_practice08.py
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

# 第8题 输入一个整数，判断他是否是素数。

num = int(input("请输入一个正整数："))

for i in range(2, num):
    if num % i == 0:
        print("%d 不是一个素数，能被 %d 整除！" %(num, i))
        break
else:
    print("%d 是一个素数!" %(num))


