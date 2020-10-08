from gendiff.config_file_loader import load_config_file
from gendiff.renderers import json, plain
from gendiff.internal_structure_generator import generate_internal_structure


def generate_diff(file1_path, file2_path, output_format):
    config1 = load_config_file(file1_path)
    config2 = load_config_file(file2_path)

    # TODO: There should be one more format.
    if output_format == 'json':
        renderer = json
    elif output_format == 'plain':
        renderer = plain
    else:
        raise ValueError('Invalid output format')

    structure = generate_internal_structure(config1, config2)
    return renderer.render_diff(structure)
