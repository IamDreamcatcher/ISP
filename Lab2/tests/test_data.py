import math

import pytest


global_x = 21


def test_fib(n):
    if n in (1, 2):
        return 1
    return test_fib(n - 1) + test_fib(n - 2)


def custom_pow(n, step):
    return pow(n, step)


def func_with_module(x, y):
    return math.sin(x * y * global_x)


class Machine:
    pass
