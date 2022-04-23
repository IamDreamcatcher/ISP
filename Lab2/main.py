import inspect

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


def lol():
    print(3)

def out():
    b = deserialize(serialize(kek))(1)


    
    #raise_power_to_3 = gfg(3)

    #c = deserialize(serialize(raise_power_to_3))(3)

    #print(raise_power_to_3.__getattribute__(lib.lib_constants.GLOBAL))
    #print(kek.__closure__)
    #print(serialize(f))


if __name__ == '__main__':
    out()
