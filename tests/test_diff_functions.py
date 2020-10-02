import os
from gendiff.diff_functions import generate_diff


def read_json_diff_output(filename):
    dir_path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'json_diff_outputs'
    )
    file_path = os.path.join(dir_path, filename + '.txt')
    with open(file_path) as file:
        content = file.read()
        # Remove trailing whitespaces.
        return content.rstrip()


def get_json_file_path(filename):
    dir_path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'json_files'
    )
    return os.path.join(dir_path, filename + '.json')


def test_generate_diff_with_full_files():
    file1_path = get_json_file_path('file1')
    file2_path = get_json_file_path('file2')

    diff_output1 = read_json_diff_output('file1_diff_file2')
    assert generate_diff(file1_path, file2_path) == diff_output1

    diff_output2 = read_json_diff_output('file2_diff_file1')
    assert generate_diff(file2_path, file1_path) == diff_output2


def test_generate_diff_with_empty_files():
    file1_path = get_json_file_path('file1')
    empty_file_path = get_json_file_path('empty')

    diff_output1 = read_json_diff_output('empty_diff_file1')
    assert generate_diff(empty_file_path, file1_path) == diff_output1

    diff_output2 = read_json_diff_output('file1_diff_empty')
    assert generate_diff(file1_path, empty_file_path) == diff_output2

    diff_output3 = read_json_diff_output('empty_diff_empty')
    assert generate_diff(empty_file_path, empty_file_path) == diff_output3
