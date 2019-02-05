#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-05 14:25:10
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$
# Example of recursive function
def calc_factorial(A_x):
	if A_x == 1:
		return A_x
	else:
		A_x *= calc_factorial(A_x - 1)
		return A_x

# int() is essential!
num = int(input('Input a num: '))
print("{0}'s factorial is {1}".format(num,calc_factorial(num)))

