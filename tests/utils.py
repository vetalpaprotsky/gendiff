import os
import json


def read_diff_output(file_name, output_format):
    dir_path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'diff_outputs',
        output_format,
    )
    file_path = os.path.join(dir_path, file_name)
    with open(file_path) as file:
        return file.read()


def read_diff_structure(file_name):
    dir_path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'diff_structures'
    )
    file_path = os.path.join(dir_path, file_name)
    with open(file_path) as file:
        return json.load(file)


def get_file_path(file_name):
    _, file_ext = os.path.splitext(file_name)
    if file_ext == '.json':
        dir_name = 'json_files'
    elif file_ext == '.yml':
        dir_name = 'yaml_files'
    elif file_ext == '.xml':
        dir_name = 'xml_files'

    dir_path = os.path.join(os.path.dirname(__file__), 'fixtures', dir_name)
    return os.path.join(dir_path, file_name)
