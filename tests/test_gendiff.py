import os
from gendiff import generate_diff
from gendiff.scripts.gendiff_main import open_file


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, 'test_data', 'files')
EXPECTED_DIR = os.path.join(BASE_DIR, 'test_data', 'expected_result')


def test_smoke_json():
    generate_diff(
        os.path.join(FILES_DIR, 'empty_json.json'),
        os.path.join(FILES_DIR, 'empty_json.json')
    )


def test_smoke_yaml():
    generate_diff(
        os.path.join(FILES_DIR, 'empty_yaml.yaml'),
        os.path.join(FILES_DIR, 'empty_yaml.yaml'),
    )


def test_flat_json_content_added():
    actual = generate_diff(
        os.path.join(FILES_DIR, 'flat_json1.json'),
        os.path.join(FILES_DIR, 'flat_json2.json'),
        formatter='stylish',
    )
    expected = open_file(os.path.join(EXPECTED_DIR, 'flat_stylish.txt'))

    assert actual == expected


def test_flat_yaml_content_added():
    actual = generate_diff(
        os.path.join(FILES_DIR, 'flat_yaml1.yaml'),
        os.path.join(FILES_DIR, 'flat_yaml2.yaml'),
        formatter='stylish',
    )
    expected = open_file(os.path.join(EXPECTED_DIR, 'flat_stylish.txt'))

    assert actual == expected


def test_nested_json():
    actual = generate_diff(
        os.path.join(FILES_DIR, 'recursive_json1.json'),
        os.path.join(FILES_DIR, 'recursive_json2.json'),
        formatter='stylish',
    )
    expected = open_file(os.path.join(EXPECTED_DIR, 'recursive_stylist.txt'))

    assert actual == expected


def test_nested_yaml():
    actual = generate_diff(
        os.path.join(FILES_DIR, 'recursive_yaml1.yaml'),
        os.path.join(FILES_DIR, 'recursive_yaml2.yaml'),
        formatter='stylish',
    )
    expected = open_file(os.path.join(EXPECTED_DIR, 'recursive_stylist.txt'))

    assert actual == expected


def test_plain_json():
    actual = generate_diff(
        os.path.join(FILES_DIR, 'recursive_json1.json'),
        os.path.join(FILES_DIR, 'recursive_json2.json'),
        formatter='plain',
    )
    expected = open_file(os.path.join(EXPECTED_DIR, 'plain.txt'))

    assert actual == expected


def test_plain_yaml():
    actual = generate_diff(
        os.path.join(FILES_DIR, 'recursive_yaml1.yaml'),
        os.path.join(FILES_DIR, 'recursive_yaml2.yaml'),
        formatter='plain',
    )
    expected = open_file("../tests/test_data/expected_result/plain.txt")

    assert actual == expected


if __name__ == '__main__':
    from pytest import main
    main()
