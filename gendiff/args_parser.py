import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    default_format = 'stylish'
    parser.add_argument(
        '-f', '--format',
        type=str,
        metavar='format',
        help=f'output format (default: {default_format}, other: json, plain)',
        default=default_format,
    )
    return parser
