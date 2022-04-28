import inspect
import math

from abc import ABC

import lib.lib_constants
from lib.parsers.json_parser import to_json, from_json
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


c = 3

def sinx():
    return math.sin(1)


class A:
    aba = "kek"

    @staticmethod
    def kik():
        print("Make AGA")


class B:
    lol = math.sin(1)


def out():
    #print(type(math.sin))
    dictionary = serialize({'kok\'s': 4, 'bob': 5})
    print(dictionary)
    print(to_json(dictionary))
    k = to_json(dictionary)
    print(from_json(k, 0, len(k) - 1))
    #k = deserialize(serialize(sinx))
    #print(k())
if __name__ == '__main__':
    out()
#co_name': {'**type**': 'str', '**data**': 'sinx'}
#co_names': {'**type**': 'tuple', '**data**': [{'**type**': 'str', '**data**': 'sin'}]},
#'__globals__': {'sin': {'**type**': 'builtin_function_or_method', '**data**': {'__doc__': {'**type**': 'str', '**data**': 'Return the sine of x (measured in radians).'}, '__module__': {'**type**': 'str', '**data**': 'math'}