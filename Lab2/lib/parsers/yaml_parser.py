from yaml import load, dump


def to_yaml(obj):
    return load(obj)


def from_yaml(obj):
    return dump(obj)
