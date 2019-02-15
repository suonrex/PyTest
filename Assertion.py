#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-15 17:58:18
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

def avg(marks):
	assert len(marks) != 0
	return sum(marks)/len(marks)

# output:AssertionError
# mark1 = []
# print("Average of mark1:",avg(mark1))


def avg2(marks):
	assert len(marks) != 0,"List is empty"
	return sum(marks)/len(marks)

# output: Average of mark2 is: 71.33333333333333
mark2 = [55,58,68,78,90,79]
print("Average of mark2 is:",avg2(mark2))

# output: AssertionError: List is empty
mark3 = []
print("Average of mark3 is:",avg2(mark3))