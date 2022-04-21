from toml import loads, dumps


def to_toml(obj):
    return dumps(obj)


def from_toml(string):
    return loads(string)
