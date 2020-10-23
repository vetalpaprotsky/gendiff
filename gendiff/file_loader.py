import os
import json
import yaml


def load_file(file_path):
    file_type = _get_file_type(file_path)
    with open(file_path) as file:
        return _parse_file(file, file_type)


def _parse_file(file, file_type):
    if file_type == 'json':
        result = json.load(file)
    elif file_type == 'yaml':
        # If the file is empty, then the return value of load
        # function is None. In that case an empty dict is assigned
        # to the result variable.
        result = yaml.load(file, Loader=yaml.Loader) or {}
    else:
        raise ValueError('Unsupported file type')
    return result


def _get_file_type(file_path):
    _, file_ext = os.path.splitext(file_path)
    if file_ext == '.json':
        return 'json'
    elif file_ext == '.yml' or file_ext == '.yaml':
        return 'yaml'
