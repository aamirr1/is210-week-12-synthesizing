#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 Synthesizing task 2"""


class CustomError(Exception):
    """This is a new class called CustomError"""
    
    def __init__(self, message, cause):
        Exception.__init__(self, message)
        self.cause = cause
