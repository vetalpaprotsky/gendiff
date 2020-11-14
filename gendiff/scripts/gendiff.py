from gendiff.args_parser import get_parser
from gendiff.diff_generator import generate_diff


def main():
    parser = get_parser()
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
