#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-07 13:25:58
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

import array as arr

L_a=arr.array('d', [1.1,2.3,4.5])
print(L_a)
for item in L_a:
	print(item)

# How to slice arrays?
numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) # beginning to 3th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end

# How to change or add elements?
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
numbers[0] = 0    
print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])   
print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])

# We can add one item to a list using append() method or add several items using extend() method.
numbers.append(11)
print(numbers)

numbers.extend([3,5,7])
print(numbers)

# concatenate two arrays using + operator.
import array as arr

odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])

numbers = arr.array('i')   # creating empty array of integer
numbers = odd + even
print(numbers)

# How to remove/delete elements?
del numbers[2]
print(numbers)

# We can use the remove() method to remove the given item, 
# and pop() method to remove an item at the given index.
numbers.remove(6)
print(numbers)

print(numbers.pop(3))
print(numbers)