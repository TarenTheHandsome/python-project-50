import itertools
import json
from pathlib import Path
import yaml
from yaml.loader import SafeLoader
from structuregenerator import build_diff
from stylishresult import format_stylish
from plainresult import format_plain
from json_formatter import json_format



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


def generate_diff(filepath1, filepath2, flag='stylish'):
    dict1, dict2 = open_file(filepath1, filepath2)
    structure = build_diff(dict1, dict2)

    if flag == 'plain':
        lines = format_plain(structure)
        print(lines)
    if flag == 'stylish':
        lines = format_stylish(structure)
        print(lines)
    if flag == 'json':
        lines = json_format(structure)
        print(lines)


generate_diff("../tests/test_data/files/recursive_json1.json", "../tests/test_data/files/recursive_json2.json", 'json')

