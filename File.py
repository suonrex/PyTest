#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-08 11:44:24
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# safe way in case of exception
try:
	f = open("text1.txt",mode='r',encoding = 'utf-8')
finally:
	f.close()

with open("test1.txt",'w',encoding = 'utf-8') as f:
# perform file operations
	f.write("my first file\n")
	f.write("This file\n\n")
	f.write("contains three lines\n")

try:
	f = open("test1.txt",mode='r',encoding = 'utf-8')
	for line in f:
		print(line, end = '')
finally:
	f.close()
	
