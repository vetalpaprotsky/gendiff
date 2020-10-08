import pytest
from tests.utils import read_diff_output, get_config_file_path
from gendiff.diff_generator import generate_diff

OUTPUT_FORMAT = 'json'


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_plain_files(file_ext):
    file1_path = get_config_file_path(f'plain_file1{file_ext}')
    file2_path = get_config_file_path(f'plain_file2{file_ext}')

    diff_output = read_diff_output('plain_file1_diff_plain_file2')
    assert generate_diff(file1_path, file2_path, OUTPUT_FORMAT) == diff_output


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_recursive_files(file_ext):
    plain_file1_path = get_config_file_path(f'plain_file1{file_ext}')
    rec_file1_path = get_config_file_path(f'rec_file1{file_ext}')
    rec_file2_path = get_config_file_path(f'rec_file2{file_ext}')

    diff_output1 = read_diff_output('rec_file1_diff_rec_file2')
    assert generate_diff(
        rec_file1_path, rec_file2_path, OUTPUT_FORMAT
    ) == diff_output1

    diff_output2 = read_diff_output('plain_file1_diff_rec_file1')
    assert generate_diff(
        plain_file1_path, rec_file1_path, OUTPUT_FORMAT
    ) == diff_output2


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_empty_files(file_ext):
    plain_file1_path = get_config_file_path(f'plain_file1{file_ext}')
    rec_file1_path = get_config_file_path(f'rec_file1{file_ext}')
    empty_file_path = get_config_file_path(f'empty{file_ext}')

    diff_output1 = read_diff_output('empty_diff_empty')
    assert generate_diff(
        empty_file_path, empty_file_path, OUTPUT_FORMAT
    ) == diff_output1

    diff_output2 = read_diff_output('empty_diff_plain_file1')
    assert generate_diff(
        empty_file_path, plain_file1_path, OUTPUT_FORMAT
    ) == diff_output2

    diff_output3 = read_diff_output('empty_diff_rec_file1')
    assert generate_diff(
        empty_file_path, rec_file1_path, OUTPUT_FORMAT
    ) == diff_output3
