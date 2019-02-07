#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-07 17:41:08
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# Conditionals in List Comprehension
# Using if with List Comprehension
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

number_list2 = list(filter(lambda x : x % 2 == 0,range(20)))
print(number_list2)

# Nested IF with List Comprehension
number_list3 = [y / 5 for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(number_list3)
# lambda cannot?
number_list4 = list(filter(lambda y : y % 2 == 0 and y % 5 == 0 ,range(100)))
print(number_list4)

# if...else With List Comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

# Transpose of Matrix using Nested Loops
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

#Output: [[1, 4], [2, 5], [3, 6]]

# Transpose of a Matrix using List Comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)