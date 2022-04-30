from lib.factory.create_serializer import create_serializer
from lib.serialization.custom_serialization import serialize
from tests.data_for_test import *

JSON_PATH = "tests/files/my_json.json"
TOML_PATH = "files/my_toml.toml"
YAML_PATH = "files/my_yaml.yaml"
# pytest -rp


def testing_fib():
    serializer = create_serializer("json")
    serializer.dump(fib, JSON_PATH)
    serialized_fib = serializer.load(JSON_PATH)

    assert (serialized_fib(5) == fib(5))


def testing_custom_pow():
    serializer = create_serializer("toml")
    serializer.dump(custom_pow, TOML_PATH)
    serialized_custom_pow = serializer.load(TOML_PATH)

    assert (serialized_custom_pow(2, 4) == custom_pow(2, 4))


def testing_func_with_module():
    serializer = create_serializer("yaml")
    serializer.dump(func_with_module, YAML_PATH)
    serialized_func_with_module = serializer.load(YAML_PATH)

    assert (serialized_func_with_module(3, 4) == func_with_module(3, 4))


def testing_class():
    serializer = create_serializer("json")
    serializer.dump(Person, JSON_PATH)
    serialized_cls = serializer.load(JSON_PATH)

    assert (serialized_cls.type == Person.type)


def testing_obj():
    serializer = create_serializer("json")
    machine = Person(3)
    serializer.dump(machine, JSON_PATH)
    serialized_obj = serializer.load(JSON_PATH)

    assert (serialized_obj.type == machine.type)


def testing_complex_class_and_obj():
    serializer = create_serializer("json")
    serializer.dump(Superman, JSON_PATH)
    serialized_cls = serializer.load(JSON_PATH)
    obj = serialized_cls(6)
    superman = Superman(6)

    assert (superman.get_power() == obj.get_power())


def testing_lambda_func():
    serializer = create_serializer("json")
    lambda_func = lambda x: x * x
    serializer.dump(lambda_func, JSON_PATH)
    serialized_lambda = serializer.load(JSON_PATH)

    assert (lambda_func(2) == serialized_lambda(2))


def testing_inheritance():
    serializer = create_serializer("json")
    serializer.dump(Biba, JSON_PATH)
    serialized_cls = serializer.load(JSON_PATH)

    assert (serialized_cls.type == Biba.type)
    assert (serialized_cls.state == Biba.state)


def testing_primitives():
    int_ = 1
    float_ = 1.1
    none_ = None
    complex_ = complex(1, 1)
    string = "MAKE AMERICA GREAT AGAIN"

    assert (str(serialize(int_)) == "{'**type**': 'int', '**data**': '1'}")
    assert (str(serialize(float_)) == "{'**type**': 'float', '**data**': '1.1'}")
    assert (str(serialize(none_)) == "{'**type**': 'NoneType', '**data**': 'None'}")
    assert (str(serialize(complex_)) == "{'**type**': 'complex', '**data**': '(1+1j)'}")
    assert (str(serialize(string)) == "{'**type**': 'str', '**data**': 'MAKE AMERICA GREAT AGAIN'}")


def testing_complex_types():
    list_ = [["Moon Knight", 8], ["Mark", True], ["Steven", False]]
    tuple_ = (("Moon Knight", 8), ("Mark", True), ("Steven", False))
    bytes_ = b'AMERICA'
    dict_ = {tuple_: "LEGENDA", "WHO?": "Maybe U"}
    assert (str(serialize(list_)) == "{'**type**': 'list', '**data**': [{'**type**': 'list', '**data**': [{"
                                     "'**type**': 'str', '**data**': 'Moon Knight'}, {'**type**': 'int', '**data**': "
                                     "'8'}]}, {'**type**': 'list', '**data**': [{'**type**': 'str', '**data**': "
                                     "'Mark'}, {'**type**': 'bool', '**data**': 'True'}]}, {'**type**': 'list', "
                                     "'**data**': [{'**type**': 'str', '**data**': 'Steven'}, {'**type**': 'bool', "
                                     "'**data**': 'False'}]}]}")
    assert (str(serialize(tuple_)) == "{'**type**': 'tuple', '**data**': [{'**type**': 'tuple', '**data**': [{"
                                      "'**type**': 'str', '**data**': 'Moon Knight'}, {'**type**': 'int', '**data**': "
                                      "'8'}]}, {'**type**': 'tuple', '**data**': [{'**type**': 'str', '**data**': "
                                      "'Mark'}, {'**type**': 'bool', '**data**': 'True'}]}, {'**type**': 'tuple', "
                                      "'**data**': [{'**type**': 'str', '**data**': 'Steven'}, {'**type**': 'bool', "
                                      "'**data**': 'False'}]}]}")
    assert (str(serialize(bytes_)) == "{'**type**': 'bytes', '**data**': [{'**type**': 'int', '**data**': '65'}, "
                                      "{'**type**': 'int', '**data**': '77'}, {'**type**': 'int', '**data**': '69'}, "
                                      "{'**type**': 'int', '**data**': '82'}, {'**type**': 'int', '**data**': '73'}, "
                                      "{'**type**': 'int', '**data**': '67'}, {'**type**': 'int', '**data**': '65'}]}")
    assert (str(serialize(dict_)) == "{'**type**': 'dict', '**data**': [[{'**type**': 'tuple', '**data**': [{"
                                     "'**type**': 'tuple', '**data**': [{'**type**': 'str', '**data**': 'Moon "
                                     "Knight'}, {'**type**': 'int', '**data**': '8'}]}, {'**type**': 'tuple', "
                                     "'**data**': [{'**type**': 'str', '**data**': 'Mark'}, {'**type**': 'bool', "
                                     "'**data**': 'True'}]}, {'**type**': 'tuple', '**data**': [{'**type**': 'str', "
                                     "'**data**': 'Steven'}, {'**type**': 'bool', '**data**': 'False'}]}]}, "
                                     "{'**type**': 'str', '**data**': 'LEGENDA'}], [{'**type**': 'str', '**data**': "
                                     "'WHO?'}, {'**type**': 'str', '**data**': 'Maybe U'}]]}")
