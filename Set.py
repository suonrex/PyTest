#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-06 18:01:03
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$


# set do not have duplicates
# Output: {1, 2, 3, 4}
my_set = {1,2,3,4,3,2}
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# If you uncomment line #12,
# this will cause an error.
# TypeError: unhashable type: 'list'

#my_set = {1, 2, [3, 4]}

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1,2,3,2])
print(my_set)

# initialize a with {}
a = {}

# check data type of a
# Output: <class 'dict'>
print(type(a))

# initialize a with set()
a = set()

# check data type of a
# Output: <class 'set'>
print(type(a))

# initialize my_set
my_set = {1,3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

#my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)

# discard an element
# Output: {1, 2, 3, 5, 6, 8}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 2, 3, 5, 8}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 2, 3, 5, 8}
my_set.discard(4)
print(my_set)

# remove an element
# not present in my_set,you will get an error.
# my_set.remove(4)

print(my_set.pop())
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)

# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)
print(A.union(B))

# use & operator
# Output: {4, 5}
print(A & B)
print(A.intersection(B))

# use - operator on A
# Output: {1, 2, 3},{8, 6, 7}
print(A - B)
print(B - A)
print(A.difference(B))
print(B.difference(A))

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)
print(A.symmetric_difference(B))

C=A.copy()
print(C)

# Sets being mutable are unhashable, so they can't be used as dictionary keys.
# On the other hand, frozensets are hashable and can be used as keys to a dictionary.
D=frozenset([1,2,3])
E=frozenset([4,5,6])
print(D.isdisjoint(E))