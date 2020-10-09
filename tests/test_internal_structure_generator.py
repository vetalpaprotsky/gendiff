import pytest
from tests.utils import read_internal_structure, get_config_file_path
from gendiff.internal_structure_generator import generate_internal_structure
from gendiff.config_file_loader import load_config_file


@pytest.mark.parametrize(
    'file1_name,file2_name,internal_structure_file_name',
    [
        ('file1.json', 'file2.json', 'file1_diff_file2.json'),
        ('file1.yml', 'file2.json', 'file1_diff_file2.json'),
        ('file1.json', 'file2.yml', 'file1_diff_file2.json'),
        ('file1.yml', 'file2.yml', 'file1_diff_file2.json'),

        ('file1.yml', 'empty.json', 'file1_diff_empty.json'),
        ('file1.json', 'empty.yml', 'file1_diff_empty.json'),

        ('empty.yml', 'empty.json', 'empty_diff_empty.json'),
        ('empty.json', 'empty.yml', 'empty_diff_empty.json'),
    ]
)
def test_generate_internal_structure_with_different_file_formats(
    file1_name, file2_name, internal_structure_file_name
):
    config1 = load_config_file(get_config_file_path(file1_name))
    config2 = load_config_file(get_config_file_path(file2_name))
    structure = read_internal_structure(internal_structure_file_name)
    assert generate_internal_structure(config1, config2) == structure
