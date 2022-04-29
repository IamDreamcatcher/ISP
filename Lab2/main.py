import inspect
import math
import json
import tomli
import tomli_w
import yaml

from abc import ABC

from yaml import UnsafeLoader

import lib.lib_constants
from lib.parsers.json_parser import to_json, from_json
from lib.parsers.toml_parser import to_toml, from_toml
from lib.parsers.yaml_parser import to_yaml, from_yaml
from lib.serialization.custom_serialization import serialize, deserialize
from math import sin


class F:
    pass


def test_fact(n):
    if n == 0:
        return 1
    else:
        return n * test_fact(n - 1)


glob = 5


def lol(n):
    return test_fact(n) * glob


c = 3


def sinx(x, y):
    return math.sin(x * y + c)


class A:
    aba = "kek"

    def kik(self):
        print("Make AGA")


class B:
    lol = math.sin(1)


def out():
    print(tomli_w.dumps(serialize({0:   1})))


if __name__ == '__main__':
    out()
