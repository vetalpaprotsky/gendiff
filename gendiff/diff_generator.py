from gendiff.file_loader import load_file
from gendiff.renderer import get_renderer
from gendiff.diff_tree import generate_diff_tree


def generate_diff(file1_path, file2_path, output_format):
    old_dict = load_file(file1_path)
    new_dict = load_file(file2_path)
    diff_tree = generate_diff_tree(old_dict, new_dict)
    renderer = get_renderer(output_format)
    return renderer.render(diff_tree)
