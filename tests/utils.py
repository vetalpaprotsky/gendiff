import os
import json


def read_diff_output(file_name):
    dir_path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'diff_outputs',
    )
    file_path = os.path.join(dir_path, file_name)
    with open(file_path) as file:
        return file.read()


def load_diff_tree(file_name):
    dir_path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'diff_trees'
    )
    file_path = os.path.join(dir_path, file_name)
    with open(file_path) as file:
        return json.load(file)


def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', file_name)
