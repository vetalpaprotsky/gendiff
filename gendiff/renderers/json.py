import json


def render_diff(internal_structure):
    return json.dumps(internal_structure, indent=4) + '\n'
