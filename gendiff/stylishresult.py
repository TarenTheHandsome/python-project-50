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
        base_indent = ' ' * (depth * INDENT_SIZE)
        key_indent = base_indent + ' ' * 2
        current_indent = f"{key_indent}"

        if status == 'nested':
            child = format_stylish(node['children'], depth + 1)
            lines.append(f"{key_indent}  {key}: {child}")
            continue

        if status == 'changed':
            old_line = stringify(node['old_value'], depth + 1)
            new_line = stringify(node['new_value'], depth + 1)
            lines.append(f"{key_indent}- {key}: {old_line}")
            lines.append(f"{key_indent}+ {key}: {new_line}")
            continue

        mark = NODE_MARK[status]
        value = stringify(node.get('value'), depth + 1)
        lines.append(f"{current_indent}{mark} {key}: {value}")

    closing_indent = ' ' * (depth * INDENT_SIZE)
    lines.append(f"{closing_indent}}}")
    return '\n'.join(lines)

