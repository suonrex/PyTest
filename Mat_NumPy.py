#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-07 14:52:37
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# Matrices
A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]
print("A =", A) 
print("A[1] =", A[1])      # 2nd row
print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])   # Last element of 1st Row

column=[]
for row in A:
	column.append(row[2])

print(column,end='\n\n')

# NumPy Array
import numpy as np
a = np.array([1,2,3])
print(a)