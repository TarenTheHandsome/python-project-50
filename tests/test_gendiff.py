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


def test_nested_json_content():
    pass


def test_nested_yaml_content():
    pass


def test_plain_json_content():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/plain-json1.json',
                            '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/plain-json2.json', 'plain')
    expected = \
        [
            "Property 'common.follow' was added with value: false",
            "Property 'common.setting2' was removed",
            "Property 'common.setting3' was updated. From true to null",
            "Property 'common.setting4' was added with value: 'blah blah'",
            "Property 'common.setting5' was added with value: [complex value]",
            "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'",
            "Property 'common.setting6.ops' was added with value: 'vops'",
            "Property 'group1.baz' was updated. From 'bas' to 'bars'",
            "Property 'group1.nest' was updated. From [complex value] to 'str'",
            "Property 'group2' was removed",
            "Property 'group3' was added with value: [complex value]",
        ]
    assert actual == expected
    pass


def test_plain_yaml_content():
    actual = generate_diff('/Users/roman/Documents/Projects/python-project-50/tests/fixtures/plain-json1.json',
                            '/Users/roman/Documents/Projects/python-project-50/tests/fixtures/plain-json2.json', 'plain')
    expected = \
        [
            "Property 'common.follow' was added with value: false",
            "Property 'common.setting2' was removed",
            "Property 'common.setting3' was updated. From true to null",
            "Property 'common.setting4' was added with value: 'blah blah'",
            "Property 'common.setting5' was added with value: [complex value]",
            "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'",
            "Property 'common.setting6.ops' was added with value: 'vops'",
            "Property 'group1.baz' was updated. From 'bas' to 'bars'",
            "Property 'group1.nest' was updated. From [complex value] to 'str'",
            "Property 'group2' was removed",
            "Property 'group3' was added with value: [complex value]",
        ]
    assert actual == expected


if __name__ == '__main__':
    from pytest import main
    main()
