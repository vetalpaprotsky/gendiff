def render_diff(diff_structure, parent_keys=None):
    result = []
    if parent_keys is None:
        parent_keys = []

    for key, data in diff_structure.items():
        key_with_parents = parent_keys + [key]
        if data['status'] == 'children_updated':
            result.append(render_diff(data['children'], key_with_parents))
        elif data['status'] != 'unchanged':
            result.append(_render_item(key_with_parents, data))

    return ''.join(result)


def _render_item(key_with_parents, data):
    result = f"Propery {'.'.join(key_with_parents)} was {data['status']}"

    if data['status'] == 'updated':
        result += _render_updated_item_data(data)
    elif data['status'] == 'added':
        result += _render_added_item_data(data)

    return result + '\n'


def _render_added_item_data(data):
    value = _to_normalized_str(data['value'])
    return f' with value: {value}'


def _render_updated_item_data(data):
    old_value = _to_normalized_str(data['old_value'])
    new_value = _to_normalized_str(data['new_value'])
    return f'. From {old_value} to {new_value}'


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
