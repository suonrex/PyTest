#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-06 16:26:27
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$
#LIST(mutable)
list1=[2 ** x for x in range(10) if x > 5 and 2 ** x % 128 == 0]
print(list1)

list2=[x+y for x in ['x','y','z','a'] for y in ['a','b','c','d']]
print(list2)

print(5 in list2)
print('x' not in list1)

# <class 'enumerate'>
# [(10, 128), (11, 256), (12, 512)]
print(type(enumerate(list1)))
print(list(enumerate(list1,10)))

#TUPLE(Immutable)
tuple1=()
# tuple with mixed datatypes
# tuple can be created without parentheses
tuple1=1,"tuple",['a','b','c']
print(tuple1)

# tuple unpacking is also possible
a,b,c=tuple1
# Output:
# 1
# tuple
# ['a', 'b', 'c']
print(a)
print(b)
print(c)

# only parentheses is not enough
# Output: <class 'str'>
my_tuple = ("hello")
print(type(my_tuple))

# need a comma at the end
# Output: <class 'tuple'>
my_tuple = ("hello",)  
print(type(my_tuple))

# parentheses is optional
# Output: <class 'tuple'>
my_tuple = "hello",
print(type(my_tuple))

my_tuple = (4, 2, 3, [6, 5])

# we cannot change an element
# If you uncomment line 8
# you will get an error:
# TypeError: 'tuple' object does not support item assignment

#my_tuple[1] = 9

# but item of mutable element can be changed
# Output: (4, 2, 3, [9, 5])
my_tuple[3][0] = 9
print(my_tuple)

# tuples can be reassigned
# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple)

# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)

# can delete entire tuple
# NameError: name 'my_tuple' is not defined
del my_tuple
# my_tuple
#print(type(my_tuple))

my_tuple = ('a','p','p','l','e',)

# Count
# Output: 2
print(my_tuple.count('p'))

# Index
# Output: 3
print(my_tuple.index('l'))

for item in my_tuple:
	print(item)

print(list(enumerate(my_tuple,10)))