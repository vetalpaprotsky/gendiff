import pytest
from tests.utils import read_diff_output, get_file_path
from gendiff.diff_functions import generate_diff


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_full_files(file_ext):
    file1_path = get_file_path(f'file1{file_ext}')
    file2_path = get_file_path(f'file2{file_ext}')

    diff_output1 = read_diff_output('file1_diff_file2')
    assert generate_diff(file1_path, file2_path) == diff_output1

    diff_output2 = read_diff_output('file2_diff_file1')
    assert generate_diff(file2_path, file1_path) == diff_output2


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_empty_files(file_ext):
    file1_path = get_file_path(f'file1{file_ext}')
    empty_file_path = get_file_path(f'empty{file_ext}')

    diff_output1 = read_diff_output('empty_diff_file1')
    assert generate_diff(empty_file_path, file1_path) == diff_output1

    diff_output2 = read_diff_output('file1_diff_empty')
    assert generate_diff(file1_path, empty_file_path) == diff_output2

    diff_output3 = read_diff_output('empty_diff_empty')
    assert generate_diff(empty_file_path, empty_file_path) == diff_output3


def test_generate_diff_with_unsopported_file_type():
    file1_path = get_file_path('file1.xml')
    file2_path = get_file_path('file2.xml')
    with pytest.raises(ValueError):
        generate_diff(file1_path, file2_path)
