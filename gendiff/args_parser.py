import argparse


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output',
        default='stylish',
    )
    return parser
