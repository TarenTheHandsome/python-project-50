#!/usr/bin/env python3
import argparse
from gendiff.scripts.gendiff_main import generate_diff


def parser_func():
    parser = argparse.ArgumentParser()

    # Positional Arguments
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    # Optional Arguments
    parser.add_argument('-f', '--format', help='set format of output', default='stylish', type=str)
    args = parser.parse_args()
    # result = '\n'.join(generate_diff(args.first_file, args.second_file, args.format))

    return args


def main():
    args = parser_func()
    print(generate_diff(args.first_file, args.second_file, args.format))




if __name__ == '__main__':
    main()
