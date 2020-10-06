import os


def read_diff_output(file_name):
    dir_path = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'diff_outputs'
    )
    file_path = os.path.join(dir_path, file_name + '.txt')
    with open(file_path) as file:
        return file.read()


def get_file_path(file_name):
    _, file_ext = os.path.splitext(file_name)
    if file_ext == '.json':
        files_dir = 'json_files'
    elif file_ext == '.yml':
        files_dir = 'yaml_files'
    elif file_ext == '.xml':
        files_dir = 'xml_files'

    dir_path = os.path.join(os.path.dirname(__file__), 'fixtures', files_dir)
    return os.path.join(dir_path, file_name)
