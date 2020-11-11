import pytest
from tests.utils import get_fixture_file_abs_path
from gendiff.diff_generator import generate_diff


@pytest.mark.parametrize(
    'file1_path,file2_path,diff_file_path,output_format',
    [
        ('file1.json', 'file2.json', 'diff/stylish.txt', 'stylish'),
        ('file1.yml', 'file2.yml', 'diff/stylish.txt', 'stylish'),

        ('file1.json', 'file2.json', 'diff/plain.txt', 'plain'),
        ('file1.yml', 'file2.yml', 'diff/plain.txt', 'plain'),

        ('file1.json', 'file2.json', 'diff/json.txt', 'json'),
        ('file1.yml', 'file2.yml', 'diff/json.txt', 'json'),
    ]
)
def test_generate_diff(
    file1_path, file2_path, diff_file_path, output_format
):
    file1_abs_path = get_fixture_file_abs_path(file1_path)
    file2_abs_path = get_fixture_file_abs_path(file2_path)
    with open(get_fixture_file_abs_path(diff_file_path)) as file:
        diff = file.read()
    assert generate_diff(file1_abs_path, file2_abs_path, output_format) == diff
