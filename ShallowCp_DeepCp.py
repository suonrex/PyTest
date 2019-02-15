#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-15 15:30:27
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# Example 1:
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old_list:',old_list)
print('Id of old list is:',id(old_list))

print('New_list:',new_list)
print('Id of new list is:',id(new_list))
# Old_list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Id of old list is: 8507184
# New_list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Id of new list is: 8507184

# Example 2:
import copy
old_list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list2 = copy.copy(old_list2)

# Old list2: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Id of old list2 is: 26402768
print("Old list2:", old_list2)
print('Id of old list2 is:',id(old_list2))
# New list2: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Id of new list2 is: 26439888
print("New list2:", new_list2)
print('Id of new list2 is:',id(new_list2))

# Shallow copy :both lists share the reference of same nested objects
# Old list2: [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# New list2: [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
old_list2[2][2] = 'a'
print("Old list2:", old_list2)
print("New list2:", new_list2)

old_list2.append([4, 4, 4])
print("Old list:", old_list2)
print("New list:", new_list2)

# Example 3:
old_list3 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list3 = copy.deepcopy(old_list3)

# Old list3: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# Id of old list3 is:304 22901
print("Old list3:", old_list3)
print('Id of old list3 is:',id(old_list3))
# New list3: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# Id of new list3 is: 22901144
print("New list3:", new_list3)
print('Id of new list3 is:',id(new_list3))

# Old list3: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
# New list3: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
old_list3[1][0] = 'BB'
print("Old list3:", old_list3)
print("New list3:", new_list3)
