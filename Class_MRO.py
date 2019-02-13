#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-13 14:30:14
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

class X: pass
class Y: pass
class Z: pass

class A(X,Y): pass
class B(Y,Z): pass

class M(B,A,Z): pass

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

print(M.mro())
