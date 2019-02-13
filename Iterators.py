#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-13 15:52:31
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# We use the next() function to manually iterate through all the items of an iterator. 
# When we reach the end and there is no more data to be returned, 
# it will raise StopIteration. Following is an example.
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

## iterate through it using next() 

#prints 4
print(next(my_iter))

#prints 7
print(next(my_iter))

## next(obj) is same as obj.__next__()

#prints 0
print(my_iter.__next__())

#prints 3
print(my_iter.__next__())

## This will raise error, no items left
# next(my_iter)

class PowTwo:
	"""Class to implement an iterator
    of powers(幂) of two"""

	def __init__(self, max = 0):
		self.max = max

	def __iter__(self):
		self.n = 0
		return self

	def __next__(self):
		if self.n <= self.max:
			result = 2 ** self.n
			self.n += 1
			return result
		else:
			raise StopIteration

a = PowTwo(4)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

for i in PowTwo(5):
	print(i)

# Infinite Iterators
class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

a=InfIter()
i=iter(a)
print(next(i))
print(next(i))