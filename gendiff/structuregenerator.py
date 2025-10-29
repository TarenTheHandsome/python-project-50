import copy


def build_diff(old={}, new={}):
    structure = []

    all_keys = sorted(set(list(old.keys()) + list(new.keys())))

    workpiece_original = {'key_status': '', 'key': ''}

    for key in all_keys:
        workpiece = copy.deepcopy(workpiece_original)
        workpiece['key'] = key

        if key not in old:
            value = new[key]

            if isinstance(value, dict):
                workpiece['key_status'] = 'nested'
                workpiece['children'] = build_diff(value, {})
            else:
                workpiece['key_status'] = 'added'
                workpiece['value'] = value

        if key not in new:
            value = old[key]

            if isinstance(value, dict):
                workpiece['key_status'] = 'nested'
                workpiece['children'] = build_diff(value, {})
            else:
                workpiece['key_status'] = 'removed'
                workpiece['value'] = value

        if key in old and key in new:
            old_value = old[key]
            new_value = new[key]

            if old_value == new_value:
                if isinstance(old_value, dict):
                    workpiece['key_status'] = 'nested'
                    workpiece['children'] = build_diff(old_value, {})
                else:
                    workpiece['key_status'] = 'unchanged'
                    workpiece['value'] = old_value

            else:
                if isinstance(old_value, dict):
                    workpiece['key_status'] = 'nested'
                    if isinstance(new_value, dict):
                        workpiece['children'] = build_diff(old_value, new_value)

                    else:
                        workpiece['children'] = {'old_value': build_diff(old_value, {}), 'new_value': new_value}

                elif isinstance(new_value, dict) and not isinstance(old_value, dict):
                    workpiece['key_status'] = 'nested'
                    workpiece['children'] = {'old_value': old_value, 'new_value': build_diff(new_value, {})}

                elif not isinstance(old_value, dict) and not isinstance(new_value, dict):
                    workpiece['key_status'] = 'changed'
                    workpiece['old_value'] = old_value
                    workpiece['new_value'] = new_value

        structure.append(workpiece)

    return structure