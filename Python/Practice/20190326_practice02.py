#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script Name   : 20190326_practice02.py
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

# 第2题：输入两个数，比较大小后，从小到大升序打印
first_number = float(input("请输入第一个数字："))
second_number = float(input("请输入第二个数字："))

if first_number < second_number :
    print("\n输入的数字从小到大依次为：\n" + str(first_number) + '\n' + str(second_number))
elif first_number > second_number :
    print("\n输入的数字从小到大依次为：\n" + str(second_number) + '\n' + str(first_number))
else :
    print("\n您输入的可能为同一个数字！")