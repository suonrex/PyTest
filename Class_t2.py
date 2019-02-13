#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-12 17:23:00
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

class MyClass:
	"This is my sceond class"
	a = 10

	def func(self):
		print("Hello")

ob=MyClass()

# output:10
print(MyClass.a)
print(ob.a)

# output:<function MyClass.func at 0x01D709C0>
print(MyClass.func)
print(ob.func())

# Output: 'This is my second class'
print(MyClass.__doc__)
print(ob.__doc__)

class ComplexNumber:
	def __init__(self,r=0,i=0):
		self.real=r
		self.imag=i
	def getData(self):
		print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
# c1.attr
