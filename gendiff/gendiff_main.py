import itertools
import json
from pathlib import Path
import yaml
from yaml.loader import SafeLoader
# from structuregenerator import make_structure
# from stylishresult import stylish_formater
# from plainresult import plain_formater



def make_dict(file, flag):
    if flag == '.json':
        result = json.load(file)
    elif flag == '.yaml':
        result = yaml.load(file, Loader=SafeLoader)

    return result


def open_file(filepath1: str, filepath2: str) -> str:
    file1 = open(filepath1, 'r')
    dict1 = make_dict(file1, Path(filepath1).suffix)
    file1.close()

    file2 = open(filepath2, 'r')
    dict2 = make_dict(file2, Path(filepath1).suffix)
    file2.close()

    return dict1, dict2


def generate_diff(filepath1, filepath2, flag=''):
    dict1, dict2 = open_file(filepath1, filepath2)
    structure = make_structure(dict1, dict2)

    if flag == 'plain':
        lines = plain_formater(structure)
        print_answer(lines, flag)
    elif flag == 'stylish':
        lines = stylish_formater(structure)
        print_answer(lines, flag)

    return lines


def print_answer(lines, flag):
    if flag == 'plain':
        print('\n'.join(lines))
    elif flag == 'stylish':
        print('\n'.join(["{"] + lines + ["}"]))

# print('\n'.join(['{'] + lines + ['}']))


#Отсюда идет лишний код

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


# print(generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/nested_json1.json',
#               "/Users/roman/Documents/Projects/python-project-50/tests/fixtures/nested_json2.json", flag='stylish'))

def plain_formater(structure):
    lines = []
    all_keys = KEYS[1]

    for all_key in all_keys:

        for structure_key in structure:

            if all_key in structure[structure_key].keys():
                main_dictionary = structure[structure_key]

                if structure_key == 'unchanged' or structure_key == 'added':
                    key_dict = main_dictionary[all_key]
                    lines.append(f"Property {all_key} was added with value: {key_dict['value']}")

                elif structure_key == 'changed':
                    key_dict = main_dictionary[all_key]
                    print(f"Changed dict is {key_dict}")
                    old_value = key_dict['old']
                    new_value = key_dict['new']
                    print(key_dict)
                    lines.append(f"Property {all_key} was updated. "
                                  f"From {old_value['value']} to {new_value['value']}")

                elif structure_key == 'removed':
                    lines.append(f"Property {all_key} was removed")

                elif structure_key == 'nested':
                    lines.append(f"Property {all_key} was added with value: [complex value]")


    return lines

def flatten_gen(nested, isatom=lambda x: not isinstance(x, list)):
    for item in nested:
        if isatom(item):
            yield item
        else:
            yield from flatten_gen(item)


def return_string(dictionary, tab):
    if isinstance(dictionary['value'], dict):
        dictionary['value'] = '{'
    return f"{tab}{dictionary['mark']} {dictionary['key']}: {dictionary['value']}"
def stylish_formater(structure, level=1):
    #наша главная строка
    lines = []

    #формируем пробел
    tab = '..' * level

    #тайми вайми с кейс
    KEYS['check_counter'] += 1
    cycle_counter = KEYS['check_counter']
    all_keys = KEYS[cycle_counter]

    for all_key in all_keys:

        for structure_key in structure:

            if all_key in structure[structure_key].keys():
                #value по ключу
                main_dictionary = structure[structure_key]

                if structure_key == 'nested':
                    #value of all_key
                    child_value = main_dictionary[all_key]

                    if isinstance(child_value['value'], dict):
                        lines.append(stylish_formater(child_value['value'], level=level * 2))
                    lines.insert(-1, return_string(child_value, tab))


                elif structure_key == 'changed':
                    for key in main_dictionary[all_key]:
                        little_dict = main_dictionary[all_key]
                        lines.append(return_string(little_dict[key], tab))

                else:
                    lines.append(return_string(main_dictionary[all_key], tab))

    lines.append(f"{'..' * (level-2)}{'}'}")

    return list(flatten_gen(lines))


# print(generate_diff("../tests/test_data/files/recursive_json1.json",
#                     "../tests/test_data/files/recursive_json2.json", flag='stylish'))