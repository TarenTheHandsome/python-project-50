import itertools
import json
from pathlib import Path
import yaml
from yaml.loader import SafeLoader


def make_dict(file, flag):
    if flag == '.json':
        result = json.load(file)
    elif flag == '.yaml':
        result = yaml.load(file, Loader=SafeLoader)

    return result


def generate_diff(filepath1: str, filepath2: str) -> str:
    file1 = open(filepath1, 'r')
    dict1 = make_dict(file1, Path(filepath1).suffix)
    file1.close()

    file2 = open(filepath2, 'r')
    dict2 = make_dict(file2, Path(filepath1).suffix)
    file2.close()
    answer = make_diff(dict1, dict2)

    return answer

def diff_recursive(dict1: dict = None, dict2: dict = None, level=0) -> list[str]:
    if dict1 is None and dict2 is not None:
        dict1 = dict2
    elif dict1 is not None and dict2 is None:
        dict2 = dict1

    lines = []
    tab = '   '*level
    total_keys = get_keys(dict1, dict2)
    print(total_keys)

    for key in total_keys:
        symbol = None
        if key in dict1 and key in dict2:
            symbol = ' '
            value = dict1[key]
        elif key in dict1:
            symbol = '-'
            value = dict1[key]
        elif key in dict2:
            symbol = '+'
            value = dict2[key]

        key1 = key in dict1 and isinstance(dict1[key], dict)
        key2 = key in dict2 and isinstance(dict2[key], dict)
        if key1 or key2:
            d1 = dict1[key] if key1 else None
            d2 = dict2[key] if key2 else None

            both_present = key in dict1 and key in dict2
            if both_present and not key1:
                lines.append(f'{tab}- {key}: {dict1[key]}')
                symbol = '+'
            elif both_present and not key2:
                symbol = '-'

            lines.append(f'{tab}{symbol} {key}: {{')
            lines.extend(diff_recursive(d1, d2, level=level + 1))
            lines.append(tab+'  }')

            if both_present and not key2:
                lines.append(f'{tab}+ {key}: {dict2[key]}')

        else:
            if symbol == ' ' and dict1[key] != dict2[key]:
                lines.append(f'{tab}- {key}: {dict1[key]}')
                lines.append(f'{tab}+ {key}: {dict2[key]}')
            else:
                lines.append(f'{tab}{symbol} {key}: {value}')

    return lines


def make_diff(dict1={}, dict2={}):
    result = diff_recursive(dict1, dict2)
    return '\n'.join(['{'] + result + ['}'])


def get_keys(dict1, dict2):
    total_keys_1 = list(dict1.keys())
    total_keys_2 = list(dict2.keys())
    result = []
    counter = 0
    while len(result) < (len(total_keys_1) + len(total_keys_2)):
        if counter <= len(total_keys_1) - 1:
            result.append(total_keys_1[counter])
        if counter <= len(total_keys_2) - 1:
            result.append(total_keys_2[counter])
        counter += 1

    return sorted(list(dict.fromkeys(result)))



