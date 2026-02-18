def stringify(value):
    """Format value for plain output. Only strings are quoted."""
    if isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'

    if value is None:
        return 'null'

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


def build_path(parent, key):
    return f"{parent}.{key}" if parent else key


def format_plain(diff, nes_key='') -> str:
    lines = []

    for node in diff:
        key = node['key']
        status = node['key_status']
        value = node.get('value')
        child_path = build_path(nes_key, key)

        if status == 'nested':
            children = node.get('children')
            lines.append(format_plain(children, child_path))

        if status == 'added':
            lines.append(f"Property '{child_path}' was added with value: {stringify(value)}")

        if status == 'removed':
            lines.append(f"Property '{child_path}' was removed")

        if status == 'changed':
            old_value = node.get('old_value')
            new_value = node.get('new_value')
            lines.append(f"Property '{child_path}' was updated."
                          f" From {stringify(old_value)} to {stringify(new_value)}")

    return '\n'.join(lines)
