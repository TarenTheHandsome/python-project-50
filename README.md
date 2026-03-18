### Hexlet tests and linter status:
[![Actions Status](https://github.com/TarenTheHandsome/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/TarenTheHandsome/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=TarenTheHandsome_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=TarenTheHandsome_python-project-50)

# Difference Calculator (gendiff)
>
> - gendiff is a command-line tool for finding differences between files. This is the second project developed as part of the Hexlet course.

### Requirements:

[Python 3.13 +] - (https://www.python.org/downloads/)

[UV 0.5.11 +] - (https://astral.sh)

### Installation:

``` bash
git clone git@github.com:TarenTheHandsome/python-project-50.git 
```

``` bash
cd python-project-50 
```

``` bash
uv build
```

``` bash
uv tool install dist/*.whl 
```

### Supported File Formats:
- JSON (.json)
- YAML (.yaml, .yml)
### Usage:

1. Place the files you want to compare inside the tests/test_data directory.
2. Run the following command, replacing file1 and file2 with your actual file names:
``` bash
uv run gendiff tests/test_data/<file1> tests/test_data/<file2>
```
3. By default, the output is formatted using the stylish formatter. 
- To use a different format (json or plain), specify it with the -f flag:

### Пример вывода инструмента при использовании разных форматтеров:
- Default (stylish) formatter:
``` bash
uv run gendiff tests/test_data/<file1> tests/test_data/<file1>
```
- Using the JSON formatter:
``` bash
uv run gendiff -f stylish tests/test_data/<file1> tests/test_data/<file1>
```
- Using the Plain formatter:
``` bash
uv run gendiff -f plain tests/test_data/<file1> tests/test_data/<file1>
```

### Development and Testing:
#### Linting
Run ruff to check for linting issues:
``` bash
make lint
```
Running Tests
``` bash
make test-coverage
```
### Example

#### without a flag (json): 
[![asciicast](https://asciinema.org/a/ll6XNoiehKakff3a)](https://asciinema.org/a/ll6XNoiehKakff3a)

#### with flag plain (json): 
[![asciicast](https://asciinema.org/a/knPi7WhRG9Iqb4vP)](https://asciinema.org/a/knPi7WhRG9Iqb4vP)

#### with flag stylish (yaml): 
[![asciicast](https://asciinema.org/a/nOG77qWkHWyaZzi3)](https://asciinema.org/a/nOG77qWkHWyaZzi3)
