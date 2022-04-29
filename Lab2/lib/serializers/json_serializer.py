from lib.parsers.json_parser import to_json, from_json
from lib.serialization.custom_serialization import serialize, deserialize


class JsonSerializer:
    @staticmethod
    def dump(obj, file_path):
        with open(file_path, 'w') as file:
            file.write(JsonSerializer.dumps(obj))

    @staticmethod
    def load(file_path):
        with open(file_path, 'r') as file:
            return JsonSerializer.loads(file_path.read())

    @staticmethod
    def dumps(obj):
        return to_json(serialize(obj))

    @staticmethod
    def loads(string):
        return deserialize(from_json(string))


