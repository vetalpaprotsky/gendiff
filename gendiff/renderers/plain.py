def render_diff(diff_structure, parent_keys=None):
    result = []
    if parent_keys is None:
        parent_keys = []

    for key, data in diff_structure.items():
        key_with_parents = parent_keys + [key]
        if data['status'] == 'children_updated':
            result.append(render_diff(data['children'], key_with_parents))
        else:
            result.append(_render_item(key_with_parents, data))

    return ''.join(result)


def _render_item(key_with_parents, data):
    key_path = '.'.join(key_with_parents)

    if data['status'] == 'added':
        value = _to_normalized_str(data['value'])
        item_info = f'Propery {key_path} was added with value: {value}\n'
    elif data['status'] == 'updated':
        old = _to_normalized_str(data['old_value'])
        new = _to_normalized_str(data['new_value'])
        item_info = f'Propery {key_path} was updated. From {old} to {new}\n'
    elif data['status'] == 'removed':
        item_info = f'Propery {key_path} was removed\n'
    else:
        item_info = ''

    return item_info


def _to_normalized_str(value):
    if isinstance(value, dict):
        result = '[complex value]'
    elif isinstance(value, str):
        result = f"'{value}'"
    elif value is None:
        result = 'null'
    elif value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    else:
        result = str(value)

    return result
