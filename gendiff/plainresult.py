def stringify(value):

    if isinstance(value, dict):
        return '[сomplex value]'

    if value is None:
        return 'null'

    if isinstance(value, bool):
        return str(value).lower()

    return f"'{value}'"


def format_plain(diff, nes_key='') -> str:
    lines = []

    for node in diff:
        key = node['key']
        status = node['key_status']
        value = node.get('value')


        if status == 'nested':
            children = node.get('children')
            lines.append(format_plain(children, nes_key+f'.{key}'))

        if status == 'added':
            lines.append(f"Property '{nes_key}.{key}' was added with value: {stringify(value)}")

        if status == 'removed':
            lines.append(f"Property '{nes_key}.{key}' was removed")

        if status == 'changed':
            old_value = node.get('old_value')
            new_value = node.get('new_value')
            lines.append(f"Property '{nes_key}.{key}' was updated."
                          f" From {stringify(old_value)} to {stringify(new_value)}")


    return '\n'.join(lines)

flat = [{'key': 'follow', 'key_status': 'removed', 'value': False}, {'key': 'host', 'key_status': 'unchanged', 'value': 'hexlet.io'}, {'key': 'proxy', 'key_status': 'removed', 'value': '123.234.53.22'}, {'key': 'timeout', 'key_status': 'changed', 'old_value': 50, 'new_value': 20}, {'key': 'verbose', 'key_status': 'added', 'value': True}]
nested = [{'key': 'common', 'key_status': 'nested', 'children': [{'key': 'follow', 'key_status': 'added', 'value': False}, {'key': 'setting1', 'key_status': 'unchanged', 'value': 'Value 1'}, {'key': 'setting2', 'key_status': 'removed', 'value': 200}, {'key': 'setting3', 'key_status': 'changed', 'old_value': True, 'new_value': None}, {'key': 'setting4', 'key_status': 'added', 'value': 'blah blah'}, {'key': 'setting5', 'key_status': 'added', 'value': {'key5': 'value5'}}, {'key': 'setting6', 'key_status': 'nested', 'children': [{'key': 'doge', 'key_status': 'nested', 'children': [{'key': 'wow', 'key_status': 'changed', 'old_value': 'value', 'new_value': 'so much'}]}, {'key': 'key', 'key_status': 'unchanged', 'value': 'value'}, {'key': 'ops', 'key_status': 'added', 'value': 'vops'}]}]}, {'key': 'group1', 'key_status': 'nested', 'children': [{'key': 'baz', 'key_status': 'changed', 'old_value': 'bas', 'new_value': 'bars'}, {'key': 'foo', 'key_status': 'unchanged', 'value': 'bar'}, {'key': 'nest', 'key_status': 'changed', 'old_value': {'key': 'value'}, 'new_value': 'str'}]}, {'key': 'group2', 'key_status': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'key': 'group3', 'key_status': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

print(format_plain(flat))
print(format_plain(nested))