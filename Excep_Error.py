#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-08 13:37:39
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
    	# sys.exc_info()->(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x018E2648>)
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r,"\n")
# output:
# The entry is a
# Oops! <class 'ValueError'> occured.
# Next entry.

# The entry is 0
# Oops! <class 'ZeroDivisionError' > occured.
# Next entry.

# The entry is 2
# The reciprocal of 2 is 0.5

try:
	a = int(input("Enter a positive integer: "))
	if a <= 0:
		raise ValueError("That is not a positive number!")
except ValueError as ve:
	print(ve)

# User-Defined Exception in Python
class Error(Exception):
	""" Base class for other exceptions"""
	pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

 # our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
	try:
		i_num = int(input("Enter a number: "))
		if i_num < number:
			raise ValueTooSmallError
		elif i_num > number:
			raise ValueTooLargeError
		break
	except ValueTooSmallError:
		print("This value is too small, try again!")
		print()
	except ValueTooLargeError:
		print("This value is too large, try again!")
		print()

print("Congratulations! You guessed it correctly.")