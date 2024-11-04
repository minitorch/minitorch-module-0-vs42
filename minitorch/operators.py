"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, Any

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


def mul(x: Any, y: Any):
    return x * y

def id(x: Any):
    return x

def add(x: Any, y: Any):
    return x + y

def neg(x: Any):
    return -x

def lt(x: Any, y: Any):
    return float(x < y)

def eq(x: Any, y: Any):
    return float(x == y)

def max(x: Any, y: Any):
    return x if x > y else y

def is_close(x: Any, y: Any):
    return abs(x - y) < 1e-2

def sigmoid(x: Any):
    return 1.0/(1.0 + math.exp(-x)) if x >=0 else math.exp(x)/(1.0 + math.exp(x))

def relu(x: Any):
    return x if x > 0 else 0

def log(x: Any):
    return math.log(x)

def exp(x: Any):
    return math.exp(x)

def log_back(x: Any, d: Any):
    return d / x

def inv(x: Any):
    return 1 / x

def inv_back(x: Any, d: Any):
    return -d / x ** 2

def relu_back(x: Any, d: Any):
    return d if x > 0 else 0.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.

def map(fn: Callable, list1: Iterable):
    return [fn(x) for x in list1]

def zipWith(fn: Callable, list1: Iterable, list2: Iterable):
    return [fn(x, y) for x, y in zip(list1, list2)]

def reduce(fn: Callable, list1: Iterable):
    ans = 0
    start = True
    for x in list1:
        if start:
            start = False
            ans = x
        else:
            ans = fn(ans, x)
    return ans


def negList(list1: Iterable):
    return map(neg, list1)

def addLists(list1: Iterable, list2: Iterable):
    return zipWith(add, list1, list2)

def sum(list1: Iterable):
    return reduce(add, list1)

def prod(list1: Iterable):
    return reduce(mul, list1)
