import tomli
import tomli_w


def convert_to_toml(obj):
    return tomli_w.dumps(obj)


def convert_from_toml(string):
    return tomli.loads(string)
