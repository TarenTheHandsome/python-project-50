from gendiff.gendiff_main import generate_diff


def test_smoke_json():
    generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_json-1.json',
                  '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat-json-2.json')


def test_smoke_yaml():
    generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_yaml1.yaml',
                  '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_yaml2.yaml')


def test_flat_json_content_added():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_json-1.json',
                            '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat-json-2.json')
    expected = \
    [
        '- follow: False',
        '  host: hexlet.io',
        '- proxy: 123.234.53.22',
        '- timeout: 50',
        '+ timeout: 20',
        '+ verbose: True',
    ]
    assert actual == expected


def test_flat_yaml_content_added():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_json-1.json',
                  '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat-json-2.json')
    expected = \
    [
        '- follow: False',
        '  host: hexlet.io',
        '- proxy: 123.234.53.22',
        '- timeout: 50',
        '+ timeout: 20',
        '+ verbose: True',
    ]
    assert actual == expected


def test_flat_json_removing():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_json-1.json',
                  '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/empty_json.json')
    expected = \
    [
        '- follow: False',
        '- host: hexlet.io',
        '- proxy: 123.234.53.22',
        '- timeout: 50',
    ]
    assert actual == expected


def test_flat_yaml_removing():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_yaml1.yaml',
                  '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/empty_yaml.yaml')
    expected = \
    [
        '- follow: False',
        '- host: hexlet.io',
        '- proxy: 123.234.53.22',
        '- timeout: 50',
    ]
    assert actual == expected


def test_flat_json_reverse_files():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat-json-2.json',
                           '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_json-1.json')

    expected = \
    [
        '+ follow: False',
        '  host: hexlet.io',
        '+ proxy: 123.234.53.22',
        '- timeout: 20',
        '+ timeout: 50',
        '- verbose: True',
    ]
    assert actual == expected


def test_flat_yaml_reverse_files():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_yaml2.yaml',
                           '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_yaml1.yaml')

    expected = \
    [
        '+ follow: False',
        '  host: hexlet.io',
        '+ proxy: 123.234.53.22',
        '- timeout: 20',
        '+ timeout: 50',
        '- verbose: True',
    ]
    assert actual == expected


def test_flat_json_add():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/empty_json.json',
                           '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_json-1.json')
    expected = \
    [
        '+ follow: False',
        '+ host: hexlet.io',
        '+ proxy: 123.234.53.22',
        '+ timeout: 50',
    ]
    assert actual == expected


def test_flat_yaml_add():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/empty_yaml.yaml',
                           '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_yaml1.yaml')
    expected = \
    [
        '+ follow: False',
        '+ host: hexlet.io',
        '+ proxy: 123.234.53.22',
        '+ timeout: 50',
    ]
    assert actual == expected


def test_flat_json_content_added():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat_json-1.json',
                            '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/flat-json-2.json')
    expected = \
    [
        '- follow: False',
        '  host: hexlet.io',
        '- proxy: 123.234.53.22',
        '- timeout: 50',
        '+ timeout: 20',
        '+ verbose: True',
    ]
    assert actual == expected


if __name__ == '__main__':
    from pytest import main
    main()
