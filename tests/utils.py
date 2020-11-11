import os


def get_fixture_file_abs_path(file_name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', file_name)
