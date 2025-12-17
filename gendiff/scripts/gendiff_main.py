import json
from pathlib import Path
import yaml
from yaml.loader import SafeLoader
from structuregenerator import build_diff
from gendiff.formatters.stylis_formatter import format_stylish
from gendiff.formatters.plain_formatter import format_plain
from gendiff.formatters.json_formatter import json_format

#разобраться с названиями функций

def make_dict(file, flag) -> dict:
    if flag == '.json':
        dictionary = json.load(file)
    elif flag == '.yaml' or flag == '.yml':
        dictionary = yaml.load(file, Loader=SafeLoader)

    return dictionary


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

    if flag == 'stylish':
        lines = format_stylish(structure)

    if flag == 'json':
        lines = json_format(structure)


    return lines


