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
        balance = 1
        data = []
        prev_left = left + 1
        el_balance = 0

        for i in range(left + 1, right + 1):
            if json_string[i] == '[':
                balance += 1
                el_balance += 1
            elif json_string[i] == ']':
                balance -= 1
                el_balance -= 1

            if json_string[i] == '{':
                el_balance += 1
            elif json_string[i] == '}':
                el_balance -= 1

            if el_balance == 0 and prev_left < i:
                data.append(from_json(json_string, prev_left, i + 1))
                prev_left = i + 3

            if balance == 0:
                break
    elif json_string[left] == '{':
        balance = 1
        data = {}
        el_balance = 0
        key_board = left + 1
        value_board = -1

        for i in range(left + 1, right + 1):
            if json_string[i] == '{':
                balance += 1
                el_balance += 1
            elif json_string[i] == '}':
                balance -= 1
                el_balance -= 1

            if json_string[i] == '[':
                el_balance += 1
            elif json_string[i] == ']':
                el_balance -= 1

            if el_balance == 0 and json_string[i] == ':':
                value_board = i

            if el_balance == 0 and value_board != -1 and (json_string[i + 1] == ',' or json_string[i + 1] == '}'):
                key = from_json(json_string, key_board, value_board - 1)
                value = from_json(json_string, value_board + 2, i)

                if isinstance(key, str):
                    key = key[1: -1]
                if isinstance(value, str):
                    value = value[1: -1]

                data[key] = value
                value_board = -1
                key_board = i + 3

            if balance == 0:
                break
    else:
        data = ""
        while left <= right:
            data += json_string[left]
            left += 1

    return data
