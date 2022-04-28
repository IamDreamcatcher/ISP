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

    def kik(self):
        print("Make AGA")


class B:
    lol = math.sin(1)


def out():
    dictionary = to_json(serialize(A))
    print(dictionary)
    pop = deserialize(from_json(dictionary, 0, len(dictionary)))
    obj = pop()
    obj.kik()
if __name__ == '__main__':
    out()