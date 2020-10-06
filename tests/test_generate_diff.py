import pytest
from tests.utils import read_diff_output, get_file_path
from gendiff.diff_functions import generate_diff


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_plain_files(file_ext):
    file1_path = get_file_path(f'plain_file1{file_ext}')
    file2_path = get_file_path(f'plain_file2{file_ext}')

    diff_output1 = read_diff_output('plain_file1_diff_plain_file2')
    assert generate_diff(file1_path, file2_path) == diff_output1

    diff_output2 = read_diff_output('plain_file2_diff_plain_file1')
    assert generate_diff(file2_path, file1_path) == diff_output2


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_recurse_files(file_ext):
    plain_file1_path = get_file_path(f'plain_file1{file_ext}')
    recurse_file1_path = get_file_path(f'recurse_file1{file_ext}')
    recurse_file2_path = get_file_path(f'recurse_file2{file_ext}')

    diff_output1 = read_diff_output('recurse_file1_diff_recurse_file2')
    assert generate_diff(recurse_file1_path, recurse_file2_path) == diff_output1

    diff_output2 = read_diff_output('recurse_file2_diff_recurse_file1')
    assert generate_diff(recurse_file2_path, recurse_file1_path) == diff_output2

    diff_output3 = read_diff_output('plain_file1_diff_recurse_file1')
    assert generate_diff(plain_file1_path, recurse_file1_path) == diff_output3


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_empty_files(file_ext):
    plain_file1_path = get_file_path(f'plain_file1{file_ext}')
    recurse_file1_path = get_file_path(f'recurse_file1{file_ext}')
    empty_file_path = get_file_path(f'empty{file_ext}')

    diff_output1 = read_diff_output('empty_diff_plain_file1')
    assert generate_diff(empty_file_path, plain_file1_path) == diff_output1

    diff_output2 = read_diff_output('plain_file1_diff_empty')
    assert generate_diff(plain_file1_path, empty_file_path) == diff_output2

    diff_output3 = read_diff_output('empty_diff_empty')
    assert generate_diff(empty_file_path, empty_file_path) == diff_output3

    diff_output4 = read_diff_output('empty_diff_recurse_file1')
    assert generate_diff(empty_file_path, recurse_file1_path) == diff_output4

    diff_output5 = read_diff_output('recurse_file1_diff_empty')
    assert generate_diff(recurse_file1_path, empty_file_path) == diff_output5


def test_generate_diff_with_unsopported_file_type():
    file1_path = get_file_path('file1.xml')
    file2_path = get_file_path('file2.xml')
    with pytest.raises(ValueError):
        generate_diff(file1_path, file2_path)
