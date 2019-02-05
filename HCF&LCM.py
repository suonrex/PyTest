#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-05 14:10:41
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# Finding HCF(highest common factor) or GCD(greatest common divisor) in a normal way
def computerHCF(x,y):
	if x > y:
		smaller=y
	else:
		smaller=x

	for i in range(1,smaller):
		if((x%i==0) and (y%i==0)):
			hcf=i
	return hcf

# Finding LCM in a normal way
def computerLCM(A_x,A_y):
	if A_x > A_y:
		L_bigger=A_x
	else:
		L_bigger=A_y

	L_lcm=L_bigger

	while True:
		
		if ((L_lcm % A_x == 0) and (L_lcm % A_y == 0)):
			return L_lcm
		else:
			L_lcm = L_lcm + 1

num1 = 24
num2 = 54

print("The HCF of",num1,"and",num2,"is",computerHCF(num1,num2))

print("The LCM of",num1,"and",num2,"is",computerLCM(num1,num2))

# Using Euclidean Algorithm to find HCF
def EuclideanHCF(x,y):
	while(y):
		x,y=y,x%y
		#print("x=",x,"y=",y)
	return x

print("The HCF of",num1,"and",num2,"is",EuclideanHCF(num1,num2))

# Using GCD function to find LCM(least common multiple)
def gcd(A_x,A_y):
	while(A_y):
		A_x, A_y= A_y, A_x % A_y

	return A_x

def lcm(A_x,A_y):
	lcm = (A_x*A_y) // gcd(A_x,A_y)
	return lcm

print("The LCM of",num1,"and",num2,"is",lcm(num1,num2))
