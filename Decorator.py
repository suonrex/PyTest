#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-14 18:01:43
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

# higher order functions.
def inc(x):
	return x + 1

def dec(x):
	return x - 1

def operate(func,x):
	result = func(x)
	return result

print(operate(inc,3))
print(operate(dec,3))

# Furthermore, a function can return another function.
def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

#Outputs "Hello"
new()

from fractions import Fraction as F
# Decorating Functions with Parameters

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return F(a,b)

# output: I am going to divide 4 and 0;Whoops! cannot divide
print(divide(4,0))

print(divide(4,2))

# Chaining Decorators in Python(参数不明)
def star(func):
	# args是一个数组(tuple)，kwargs一个字典(dictionary)
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star # next
@percent # first
def printer(msg):
    print(msg)
# output:
# ******************************
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Hello
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ******************************
printer("Hello")
print()

# Example2:
import logging


def use_logging(level):

    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

# @use_logging(level="warn")等价于@decorator
@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()


# 类装饰器(__call__)
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('\nclass decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()
print()

# functools.wraps
# 装饰器
def logged(func):
	# @wraps(func) #python 3以前保证元属性要用
    def with_logging(*args, **kwargs):
        print(func.__name__)      # 输出 'with_logging'(Not in Python 3.7?)
        print(func.__doc__)       # 输出 None(Not in Python 3.7?)x
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """does some math"""
   return x + x * x

# output:
#f
#does some math
#6
print(f(2))