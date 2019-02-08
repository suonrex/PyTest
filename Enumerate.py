#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-08 16:16:25
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# Example 1: How enumerate() works in Python?

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

# Example 2: Looping Over an Enumerate object
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)