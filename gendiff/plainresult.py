
def flatten_gen(nested, isatom=lambda x: not isinstance(x, list)):
    for item in nested:
        if isatom(item):
            yield item
        else:
            yield from flatten_gen(item)

def find_key(structure):

    keys = []
    if isinstance(structure['value'], list) and 'old_value' in structure['value']:
        keys.append([])
    elif isinstance(structure['value'], dict):
        keys.append(find_key(structure['value']))

    keys.insert(-1, structure['key'])
    return list(flatten_gen(keys))

def find_value(structure):
    #переименовать переменную
    value_collecter = []
    if isinstance(structure, dict):
        if not isinstance(structure['value'], dict):
            value_collecter.append(structure['value'])
        # elif isinstance(structure['value'], list):
        #     value_collecter.append([structure['value']['old_value'], structure['value']['new_value']])

        else:
            value_collecter.append(find_value(structure['value']))

    return list(flatten_gen(value_collecter))

def plain_formater(structure):
    answer = []
    print(answer)
    for line in structure:
        keys = find_key(line)
        value = find_value(line)
        if line['key_status'] == 'removed':
            answer.append(f"'{'.'.join(keys)}' was removed")
        elif line['key_status'] == 'added':
            answer.append(f"'{'.'.join(keys)}' was added with value:'{''.join(value)}'")
        elif line['key_status'] == 'changed':
            answer.append(f"'{'.'.join(keys)}' was updated. From value: '{value[0]}' to '{value[1]}'")
        elif line['key_status'] == 'unchanged':
            answer.append(f"'{'.'.join(keys)}' was unchanged with value: '{''.join(value)}'")

    return answer

def recursive_stuff(structure, index=0):
    answer = []

    for line in structure:
        if isinstance(line, dict):

            if isinstance(line['value'], list):
                answer.append(recursive_stuff(line['value'], index + 1))
                answer.insert(-1, {line['key']: f'index {index}'})
            else:
                answer.append({line['key']: line['value']})

    return answer











