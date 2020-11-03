import pytest
from tests.utils import read_diff_output, get_file_path
from gendiff.diff_generator import generate_diff


@pytest.mark.parametrize(
    'file1_name,file2_name,output_file_name,output_format',
    [
        ('file1.json', 'file2.json', 'stylish_file1_diff_file2.txt', 'stylish'),
        ('file1.yml', 'empty.json', 'stylish_file1_diff_empty.txt', 'stylish'),
        ('empty.yml', 'empty.yml', 'stylish_empty_diff_empty.txt', 'stylish'),

        ('file1.json', 'file2.json', 'plain_file1_diff_file2.txt', 'plain'),
        ('file1.yml', 'empty.json', 'plain_file1_diff_empty.txt', 'plain'),
        ('empty.yml', 'empty.yml', 'plain_empty_diff_empty.txt', 'plain'),

        ('file1.json', 'file2.json', 'json_file1_diff_file2.txt', 'json'),
        ('file1.yml', 'empty.json', 'json_file1_diff_empty.txt', 'json'),
        ('empty.yml', 'empty.yml', 'json_empty_diff_empty.txt', 'json'),
    ]
)
def test_generate_diff_with_different_file_formats_and_output_formats(
    file1_name, file2_name, output_file_name, output_format
):
    file1_path = get_file_path(file1_name)
    file2_path = get_file_path(file2_name)

    diff_output = read_diff_output(output_file_name)
    assert generate_diff(file1_path, file2_path, output_format) == diff_output


def test_generate_diff_with_unsupported_file_format():
    file_path = get_file_path('empty.xml')

    with pytest.raises(ValueError) as error:
        generate_diff(file_path, file_path, 'plain')

    assert str(error.value) == 'Unsupported file type'


def test_generate_diff_with_unsupported_output_format():
    file_path = get_file_path('empty.json')

    with pytest.raises(ValueError) as error:
        generate_diff(file_path, file_path, 'unexisting')

    assert str(error.value) == 'Invalid output format'
