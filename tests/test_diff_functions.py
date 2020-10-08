import pytest
from tests.utils import (read_diff_output, read_diff_structure,
                         get_config_file_path)
from gendiff.diff_functions import generate_diff, generate_diff_structure
from gendiff.file_loader import load_config_file


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_plain_files(file_ext):
    file1_path = get_config_file_path(f'plain_file1{file_ext}')
    file2_path = get_config_file_path(f'plain_file2{file_ext}')

    diff_output = read_diff_output('plain_file1_diff_plain_file2')
    assert generate_diff(file1_path, file2_path) == diff_output


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_recursive_files(file_ext):
    plain_file1_path = get_config_file_path(f'plain_file1{file_ext}')
    rec_file1_path = get_config_file_path(f'rec_file1{file_ext}')
    rec_file2_path = get_config_file_path(f'rec_file2{file_ext}')

    diff_output1 = read_diff_output('rec_file1_diff_rec_file2')
    assert generate_diff(rec_file1_path, rec_file2_path) == diff_output1

    diff_output2 = read_diff_output('plain_file1_diff_rec_file1')
    assert generate_diff(plain_file1_path, rec_file1_path) == diff_output2


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_with_empty_files(file_ext):
    plain_file1_path = get_config_file_path(f'plain_file1{file_ext}')
    rec_file1_path = get_config_file_path(f'rec_file1{file_ext}')
    empty_file_path = get_config_file_path(f'empty{file_ext}')

    diff_output1 = read_diff_output('empty_diff_empty')
    assert generate_diff(empty_file_path, empty_file_path) == diff_output1

    diff_output2 = read_diff_output('empty_diff_plain_file1')
    assert generate_diff(empty_file_path, plain_file1_path) == diff_output2

    diff_output3 = read_diff_output('empty_diff_rec_file1')
    assert generate_diff(empty_file_path, rec_file1_path) == diff_output3


def test_generate_diff_with_unsopported_file_type():
    file1_path = get_config_file_path('file1.xml')
    file2_path = get_config_file_path('file2.xml')
    with pytest.raises(ValueError):
        generate_diff(file1_path, file2_path)


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_structure_with_plain_files(file_ext):
    config1 = load_config_file(get_config_file_path(f'plain_file1{file_ext}'))
    config2 = load_config_file(get_config_file_path(f'plain_file2{file_ext}'))
    diff_structure = read_diff_structure('plain_file1_diff_plain_file2')
    assert generate_diff_structure(config1, config2) == diff_structure


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_diff_structure_with_recursive_files(file_ext):
    config1 = load_config_file(get_config_file_path(f'rec_file1{file_ext}'))
    config2 = load_config_file(get_config_file_path(f'rec_file2{file_ext}'))
    diff_structure = read_diff_structure('rec_file1_diff_rec_file2')
    assert generate_diff_structure(config1, config2) == diff_structure