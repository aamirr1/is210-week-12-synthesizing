#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""

def exception_test(arg1, arg2, arg3):
    """This is xception_test function"""
    
    caught = False
    try:
        arg1[arg2].index(arg3)
    except(TypeError, KeyError, IndexError):
        caught = True
    else:
        caught = False

    return caught
    
