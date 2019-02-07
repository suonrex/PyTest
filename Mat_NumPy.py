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
# output:<class 'numpy.ndarray'>
print(type(a),end='\n\n')

# 1. Array of integers, floats and complex Numbers
A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)

A = np.array([[1.1, 2, 3], [3, 4, 5]]) # Array of floats
print(A)

A = np.array([[1, 2, 3], [3, 4, 5]], dtype = complex) # Array of complex numbers
print(A,end='\n\n')

# 2. Array of zeros and ones
zeors_array = np.zeros( (2, 3) )
print(zeors_array)
'''
 Output:
 [[0. 0. 0.]
  [0. 0. 0.]]
'''
ones_array = np.ones( (1, 5), dtype=np.int32 ) # specifying dtype
print(ones_array,end='\n\n')      # Output: [[1 1 1 1 1]]

# 3. Using arange() and shape()
A = np.arange(4)
print('A =', A)

B = np.arange(12).reshape(2, 6)
print('B =', B,end='\n\n')
''' 
Output:
A = [0 1 2 3]
B = [[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
'''
# Addition of Two Matrices
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B      # element wise addition
print(C,end='\n\n')

''' 
Output:
[[11  1]
 [ 8  0]]
 '''

# Multiplication of Two Matrices
A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = a.dot(B)
print(C,end='\n\n')

# Transpose of a Matrix
A = np.array([[1, 1], [2, 1], [3, -3]])
print(A.transpose(),end='\n\n')

# Access matrix elements
A = np.array([[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]])

#  First element of first row
print("A[0][0] =", A[0][0])  

# Third element of second row
print("A[1][2] =", A[1][2])

# Last element of last row
print("A[-1][-1] =", A[-1][-1])

# Access rows of a Matrix
print("A[0] =", A[0]) # First Row
print("A[2] =", A[2]) # Third Row
print("A[-1] =", A[-1]) # Last Row (3rd row in this case)

# Access columns of a Matrix
print("A[:,0] =", A[:,0]) # First Column
print("A[:,3] =", A[:,3]) # Fourth Column
print("A[:,-1] =", A[:,-1],end='\n\n') # Last Column (4th column in this case)

# Slicing of a Matrix
letters = np.array([1, 3, 5, 7, 9, 7, 5])

# 3rd to 5th elements
print(letters[2:5])        # Output: [5, 7, 9]
# 1st to 4th elements
print(letters[:-5])        # Output: [1, 3]   
# 6th to last elements
print(letters[5:])         # Output:[7, 5]
# 1st to last elements
print(letters[:])          # Output:[1, 3, 5, 7, 9, 7, 5]
# reversing a list
print(letters[::-1],end='\n\n')          # Output:[5, 7, 9, 7, 5, 3, 1]

A = np.array([[1, 4, 5, 12, 14], 
    [-5, 8, 9, 0, 17],
    [-6, 7, 11, 19, 21]])

print(A[:2, :4])  # two rows, four columns
''' Output:
[[ 1  4  5 12]
 [-5  8  9  0]]
'''

print(A[:1,])  # first row, all columns
''' Output:
[[ 1  4  5 12 14]]
'''

print(A[:,2])  # all rows, third column
''' Output:
[ 5  9 11]
'''

print(A[:, 2:5])  # all rows, third to fifth column
'''Output:
[[ 5 12 14]
 [ 9  0 17]
 [11 19 21]]
'''