import json


def json_format(structure):
    return json.dumps(structure, separators=(',', ':'), indent=4)
