#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-06 20:04:06
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

my_dict={'name':'Jack','age':'26'}
# change an element
my_dict['age']=27
print(my_dict)

my_dict['name']='Bob'
print(my_dict.get('name'))

# add an element
my_dict['gender']='man'
print(my_dict)
my_dict['job']='PG'
print(my_dict)

# remove an element
print(my_dict.pop('age'))
print(my_dict)

# remove an arbitrary(随机) item
print(my_dict.popitem())
del my_dict['name']
print(my_dict)

# remove all items
my_dict.clear()

# fromkeys(seq[, v]):Return a new dictionary with keys from seq and value equal to v (defaults to None).
marks = {}.fromkeys(['Math','English','Science'], 0)
# output:{'Math': 0, 'English': 0, 'Science': 0}
print(marks)

# items():Return a new view of the dictionary's items (key, value).
for item in marks.items():
	print(item)

# output:['English', 'Math', 'Science']
print(list(sorted(marks.keys())))

# Dictionary comprehension
squares = {x: x*x for x in range(6)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)

odd_squares = {x: x*x for x in range(6) if x%2==1}
print(odd_squares)

# Using a for loop we can iterate though each key in a dictionary.i->key
for i in odd_squares:
	print(odd_squares[i])

# Nested Dictionary
people = {'no1': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'no2': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people['no1']['name'])
print(people['no1']['age'])
print(people['no1']['sex'])

# add element to a nested dic
people['no3'] = {}

people['no3']['name'] = 'Luna'
people['no3']['age'] = '24'
people['no3']['sex'] = 'Female'
people['no3']['married'] = 'No'

for n_dic in people:
	print(people[n_dic])

# delete elements from a nested dic
# del people['no3']['age']
# print(people['no3'])

# delete dictionary from a nested dic
# del people['no2'],people['no3']
# print(people)

# iterate through
for p_id,p_info in people.items():
	print("\nPerson ID:",p_id)
	for key in p_info:
		print(key+":",p_info[key])