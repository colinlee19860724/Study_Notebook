#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script Name   : 20190326_practice05.py
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

# 第5题 用 * 打印一个边长为 n 的正方形，n 为整数。
# 比如，当 n 为 3 时，打印的效果如下:
#
#     * * *
#     * * *
#     * * *

side_length = int(float(input("请输入正方形的边长：")))
print("绘图如下：")
for i in range(side_length):
    print("* " * side_length)