import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    print("First file: {}".format(args.first_file))
    print("Second file: {}".format(args.second_file))


if __name__ == '__main__':
    main()
