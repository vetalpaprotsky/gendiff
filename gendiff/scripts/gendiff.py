from gendiff.args_parser import get_parser
from gendiff.diff_generator import generate_diff


def main():
    parser = get_parser()
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
