#!/usr/bin/env python3
import argparse
from gendiff.gendiff_main import open_file


def main():
    parser = argparse.ArgumentParser()
    # Positional Arguments
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    # Optional Arguments
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    result = '\n'.join(open_file(args.first_file, args.second_file))
    print(result)
    return result


if __name__ == '__main__':
    main()

