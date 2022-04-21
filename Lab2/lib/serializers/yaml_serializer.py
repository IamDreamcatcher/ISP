from lib.serializers.abstract_serializer import AbstractSerializer
from lib.parsers.yaml_parser import to_yaml, from_yaml
from lib.serialization.custom_serialization import serialize, deserialize


class YamlSerializer(AbstractSerializer):
    @staticmethod
    def dump(obj, file_path):
        with open(file_path, 'w') as file:
            file.write(YamlSerializer.dumps(obj))

    @staticmethod
    def load(file_path):
        with open(file_path, 'r') as file:
            return YamlSerializer.loads(file_path.read())

    @staticmethod
    def dumps(obj):
        return to_yaml(serialize(obj))

    @staticmethod
    def loads(string):
        return deserialize(from_yaml(string))


