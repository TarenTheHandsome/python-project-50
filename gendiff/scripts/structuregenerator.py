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
