#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script Name   : 20190326_practice06.py
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

# 第6题 输入一个正整数n，求0到这个数以内的所有 奇数的和 与 偶数的和。
num = int(input("Please input a integer number: "))
odd_num = 0
even_num = 0

for i in range(num + 1):
    if i & 1 == 1: # 奇数与 1 做位运算 与（&），其结果恒为 1；偶数与 1 做位运算 与（&），其结果恒为 0
        print("%d is an odd number! " %(i))
        odd_num = odd_num + i
    else :
        print("%d is an even number! " %(i))
        even_num = even_num + i
print("----------------------------------------")
print("Sum of odd numbers is: ", odd_num)
print("Sum of even numbers is: ", even_num)