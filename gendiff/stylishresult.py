INDENT_SIZE = 4
NODE_MARK = {
    'unchanged': ' ',
    'changed': ('-', '+'),
    'removed': '-',
    'added': '+',
    'nested': ' '
}


def stringify(value, depth) -> str:
    if isinstance(value, dict):
        lines = ['{']

        for k, v in value.items():
            indent = ' ' * ((depth + 1) * INDENT_SIZE)
            lines.append(f"{indent}{k}: {stringify(v, depth + 1)}")
        closing_indent = ' ' * (depth * INDENT_SIZE)
        lines.append(f"{closing_indent}}}")
        return '\n'.join(lines)

    if value is None:
        return 'null'

    if isinstance(value, bool):
        return str(value).lower()

    return str(value)


def format_stylish(diff, depth=0) -> str:
    lines = ['{']

    for node in diff:
        key = node['key']
        status = node['key_status']
        indent = ' ' * (INDENT_SIZE + depth * 2)
        current_indent = f"{indent}"

        if status == 'nested':
            child = format_stylish(node['children'], depth + 1)
            lines.append(f"{indent[:-2]}  {key}: {child}")
            continue

        if status == 'changed':
            old_line = stringify(node['old_value'], depth + 1)
            new_line = stringify(node['new_value'], depth + 1)
            lines.append(f"{indent}- {key}: {old_line}")
            lines.append(f"{indent}+ {key}: {new_line}")
            continue

        mark = NODE_MARK[status]
        value = stringify(node.get('value'), depth + 1)
        lines.append(f"{current_indent}{mark} {key}: {value}")

    closing_indent = ' ' * (depth * INDENT_SIZE)
    lines.append(f"{closing_indent}}}")
    return '\n'.join(lines)


flat = [{'key': 'follow', 'key_status': 'removed', 'value': False}, {'key': 'host', 'key_status': 'unchanged', 'value': 'hexlet.io'}, {'key': 'proxy', 'key_status': 'removed', 'value': '123.234.53.22'}, {'key': 'timeout', 'key_status': 'changed', 'old_value': 50, 'new_value': 20}, {'key': 'verbose', 'key_status': 'added', 'value': True}]
nested = [{'key': 'common', 'key_status': 'nested', 'children': [{'key': 'follow', 'key_status': 'added', 'value': False}, {'key': 'setting1', 'key_status': 'unchanged', 'value': 'Value 1'}, {'key': 'setting2', 'key_status': 'removed', 'value': 200}, {'key': 'setting3', 'key_status': 'changed', 'old_value': True, 'new_value': None}, {'key': 'setting4', 'key_status': 'added', 'value': 'blah blah'}, {'key': 'setting5', 'key_status': 'added', 'value': {'key5': 'value5'}}, {'key': 'setting6', 'key_status': 'nested', 'children': [{'key': 'doge', 'key_status': 'nested', 'children': [{'key': 'wow', 'key_status': 'changed', 'old_value': 'value', 'new_value': 'so much'}]}, {'key': 'key', 'key_status': 'unchanged', 'value': 'value'}, {'key': 'ops', 'key_status': 'added', 'value': 'vops'}]}]}, {'key': 'group1', 'key_status': 'nested', 'children': [{'key': 'baz', 'key_status': 'changed', 'old_value': 'bas', 'new_value': 'bars'}, {'key': 'foo', 'key_status': 'unchanged', 'value': 'bar'}, {'key': 'nest', 'key_status': 'changed', 'old_value': {'key': 'value'}, 'new_value': 'str'}]}, {'key': 'group2', 'key_status': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'key': 'group3', 'key_status': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

# print(format_stylish(flat))
print(format_stylish(nested))
