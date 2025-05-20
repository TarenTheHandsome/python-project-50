KEYS = {'make_counter': 0, 'check_counter': 0}


def return_dict(mark, key, value):
    return {'mark': mark, 'key': key, 'value': value}


def make_structure(dict1, dict2, level=0):

    #создаем список всех ключей в двух словарях
    all_keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))

    KEYS['make_counter'] += 1

    KEYS.update({KEYS['make_counter']: all_keys})

    structure = {'unchanged': {},
                'changed': {},
                'added': {},
                'removed': {},
                'nested': {}}

    for key in all_keys:

        if (key in dict1 and isinstance(dict1[key], dict)) \
                or (key in dict2 and isinstance(dict2[key], dict)):

            #есть ли ключ в обоих словарях
            if key in dict1 and key in dict2:
                # проверяем оба ли значения являются словарями

                if not (isinstance(dict1[key], dict) and isinstance(dict2[key], dict)):
                    old_dict = {**{'mark': '-', 'key': key, 'value': dict1[key]}}
                    new_dict = {**{'mark': '+', 'key': key, 'value': dict2[key]}}


                    structure['changed'].update({key: {'old': old_dict, 'new': new_dict}})
                else:
                    mark = ' '
                    result = make_structure(dict1[key], dict2[key])
                    value = {**{'mark': mark, 'key': key, 'value': result}}
                    structure['nested'].update({key: value})
                    #

            else:
                if key in dict1:
                    if level == 0:
                        mark = '-'
                    else:
                        mark = ' '
                    #рекурсия
                    result = make_structure(dict1[key], {}, level=level + 1)

                else:

                    if level == 0:
                        mark = '+'
                    else:
                        mark = ' '
                    # рекурсия
                    result = make_structure({}, dict2[key],  level=level + 1)

                structure['nested'].update({key: {**{'mark': mark, 'key': key, 'value': result}}})


        elif key in dict1 and key in dict2:

                if dict1[key] == dict2[key]:
                    structure['unchanged'].update({key: {**{'mark': ' ', 'key': key, 'value': dict2[key]}}})
                else:
                    old_dict = {**{'mark': '-', 'key': key, 'value': dict1[key]}}
                    new_dict = {**{'mark': '+', 'key': key, 'value': dict2[key]}}
                    structure['changed'].update({key: {'old': old_dict, 'new': new_dict}})

        #проверяем добавления
        elif key not in dict1 and key in dict2:
            if level == 0:
                mark = '+'
            else:
                mark = ' '
            structure['added'].update({key: {**{'mark': mark, 'key': key, 'value': dict2[key]}}})

        # проверяем удаление
        elif key in dict1 and key not in dict2:
            if level == 0:
                mark = '-'
            else:
                mark = ' '
            structure['removed'].update({key: {**{'mark': mark, 'key': key, 'value': dict1[key]}}})

    return structure


