#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-02-28 14:29:03
# @Author  : Lance He (suonrex@gmail.com)
# @Link    : Null
# @Version : $Id$

import re
pattern = '^[^a]...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
	print("Search successful.")
else:
	print("Search unsuccessful.")
