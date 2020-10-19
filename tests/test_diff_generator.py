import pytest
from tests.utils import read_diff_output, get_file_path
from gendiff.diff_generator import generate_diff


@pytest.mark.parametrize(
    'file1_name,file2_name,output_file_name,output_format',
    [
        ('file1.json', 'file2.json', 'file1_diff_file2.txt', 'stylish'),
        ('file1.yml', 'empty.json', 'file1_diff_empty.txt', 'stylish'),
        ('empty.yml', 'empty.yml', 'empty_diff_empty.txt', 'stylish'),

        ('file1.json', 'file2.json', 'file1_diff_file2.txt', 'plain'),
        ('file1.yml', 'empty.json', 'file1_diff_empty.txt', 'plain'),
        ('empty.yml', 'empty.yml', 'empty_diff_empty.txt', 'plain'),

        ('file1.json', 'file2.json', 'file1_diff_file2.txt', 'json'),
        ('file1.yml', 'empty.json', 'file1_diff_empty.txt', 'json'),
        ('empty.yml', 'empty.yml', 'empty_diff_empty.txt', 'json'),
    ]
)
def test_generate_diff_with_different_file_formats_and_output_formats(
    file1_name, file2_name, output_file_name, output_format
):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)

    diff_output = read_diff_output(output_file_name, output_format)
    assert generate_diff(file1_path, file2_path, output_format) == diff_output


def test_generate_diff_with_unsupported_file_format():
    file1_path = get_file_path('file1.xml')
    file2_path = get_file_path('file2.xml')

    with pytest.raises(ValueError):
        generate_diff(file1_path, file2_path, 'plain')


def test_generate_diff_with_unsupported_output_format():
    file1_path = get_file_path('file1.json')
    file2_path = get_file_path('file2.json')

    with pytest.raises(ValueError):
        generate_diff(file1_path, file2_path, 'unexisting')
