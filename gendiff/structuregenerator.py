
def build_diff(old={}, new={}):
    structure = []

    all_keys = sorted(old.keys() | new.keys())

    for key in all_keys:
        workpiece = {'key': key}


        if key not in old:
            workpiece['key_status'] = 'added'
            workpiece['value'] = new[key]

        elif key not in new:
            workpiece['key_status'] = 'removed'
            workpiece['value'] = old[key]

        else:
            old_value = old[key]
            new_value = new[key]

            if isinstance(old_value, dict) and isinstance(new_value, dict):
                workpiece['key_status'] = 'nested'
                workpiece['children'] = build_diff(old_value, new_value)

            elif old_value == new_value:
                workpiece['key_status'] = 'unchanged'
                workpiece['value'] = old_value

            else:
                workpiece['key_status'] = 'changed'
                workpiece['old_value'] = old_value
                workpiece['new_value'] = new_value


        structure.append(workpiece)

    return structure



flat1 = {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
flat2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}

print(build_diff(flat1, flat2))

new1 = {'common': {'setting1': 'Value 1', 'setting2': 200, 'setting3': True, 'setting6': {'key': 'value', 'doge': {'wow': 'value'}}}, 'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}}, 'group2': {'abc': 12345, 'deep': {'id': 45}}}
new2 = {'common': {'follow': False, 'setting1': 'Value 1', 'setting3': None, 'setting4': 'blah blah', 'setting5': {'key5': 'value5'}, 'setting6': {'key': 'value', 'ops': 'vops', 'doge': {'wow': 'so much'}}}, 'group1': {'foo': 'bar', 'baz': 'bars', 'nest': 'str'}, 'group3': {'deep': {'id': {'number': 45}}, 'fee': 100500}}

print(build_diff(new1, new2))

