import lib.lib_constants


def serialize(obj):
    data = {}
    obj_type = type(obj)
    obj_type_name = obj.__name__
    if obj_type in (int, float, str, bool, complex):
        return obj
    elif obj_type in (tuple, list):
        data[lib.lib_constants.TYPE] = obj_type_name
        data[lib.lib_constants.VALUE] = [serialize(cur) for cur in obj]


def deserialize(obj):
    pass
