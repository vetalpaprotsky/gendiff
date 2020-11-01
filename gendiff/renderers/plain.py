def render(diff):
    return _render(diff, [])


def _render(diff, parent_keys):
    result = []

    for key, data in diff.items():
        key_with_parents = parent_keys + [key]
        key_path = '.'.join(key_with_parents)
        if data['status'] == 'children_updated':
            result.append(_render(data['children'], key_with_parents))
        elif data['status'] == 'updated':
            old = _to_str(data['old_value'])
            new = _to_str(data['new_value'])
            result.append(
                f'Propery {key_path} was updated. From {old} to {new}'
            )
        elif data['status'] == 'added':
            value = _to_str(data['value'])
            result.append(f'Propery {key_path} was added with value: {value}')
        elif data['status'] == 'removed':
            result.append(f'Propery {key_path} was removed')

    return '\n'.join(result)


def _to_str(value):
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
