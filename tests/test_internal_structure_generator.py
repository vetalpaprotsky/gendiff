import pytest
from tests.utils import read_internal_structures, get_config_file_path
from gendiff.internal_structure_generator import generate_internal_structure
from gendiff.config_file_loader import load_config_file


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_internal_structure_with_plain_files(file_ext):
    config1 = load_config_file(get_config_file_path(f'plain_file1{file_ext}'))
    config2 = load_config_file(get_config_file_path(f'plain_file2{file_ext}'))
    structure = read_internal_structures('plain_file1_diff_plain_file2')
    assert generate_internal_structure(config1, config2) == structure


@pytest.mark.parametrize('file_ext', ['.json', '.yml'])
def test_generate_internal_structure_with_recursive_files(file_ext):
    config1 = load_config_file(get_config_file_path(f'rec_file1{file_ext}'))
    config2 = load_config_file(get_config_file_path(f'rec_file2{file_ext}'))
    structure = read_internal_structures('rec_file1_diff_rec_file2')
    assert generate_internal_structure(config1, config2) == structure
