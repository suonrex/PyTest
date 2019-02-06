#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-06 17:43:27
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# string
print("Binary representation of {0} is {0:b}".format(10))
print("Binary representation of {0} is {0:o}".format(10))
print("Binary representation of {0} is {0:x}".format(10))
# Exponent representation: 1.566345e+03
print("Exponent representation: {0:e}".format(1566.345))
# One third is: 0.333
print("One third is: {0:.3f}".format(1/3))
# |ham       |  bread   |    butter|
print("|{2:<10}|{1:^10}|{0:>10}|".format('butter','bread','ham'))

# old format
# x = 12.3456789
# print('The value of x is %3.2' %x)
# print('The value of x is %3.4' %x)

print("PrOgRaMiZ".lower())
print("PrOgRaMiZ".upper())

str_1="This will split all words into a list"
list1=str_1.split()
print(list1)
print(str_1.find('ll'))
print(str_1.replace('ll','rr'))