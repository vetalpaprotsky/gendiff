from gendiff.file_loader import load_file
from gendiff.renderers import stylish, plain, json
from gendiff.diff_structure_generator import generate_diff_structure


def generate_diff(file1_path, file2_path, output_format):
    old_data = load_file(file1_path)
    new_data = load_file(file2_path)

    if output_format == 'stylish':
        renderer = stylish
    elif output_format == 'plain':
        renderer = plain
    elif output_format == 'json':
        renderer = json
    else:
        raise ValueError('Invalid output format')

    structure = generate_diff_structure(old_data, new_data)
    return renderer.render_diff(structure)
