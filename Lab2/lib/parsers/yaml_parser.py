import yaml
from yaml import UnsafeLoader


def convert_from_yaml(obj):
    return yaml.load(obj, Loader=UnsafeLoader)


def convert_to_yaml(obj):
    return yaml.dump(obj)
