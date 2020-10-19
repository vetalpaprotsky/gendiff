INDENT = 4


def render_diff(diff_structure, shift=0):
    result = [_render_open_braket()]
    shift += INDENT

    for key, data in diff_structure.items():
        if data['status'] == 'children_updated':
            result.append(_render_item_key(key, shift))
            result.append(render_diff(data['children'], shift))
        elif data['status'] == 'updated':
            result.extend([
                _render_item(key, data['old_value'], 'removed', shift),
                _render_item(key, data['new_value'], 'added', shift),
            ])
        else:
            result.append(
                _render_item(key, data['value'], data['status'], shift),
            )

    result.append(_render_closed_braket(shift - INDENT))
    return ''.join(result)


def _render_item(key, value, status, shift=0):
    prepend = _get_item_prepend(status)
    result = [_render_item_key(key, shift - len(prepend), prepend)]

    # Complex item value
    if isinstance(value, dict):
        result.append(_render_open_braket())
        for k, v in value.items():
            result.append(_render_item(k, v, None, shift + INDENT))
        result.append(_render_closed_braket(shift))
    # Plain item value
    else:
        result.append(_render_item_plain_value(value))

    return ''.join(result)


def _render_open_braket(shift=0):
    return ' ' * shift + '{\n'


def _render_closed_braket(shift=0):
    return ' ' * shift + '}\n'


def _render_item_key(key, shift=0, prepend=''):
    return ' ' * shift + prepend + key + ': '


def _render_item_plain_value(value):
    return _to_normalized_str(value) + '\n'


def _get_item_prepend(item_status):
    if item_status == 'removed':
        prepend = '- '
    elif item_status == 'added':
        prepend = '+ '
    elif item_status == 'unchanged' or item_status is None:
        prepend = '  '

    return prepend


def _to_normalized_str(value):
    if value is None:
        result = 'null'
    elif value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    else:
        result = str(value)

    return result
