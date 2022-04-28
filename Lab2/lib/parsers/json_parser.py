import lib.lib_constants


def to_json(obj: object):
    dictionary_string = str(obj)
    json_string = ""
    size = len(dictionary_string)

    for i in range(size):
        if dictionary_string[i] == '\'':
            if dictionary_string[max(i - 1, 0)].isalpha() and dictionary_string[min(i + 1, size - 1)].isalpha():
                json_string += dictionary_string[i]
            else:
                json_string += '"'
        else:
            json_string += dictionary_string[i]

    return json_string


def from_json(json_string, left, right):
    if json_string[left] == '[':
        while json_string[right] != ']':
            right -= 1

        data = list(from_json(json_string, left + 1, right - 1))
    elif json_string[left] == '{':
        while json_string[right] != '}':
            right -= 1

        left += 14
        data_type = ""
        while json_string[left] != '"' and json_string[left + 1] != ',':
            data_type += json_string[left]
            left += 1

        left += 15
        raw_data = from_json(json_string, left, right - 1)
        data = {lib.lib_constants.TYPE: data_type, lib.lib_constants.DATA: raw_data}
    else:
        data = ""
        #print(json_string)
        #print(left)
        #print(right)
        while left <= right:
            data += json_string[left]
            left += 1

    return data
