import yaml
from yaml import UnsafeLoader


def from_yaml(obj):
    return yaml.load(obj, Loader=UnsafeLoader)


def to_yaml(obj):
    return yaml.dump(obj)
