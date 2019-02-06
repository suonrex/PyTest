#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-06 20:04:06
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

my_dict={'name':'Jack','age':'26'}
# change an element
my_dict['age']=27
print(my_dict)

my_dict['name']='Bob'
print(my_dict.get('name'))

# add an element
my_dict['gender']='man'
print(my_dict)
my_dict['job']='PG'
print(my_dict)

# remove an element
print(my_dict.pop('age'))
print(my_dict)

# remove an arbitrary item
print(my_dict.popitem())
del my_dict['name']
print(my_dict)

# remove all items
my_dict.clear()
