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

# Why generators are used in Python?
# 1. Easy to Implement
class PowTwo:
    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

def PowTwoGen(max = 0):
    n = 0
    while n <= max:
        yield 2 ** n
        n += 1

for item in PowTwo(3):
	print(item)

for item in PowTwoGen(3):
	print(item)

# 3.Represent Infinite Stream
def all_even():
    n = 0
    while True:
        yield n
        n += 2
for ev_no in all_even():
	if ev_no > 10:
		break
	else:
		print(ev_no)