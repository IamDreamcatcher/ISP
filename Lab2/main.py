from lib.serialization.custom_serialization import serialize


class f:
    pass


def out():
    print(serialize(1))
    #print(serialize(f))


if __name__ == '__main__':
    out()
