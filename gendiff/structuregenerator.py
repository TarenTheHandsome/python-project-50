import copy


def get_nested_status(value):
    for i in value:
        if isinstance(i, dict):
            return True
    return False


def get_simple_status(value):
    if len(value) == 4:
        if value[1] == value[3]:
            return 'unchanged'
        else:
            if isinstance(value[1], dict) and not isinstance(value[3], dict):
                return 'old_nest'
            elif not isinstance(value[1], dict) and isinstance(value[3], dict):
                return 'new_nest'
            return 'changed'
    else:
        if 'old' in value:
            return 'removed'
        elif 'new' in value:
            return 'added'


def get_status(value):
    if get_nested_status(value):
        return 'nested'
    else:
        return get_simple_status(value)


def build_diff(old={}, new={}):
    structure = []

    all_keys = sorted(set(list(old.keys()) + list(new.keys())))

    workpiece_original = {'key_status': '', 'key': ''}

    for key in all_keys:
        workpiece = copy.deepcopy(workpiece_original)
        workpiece['key'] = key
        value = []

        if key in old:
            value.append('old')
            value.append(old[key])
        if key in new:
            value.append('new')
            value.append(new[key])

        workpiece['key_status'] = get_status(value)

        if workpiece['key_status'] == 'nested':
            status = get_simple_status(value)

            if status == 'added' or status == 'added' or status == 'unchanged':
                workpiece['children'] = build_diff(value[1], {})

            elif status == 'changed':
                workpiece['children'] = build_diff(value[1], value[3])

            elif status == 'old_nest':
                workpiece['children'] = {'old_value': build_diff(value[1], {}), 'new_value': value[3]}

            elif status == 'new_nest':
                workpiece['children'] = {'old_value': value[1], 'new_value': build_diff(value[3], {})}

        elif workpiece['key_status'] == 'added' or workpiece['key_status'] == 'removed' \
                or workpiece['key_status'] == 'unchanged':
            workpiece['value'] = value[1]

        elif workpiece['key_status'] == 'changed':
            workpiece['old_value'] = value[1]
            workpiece['new_value'] = value[3]

        structure.append(workpiece)

    return structure





