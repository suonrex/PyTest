#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-05 17:50:28
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

my_list=[1,3,4,5,6,9,10]

filter_list=list(filter(lambda x:(x%3==0),my_list))

print(filter_list)

map_list=list(map(lambda x:(x*2),my_list))

print(map_list)