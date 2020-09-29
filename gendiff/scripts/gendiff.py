import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    print("First file: {}".format(args.first_file))
    print("Second file: {}".format(args.second_file))
    print("Format: {}".format(args.format))


if __name__ == '__main__':
    main()
