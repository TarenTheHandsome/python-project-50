from gendiff.scripts.gendiff_main import generate_diff
from gendiff.scripts.gendiff_main import open_file


def test_smoke_json():
    generate_diff('../tests/test_data/files/empty_json.json',
                  '../tests/test_data/files/empty_json.json')


def test_smoke_yaml():
    generate_diff('../tests/test_data/files/empty_yaml.yaml',
                  '../tests/test_data/files/empty_yaml.yaml')


def test_flat_json_content_added():
    actual = generate_diff('../tests/test_data/files/flat_json1.json',
                            '../tests/test_data/files/flat_json2.json', flag='stylish')
    expected = open_file("../tests/test_data/expected_result/flat_stylish.txt")

    assert actual == expected


def test_flat_yaml_content_added():
    actual = generate_diff('../tests/test_data/files/flat_yaml1.yaml',
                           '../tests/test_data/files/flat_yaml2.yaml', flag='stylish')

    expected = open_file("../tests/test_data/expected_result/flat_stylish.txt")

    assert actual == expected


def test_nested_json():
    actual = generate_diff('../tests/test_data/files/recursive_json1.json',
                           '../tests/test_data/files/recursive_json2.json', flag='stylish')
    expected = open_file("../tests/test_data/expected_result/recursive_stylist.txt")

    assert actual == expected


def test_nested_yaml():
    actual = generate_diff('../tests/test_data/files/recursive_yaml1.yaml',
                           '../tests/test_data/files/recursive_yaml2.yaml', flag='stylish')
    expected = open_file("../tests/test_data/expected_result/recursive_stylist.txt")

    assert actual == expected


def test_plain_json():
    actual = generate_diff('../tests/test_data/files/recursive_json1.json',
                           '../tests/test_data/files/recursive_json2.json', flag='plain')
    expected = open_file("../tests/test_data/expected_result/plain.txt")

    assert actual == expected


def test_plain_yaml():
    actual = generate_diff('../tests/test_data/files/recursive_yaml1.yaml',
                           '../tests/test_data/files/recursive_yaml2.yaml', flag='plain')
    expected = open_file("../tests/test_data/expected_result/plain.txt")

    assert actual == expected


if __name__ == '__main__':
    from pytest import main
    main()
