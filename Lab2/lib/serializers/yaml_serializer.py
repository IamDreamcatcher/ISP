from lib.parsers.yaml_parser import convert_to_yaml, convert_from_yaml
from lib.serialization.custom_serialization import serialize, deserialize


class YamlSerializer:
    @staticmethod
    def dump(obj, file_path):
        with open(file_path, 'w') as file:
            file.write(YamlSerializer.dumps(obj))

    @staticmethod
    def load(file_path):
        with open(file_path, 'r') as file:
            return YamlSerializer.loads(file.read())

    @staticmethod
    def dumps(obj):
        return convert_to_yaml(serialize(obj))

    @staticmethod
    def loads(string):
        return deserialize(convert_from_yaml(string))


