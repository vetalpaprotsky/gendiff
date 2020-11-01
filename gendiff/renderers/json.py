import json


def render(diff_tree):
    return json.dumps(diff_tree, indent=4)
