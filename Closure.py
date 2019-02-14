#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-14 17:21:28
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)
# <function make_multiplier_of.<locals>.multiplier at 0x015B0D20>
print(times3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))
