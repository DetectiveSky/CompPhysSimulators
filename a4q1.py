#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:53:35 2020

@author: davidstothers
"""

def outer():
    x, y = 'E', 'E'
    def inner():
        global x
        x = 'L'
        print("Inner Function:", x, y, z)
    inner()
    print("Outer Function:", x, y, z)
x, y, z = 'G', 'G', 'G'
outer()
print("Main Program:", x, y, z)