# -*- coding: utf-8 -*-
"""
Created on Thu May 25 00:00:54 2023

@author: T
"""

import clang.cindex

file=r'abc.c'
clang.cindex.Config.set_library_file(r'C:\Program Files\LLVM\bin\libclang.dll')
index=clang.cindex.Index.create()
tu=index.parse(file)