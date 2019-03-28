#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script Name   : 20190326_practice03.py
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

# 第3题：输入一个成绩分数，判断学生成绩等级，A至E，其中，90分以上为‘A'，80~89分为'B'，70~79分为'C'，60~69分为'D'，60分以下为'E'
score = float(input("请输入学生的成绩分数："))

print("\n")
if score >= 90:
    print("学生成绩等级为：A")
elif score >= 80:
    print("学生成绩等级为：B")
elif score >= 70:
    print("学生成绩等级为：C")
elif score >= 60:
    print("学生成绩等级为：D")
elif score >= 0:
    print("学生成绩等级为：E")
else :
    print("您输入的成绩不正确！")