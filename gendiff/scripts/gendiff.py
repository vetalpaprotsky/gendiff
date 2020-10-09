import argparse
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output',
        default='stylish',
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
