import tomli
import tomli_w


def to_toml(obj):
    return tomli_w.dumps(obj)


def from_toml(string):
    return tomli.loads(string)
