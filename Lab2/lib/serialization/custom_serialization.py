import inspect
from types import CodeType, FunctionType

import lib.lib_constants


def serialize(obj):
    obj_type = type(obj)
    obj_type_name = obj_type.__name__
    data = {lib.lib_constants.TYPE: obj_type_name}

    match obj_type_name:
        case "int" | "float" | "bool" | "complex" | "str" | "NoneType":
            data[lib.lib_constants.DATA] = obj
        case "list" | "tuple" | "bytes":
            data[lib.lib_constants.DATA] = [serialize(cur) for cur in list(obj)]
        case "dict":
            data[lib.lib_constants.DATA] = []

            for cur_key, cur_value in obj.items():
                key = serialize(cur_key)
                value = serialize(cur_value)
                data[lib.lib_constants.DATA].append([key, value])
        case "function" | "method":
            data[lib.lib_constants.DATA] = serialize_function(obj)
        case "type":
            data[lib.lib_constants.DATA] = serialize_class(obj)
        case _:
            if inspect.ismodule(obj):
                serialize_instance(obj)
            elif hasattr(obj, "__dict__"):
                data[lib.lib_constants.TYPE] = "class_object"
                data[lib.lib_constants.DATA] = serialize_class_obj(obj)
            else:
                data[lib.lib_constants.DATA] = serialize_instance(obj)

    return data


def serialize_function(obj):
    data = {}
    content = inspect.getmembers(obj)

    for o in content:
        if o[0] not in lib.lib_constants.FUNCTION_ATTRIBUTES:
            continue
        data[o[0]] = serialize(o[1])

        if o[0] == lib.lib_constants.CODE:
            data[lib.lib_constants.GLOBAL] = {}
            names = o[1].__getattribute__("co_names")
            globals_inst = obj.__getattribute__("__globals__")
            func_name = obj.__name__

            for name in names:
                if name == func_name:
                    data[lib.lib_constants.GLOBAL][name] = serialize(func_name)
                elif name in globals_inst and name not in __builtins__ and not inspect.ismodule(name):
                    data[lib.lib_constants.GLOBAL][name] = serialize(globals_inst[name])

    return data


def serialize_class(obj):
    pass


def serialize_class_obj(obj):
    pass


def serialize_instance(obj):
    data = {}
    for o in inspect.getmembers(obj):
        if not callable(o[1]):
            data[o[0]] = serialize(o[1])

    return data


def deserialize(obj):
    obj_type = type(obj)

    if obj_type != dict:
        return obj

    obj_type_name = obj[lib.lib_constants.TYPE]
    match obj_type_name:
        case "int" | "float" | "bool" | "complex" | "str" | "NoneType":
            return get_primitive(obj[lib.lib_constants.DATA], obj_type_name)
        case "list":
            data = [deserialize(cur) for cur in obj[lib.lib_constants.DATA]]
        case "tuple":
            data = [deserialize(cur) for cur in obj[lib.lib_constants.DATA]]
            data = tuple(data)
        case "bytes":
            data = [deserialize(cur) for cur in obj[lib.lib_constants.DATA]]
            data = bytes(data)
        case "dict":
            data = {}
            for o in obj:
                data[deserialize(o[0])] = deserialize(o[1])
        case "function":
            data = deserialize_function(obj[lib.lib_constants.DATA])
        case "type":
            data = deserialize_class(obj[lib.lib_constants.DATA])
        case "class_object":
            data = deserialize_class_object(obj[lib.lib_constants.DATA])
        case _:
            data = {}
            for key, value in obj.items():
                data[key] = deserialize(value)
    return data


def deserialize_function(obj):
    code_data = []
    global_data = {}
    func_attributes = {}

    for key, value in obj.items():
        if key == lib.lib_constants.GLOBAL:
            global_data = get_global_data(value)
        elif key == lib.lib_constants.CODE:
            code_data = get_code_data(obj[key][lib.lib_constants.DATA])
        else:
            func_attributes[key] = deserialize(value)

    func_code = [CodeType(*code_data), global_data, func_attributes["__name__"],
                 func_attributes["__defaults__"], func_attributes["__closure__"]]

    function = FunctionType(*func_code)
    if function.__name__ in function.__getattribute__(lib.lib_constants.GLOBAL):
        function.__getattribute__(lib.lib_constants.GLOBAL)[function.__name__] = function

    return function


def deserialize_class(obj):
    pass


def deserialize_class_object(obj):
    pass


def get_global_data(obj):
    global_data = {}

    for key, value in obj.items():
        global_data[key] = deserialize(value)

    return global_data


def get_code_data(obj):
    code_data = []

    for current_arg in lib.lib_constants.OBJECT_ARGS:
        code_data.append(deserialize(obj[current_arg]))

    return code_data


def get_primitive(obj: object, obj_type_name: str):
    match obj_type_name:
        case "int":
            return int(obj)
        case "float":
            return float(obj)
        case "bool":
            return bool(obj)
        case "complex":
            return complex(obj)
        case "str":
            return str(obj)
        case _:
            return None
