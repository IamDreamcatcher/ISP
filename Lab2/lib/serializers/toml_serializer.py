from lib.parsers.toml_parser import to_toml, from_toml
from lib.serialization.custom_serialization import serialize, deserialize


class TomlSerializer:
    @staticmethod
    def dump(obj, file_path):
        with open(file_path, 'w') as file:
            file.write(TomlSerializer.dumps(obj))

    @staticmethod
    def load(file_path):
        with open(file_path, 'r') as file:
            return TomlSerializer.loads(file.read())

    @staticmethod
    def dumps(obj):
        return to_toml(serialize(obj))

    @staticmethod
    def loads(string):
        return deserialize(from_toml(string))


