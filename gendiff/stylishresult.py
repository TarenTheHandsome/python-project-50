
def make_string(key_status, key, value):
    if isinstance(value, dict):
        return f"{key_status} {key}:""{"
    if isinstance(value, list):
        return f"{key_status} {key}:""{"
    else:
        return f"{key_status} {key}:{value}"

def stylish_formater(structure):
    #результирующий список
    lines = []


    status = {'changed': ' ' , 'unchanged': ' ', 'removed': '-', 'added': '+'}

    for line in structure:
        key = line['key']
        value = line['value']
        key_status = line['key_status']
        value_form = line['value_form']

        if value_form == 'simple':
            if line['key_status'] == 'changed':
                lines.append(make_string(status['removed'], key, value['old_value']))
                lines.append(make_string(status['added'], key, value['new_value']))
            else:
                lines.append(make_string(status[key_status], key, value))

        if value_form == 'nested':
            if line['key_status'] == 'changed':
                if isinstance(value, list):
                    lines.append(stylish_formater(value))
                elif isinstance(value, dict):
                    if isinstance(value['old_value'], list):
                        lines.append(stylish_formater(value['old_value']))
                    else:
                        lines.append(make_string(status['removed'], key, value['old_value']))
                    if isinstance(value['new_value'], list):
                        lines.append(stylish_formater(value['new_value']))
                    else:
                        lines.append(make_string(status['added'], key, value['new_value']))
            else:
                 lines.append(stylish_formater(value))

        lines.insert(-1, make_string(status[key_status], key, value))


    return lines

