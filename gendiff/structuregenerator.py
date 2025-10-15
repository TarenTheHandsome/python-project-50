import copy

def find_key_status(key, old, new):
    if key not in old and key in new:
        return 'added'
    elif key in old and key not in new:
        return 'removed'
    elif key in old and key in new:
        if old[key] != new[key]:
            return 'changed'
        return 'unchanged'


def find_value_form(key, old, new):
    if (key in old and isinstance(old[key], dict)) \
            or (key in new and isinstance(new[key], dict)):
        return 'nested'
    return 'simple'


def check_value(value):
    if len(value) == 1:
        return value[0]
    else:
        if value[0] == value[1]:
            return value[0]
        return value


def get_value(key, old, new):
    value = []
    if key in old:
        value.append(old[key])
    if key in new:
        value.append(new[key])

    return check_value(value)


def structure_generator(old={}, new={}):
    if not isinstance(old, dict):
        old = {}
    if not isinstance(new, dict):
        new = {}
    structure = []
    workpiece_original = {'value_form': 'simple', 'key_status': 'unchanged',
                  'key': '', 'value': ''}

    all_keys = sorted(set(list(old.keys()) + list(new.keys())))

    for key in all_keys:
        workpiece = copy.deepcopy(workpiece_original)
        workpiece['key'] = key
        workpiece['value_form'] = find_value_form(key, old, new)
        workpiece['key_status'] = find_key_status(key, old, new)
        value = get_value(key, old, new)

        if workpiece['value_form'] == 'simple':
            if workpiece['key_status'] == 'changed':
                workpiece['value'] = {'old_value': value[0], 'new_value': value[1]}
            else:
                workpiece['value'] = value

        elif workpiece['value_form'] == 'nested':
            if workpiece['key_status'] == 'changed':
                if isinstance(value[0], dict) and isinstance(value[1], dict):
                    workpiece['value'] = structure_generator(value[0], value[1])

                elif not isinstance(value[0], dict) and isinstance(value[1], dict):
                    old_value = value[0]
                    new_value = structure_generator({}, value[1])
                    workpiece['value'] = {'old_value': old_value, 'new_value': new_value}

                elif isinstance(value[0], dict) and not isinstance(value[1], dict):
                    old_value = structure_generator({}, value[0])
                    new_value = value[1]
                    workpiece['value'] = {'old_value': old_value, 'new_value': new_value}


            else:
                workpiece['value'] = structure_generator(value)


        structure.append(workpiece)


    return structure




