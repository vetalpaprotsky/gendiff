import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.parse_args()


if __name__ == '__main__':
    main()
