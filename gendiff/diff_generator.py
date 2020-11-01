from gendiff.file_loader import load_file
from gendiff.renderer import get_renderer
from gendiff.diff_structure_generator import generate_diff_structure


def generate_diff(file1_path, file2_path, output_format):
    old_data = load_file(file1_path)
    new_data = load_file(file2_path)
    structure = generate_diff_structure(old_data, new_data)
    renderer = get_renderer(output_format)
    return renderer.render(structure)
