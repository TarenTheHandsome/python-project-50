import json
from pathlib import Path
import yaml
from yaml.loader import SafeLoader
from gendiff.scripts.structuregenerator import build_diff
from gendiff.formatters.stylis_formatter import format_stylish
from gendiff.formatters.plain_formatter import format_plain
from gendiff.formatters.json_formatter import json_format

#разобраться с названиями функций

def make_dict(file, flag) -> dict:
    if flag == '.json':
        dictionary = json.loads(file)
    elif flag == '.yaml' or flag == '.yml':
        dictionary = yaml.load(file, Loader=SafeLoader)

    return dictionary


def open_file(file_path: str) -> str:
    with open(file_path, encoding='utf-8') as file:
        return file.read()


def make_dicts(*file_paths: str) -> dict:
    dicts = []
    for file_path in file_paths:
        dicts.append(make_dict(open_file(file_path), Path(file_path).suffix))

    return dicts


def generate_diff(filepath1, filepath2, flag='stylish'):
    dict1, dict2 = make_dicts(filepath1, filepath2)
    structure = build_diff(dict1, dict2)

    if flag == 'plain':
        lines = format_plain(structure)

    if flag == 'stylish':
        lines = format_stylish(structure)

    if flag == 'json':
        lines = json_format(structure)


    return lines

