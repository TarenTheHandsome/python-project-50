def flatten_gen(nested, isatom=lambda x: not isinstance(x, list)):
    for item in nested:
        if isatom(item):
            yield item
        else:
            yield from flatten_gen(item)


def jack_the_pipper(data, counter):
    level = '*' * counter
    lines = []
    for key in data:
        value = data[key]
        if isinstance(value, dict):
            lines.append([f'{level} {key}: {"{"}', jack_the_pipper(value, counter + 1)])

        else:
            lines.append(f'{level} {key}: {value}')

    return lines


def stylish_formater(structure, counter=1):
    lines = []
    status = {'changed': ' ', 'unchanged': ' ', 'removed': '-', 'added': '+', 'nested': '?'}
    level = '*' * counter

    for line in structure:

        key = line['key']
        key_status = line['key_status']

        if key_status == 'nested':
            lines.append([f'{level} {status[key_status]} {key}: {"{"}',
                          stylish_formater(line['children'], counter + 1)])

        elif key_status == 'changed':
            if isinstance(line['old_value'], dict):
                lines.append([f"{level} {status['removed']} {key}: {'{'}",
                              jack_the_pipper(line['old_value'], counter + 1)])
            else:
                lines.append(f"{level} {status['removed']} {key}: {line['old_value']}")

            if isinstance(line['new_value'], dict):
                lines.append([f"{level} {status['added']} {key}: {'{'}",
                              jack_the_pipper(line['new_value'], counter + 1)])
            else:
                lines.append(f"{level} {status['added']} {key}: {line['new_value']}")


        elif key_status in ['unchanged', 'removed', 'added']:
            if isinstance(line['value'], dict):
                lines.append([f"{level} {status[key_status]} {key}: {'{'}",
                              jack_the_pipper(line['value'], counter + 1)])
            else:
                lines.append(f"{level} {status[key_status]} {key}: {line['value']}")

    return lines



flat = [{'key': 'follow', 'key_status': 'removed', 'value': False}, {'key': 'host', 'key_status': 'unchanged', 'value': 'hexlet.io'}, {'key': 'proxy', 'key_status': 'removed', 'value': '123.234.53.22'}, {'key': 'timeout', 'key_status': 'changed', 'old_value': 50, 'new_value': 20}, {'key': 'verbose', 'key_status': 'added', 'value': True}]
nested = [{'key': 'common', 'key_status': 'nested', 'children': [{'key': 'follow', 'key_status': 'added', 'value': False}, {'key': 'setting1', 'key_status': 'unchanged', 'value': 'Value 1'}, {'key': 'setting2', 'key_status': 'removed', 'value': 200}, {'key': 'setting3', 'key_status': 'changed', 'old_value': True, 'new_value': None}, {'key': 'setting4', 'key_status': 'added', 'value': 'blah blah'}, {'key': 'setting5', 'key_status': 'added', 'value': {'key5': 'value5'}}, {'key': 'setting6', 'key_status': 'nested', 'children': [{'key': 'doge', 'key_status': 'nested', 'children': [{'key': 'wow', 'key_status': 'changed', 'old_value': 'value', 'new_value': 'so much'}]}, {'key': 'key', 'key_status': 'unchanged', 'value': 'value'}, {'key': 'ops', 'key_status': 'added', 'value': 'vops'}]}]}, {'key': 'group1', 'key_status': 'nested', 'children': [{'key': 'baz', 'key_status': 'changed', 'old_value': 'bas', 'new_value': 'bars'}, {'key': 'foo', 'key_status': 'unchanged', 'value': 'bar'}, {'key': 'nest', 'key_status': 'changed', 'old_value': {'key': 'value'}, 'new_value': 'str'}]}, {'key': 'group2', 'key_status': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'key': 'group3', 'key_status': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

print('\n'.join(flatten_gen(stylish_formater(flat))))
print('\n'.join(flatten_gen(stylish_formater(nested))))