import lib.lib_constants
from lib.serializers.json_serializer import JsonSerializer
from lib.serializers.toml_serializer import TomlSerializer
from lib.serializers.yaml_serializer import YamlSerializer


def create_serializer(received_format: str):
    received_format = received_format.upper()
    if received_format == lib.lib_constants.TOML:
        return TomlSerializer()
    elif received_format == lib.lib_constants.YAML:
        return YamlSerializer()
    elif received_format == lib.lib_constants.JSON:
        return JsonSerializer()
    else:
        raise ValueError(f"Serializer format is wrong: {received_format}")
