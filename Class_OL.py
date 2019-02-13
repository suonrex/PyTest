#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-13 14:40:57
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
    	return "({0},{1})".format(self.x,self.y)
    # Overloading the + Operator in Python
    def __add__(self,other):
    	x=self.x+other.x
    	y=self.y+other.y
    	return Point(x,y)
    def __lt__(self,other):
	    self_mag = (self.x ** 2) + (self.y ** 2)
	    other_mag = (other.x ** 2) + (other.y ** 2)
	    return self_mag < other_mag

p1=Point(2,3)
p2=Point(-1,2)
# output:(1,5)
print(p1+p2)
# output:False
print(p1<p2)
