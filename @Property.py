#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-15 13:27:49
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# import sys
class Celsius:
	def __init__(self, temperature = 0):
		self.temperature = temperature

	def to_fahrenheit(self):
		return (self.temperature * 1.8) + 32

	# def get_temperature(self):
	@property
	def temperature(self):
		print("Getting value")
		return self._temperature

	# def set_temperature(self, value):
	@temperature.setter
	def temperature(self, value):
		if value < -273:
			raise ValueError("Temperature below -273 is not possible")
		print("Setting value")
		self._temperature = value

	# temperature = property(get_temperature,set_temperature)

# man = Celsius()
# man.temperature = 37

## output:98.60000000000001
# print(man.to_fahrenheit())

# # Therefore, man.temperature internally becomes man.__dict__['temperature']
# print(man.__dict__)

# c = Celsius()
# c.set_temperature(-272)
# print(c.get_temperature())
# sys.setrecursionlimit(4)

# output:
# Setting value
# Getting value
# 10
c = Celsius(10)
print(c.temperature)

# output:
# Setting value
# Getting value
# -272
c.temperature = -272
print(c.temperature)