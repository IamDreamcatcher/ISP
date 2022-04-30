import math

global_x = 21


def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def custom_pow(n, step):
    return pow(n, step)


def func_with_module(x, y):
    return math.sin(x * y * global_x)


class Person:
    type = "Machine"

    def __init__(self, power=5):
        self.power = power

    def get_power(self):
        return self.power


class Biba(Person):
    state = "lox"


class Superman:
    name = "Vladick Sergeevich"
    status = "Legenda"

    def __init__(self, number_of_libs=4):
        self.power_of_libs = []
        for i in range(number_of_libs):
            self.power_of_libs.append(Person(i).power)

    def get_power(self):
        ans = 0
        for i in self.power_of_libs:
            ans += i

        return ans
