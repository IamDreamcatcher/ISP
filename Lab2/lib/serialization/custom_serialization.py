import lib.lib_constants


def serialize(obj):
    data = {}
    obj_type = type(obj)
    obj_type_name = obj_type.__name__
    data[lib.lib_constants.TYPE] = obj_type_name

    match obj_type_name:
        case 'int' | 'float' | 'bool' | 'complex' | 'str':
            data[lib.lib_constants.VALUE] = obj
            return data
        case 'list' | 'tuple' | 'bytes':
            data[lib.lib_constants.VALUE] = [serialize(cur) for cur in obj]
            return data
        case 'dict':
            data[lib.lib_constants.VALUE] = []
            for cur_key, cur_value in obj.items():
                key = serialize(cur_key)
                value = serialize(cur_value)
                data[lib.lib_constants.VALUE].append([key, value])
            return data
        case 'function':
            data[lib.lib_constants.VALUE] = serialize_function()
            return data
        case 'type':
            data[lib.lib_constants.VALUE] = serialize_class()
        case _:
            pass

    print(obj_type_name)

    return data


def serialize_function():
    pass


def serialize_class():
    pass


def deserialize(obj):
    pass
