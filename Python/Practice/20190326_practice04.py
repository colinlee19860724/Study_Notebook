#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script Name   : 20190326_practice04.py
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

# 第4题 死循环输入数字，输入后打印出之前输入的最大值、之前所有数字的平均数，如果输入的不是数字，而是quit字符串或者空格，则结束循环，退出程序。

count = 0
maxNum = 0
totalNum = 0

while True:
    input_str = input("请输入一个数字(如需退出请输入 quit 或空格)：")
    if input_str == '' or input_str == ' ' or input_str == 'quit' :
        print("已退出程序！")
        break
    else:
        input_number = float(input_str)
        if input_number > maxNum :
            maxNum = input_number
        else :
            maxNum = maxNum
    count = count + 1
    totalNum = totalNum + input_number
    averageNum = totalNum / count
    print("已输入 %d 次数字！" %(count))
    print("之前输入的最大值是：",maxNum)
    print("所有数字的平均数是：",averageNum)
