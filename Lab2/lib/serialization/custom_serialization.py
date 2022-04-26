import inspect
from types import CodeType, FunctionType

import lib.lib_constants


def serialize(obj):
    obj_type = type(obj)
    obj_type_name = obj_type.__name__
    if inspect.isclass(obj):
        obj_type_name = "class"
    if inspect.ismodule(obj):
        obj_type_name = "module"

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
        case "function":
            data[lib.lib_constants.DATA] = serialize_function(obj)
        case "class":
            data[lib.lib_constants.DATA] = serialize_class(obj)
        case "module":
            data[lib.lib_constants.DATA] = {"module": obj.__name__}
        case _:
            if hasattr(obj, "__dict__"):
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
                elif name in globals_inst and type(globals_inst[name]).__name__ != "builtin_function_or_method" \
                        and name not in __builtins__:
                    data[lib.lib_constants.GLOBAL][name] = serialize(globals_inst[name])

    return data


def serialize_class(obj):
    if obj.__name__ == "object":
        return
    data = {"**name**": serialize(obj.__name__)}
    hierarchy = ()
    for o in obj.__bases__:
        base_class = serialize_class(o)
        if base_class is not None:
            hierarchy += (base_class,)

    data["**hierarchy**"] = serialize(hierarchy)
    data["**dict**"] = serialize(dict(obj.__dict__))

    return data


def serialize_class_obj(obj):
    serialized_class = serialize_class(obj.__class__)
    serialized_obj_dict = serialize(obj.__dict__)
    return {
        "**class**": serialized_class,
        "**obj_dict**": serialized_obj_dict
    }


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
    if obj.get(lib.lib_constants.TYPE):
        obj_type_name = obj[lib.lib_constants.TYPE]
    else:
        obj_type_name = "special_dict"

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
            for o in obj[lib.lib_constants.DATA]:
                data[deserialize(o[0])] = deserialize(o[1])
        case "function":
            data = deserialize_function(obj[lib.lib_constants.DATA])
        case "class":
            data = deserialize_class(obj[lib.lib_constants.DATA])
        case "class_object":
            data = deserialize_class_object(obj[lib.lib_constants.DATA])
        case "module":
            data = __import__(obj[lib.lib_constants.DATA]["module"])
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

    if func_attributes["__name__"] in function.__getattribute__(lib.lib_constants.GLOBAL):
        function.__getattribute__(lib.lib_constants.GLOBAL)[func_attributes["__name__"]] = function

    return function


def deserialize_class(obj):
    name = deserialize(obj["**name**"])
    hierarchy = deserialize(obj["**hierarchy**"])
    dictionary = deserialize(obj["**dict**"])

    return type(name, hierarchy, dictionary)


def deserialize_class_object(obj):
    deserialized_class = deserialize_class(obj["**class**"])
    deserialized_obj_dict = deserialize(obj["**obj_dict**"])

    data = deserialized_class()
    data.__dict__ = deserialized_obj_dict

    return data


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


def get_primitive(obj, obj_type_name):
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
