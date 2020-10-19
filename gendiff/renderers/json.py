import json


def render_diff(diff_structure):
    return json.dumps(diff_structure, indent=4) + '\n'
