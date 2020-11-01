import pytest
from tests.utils import load_diff_tree, get_file_path
from gendiff.diff_tree import generate_diff_tree
from gendiff.file_loader import load_file


@pytest.mark.parametrize(
    'file1_name,file2_name,diff_tree_file_name',
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
def test_generate_diff_tree_with_different_file_formats(
    file1_name, file2_name, diff_tree_file_name
):
    old_data = load_file(get_file_path(file1_name))
    new_data = load_file(get_file_path(file2_name))
    diff_tree = load_diff_tree(diff_tree_file_name)
    assert generate_diff_tree(old_data, new_data) == diff_tree
