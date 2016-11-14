#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 synthesizing task 1"""


class BaseError(Exception):
    """This is a class called BaseError class"""
    pass

class StringError(BaseError, TypeError):
    """This is a class calledStringError class"""
    pass

class NumberError(BaseError, TypeError):
    """This is a class called NumberError class"""
    pass

class NonZeroError(NumberError):
    """AThis is a class called NonZeroError class"""
    pass
