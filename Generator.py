#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-13 17:56:05
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

import sys
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_gen()
try:
	next(a)
	next(a)
	next(a)
	next(a)
except StopIteration :
	print(sys.exc_info()[0])

# Using for loop
for item in my_gen():
	print(item)
# output:This is printed first
# 1
# This is printed second
# 2
# This is printed at last
# 3

# Generators with a Loop
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)

# Generator Expression
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
print([x**2 for x in my_list])

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
print((x**2 for x in my_list))

b = (x**2 for x in my_list)
try:
	print(next(b))
	print(next(b))
	print(next(b))
	print(next(b))
	print(next(b))
except StopIteration :
	print(sys.exc_info()[0])

#using for loop
for item in (x**2 for x in my_list):
	print(item)