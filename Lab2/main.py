import inspect
import math
from abc import ABC

import lib.lib_constants
from lib.serialization.custom_serialization import serialize, deserialize
from math import sin


class F:
    pass

# this is a nested function
def gfg(raise_power_to):

    def power(number):
        return number ** raise_power_to
    return power


def kek(a, b = 4):
    a = "aboba"
    if False:
        kek(1, 2)
    b = sin(1)
    return a


def test_fact(n):
    if n == 0:
        return  1
    else:
        return n * test_fact(n - 1)

glob = 5


def lol(n):
    return test_fact(n) * glob


def sinx(x):
    return math.sin(x)


class A:
    aba = "kek"

    @staticmethod
    def kik():
        print("Make AGA")


class B:
    lol = "lol"


def out():
    k = deserialize(serialize(B))
    print(k.lol)

    
    #raise_power_to_3 = gfg(3)

    #c = deserialize(serialize(raise_power_to_3))(3)

    #print(raise_power_to_3.__getattribute__(lib.lib_constants.GLOBAL))
    #print(kek.__closure__)
    #print(serialize(f))


if __name__ == '__main__':
    out()
