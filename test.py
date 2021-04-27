#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 4/12/21-11:00
# @Author   : TuringEmmy
# @Email    : yonglonggeng@163.com
# @WeChat   : superior_god
# @File     : test.py
# @Project  : 00PythonProjects
import tensorflow as tf

with open("data/jay.csv") as f:
    content = f.read()
    content=content[8:]

print(content)
