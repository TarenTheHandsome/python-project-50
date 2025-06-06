import itertools
import json
from pathlib import Path
import yaml
from yaml.loader import SafeLoader
from structuregenerator import make_structure
from stylishresult import stylish_formater
from plainresult import plain_formater



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




# print(generate_diff("../tests/test_data/files/recursive_json1.json",
#                     "../tests/test_data/files/recursive_json2.json", flag='stylish'))