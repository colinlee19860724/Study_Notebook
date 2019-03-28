#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script Name   : 20190326_practice01.py
# Author        : ColinLee
# QQ:           : 517999276
# URL:          : https://github.com/colinlee19860724
# Created       : 2019/3/26
# Last Modified : 2019/3/26
# Version       : 1.0.1
# Modifications : Add last modification details
#               : [Version ID] Add modification details
#
# Description   : Just describe your script, you may write it later.

# 第1题：给一个半径，求圆的面积和周长。圆周率为3.14
pi = 3.14
radius = float(input("请输入圆的半径："))

print("圆的面积为：" + str(pi * radius ** 2) )
print("圆的周长为：" + str(2 * pi * radius) )