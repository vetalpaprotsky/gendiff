INDENT = 4
braket_temp = "{}{}\n"
item_key_temp = "{}{}: "


def render_diff(diff_structure, shift=0):
    result = [braket_temp.format('', '{')]
    shift += INDENT

    for key, data in diff_structure.items():
        if data['status'] == 'children_updated':
            result.append(item_key_temp.format(' ' * shift, key))
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

    result.append(braket_temp.format(' ' * (shift - INDENT), '}'))
    return ''.join(result)


def _render_item(key, value, status, shift=0):
    prepend = _get_item_prepend(status)
    result = [item_key_temp.format(' ' * (shift - len(prepend)) + prepend, key)]

    # Complex item value
    if isinstance(value, dict):
        result.append(braket_temp.format('', '{'))
        for k, v in value.items():
            result.append(_render_item(k, v, None, shift + INDENT))
        result.append(braket_temp.format(' ' * shift, '}'))
    # Plain item value
    else:
        result.append(_render_item_plain_value(value))

    return ''.join(result)


def _render_item_plain_value(value):
    if value is None:
        normalized_str = 'null'
    elif value is True:
        normalized_str = 'true'
    elif value is False:
        normalized_str = 'false'
    else:
        normalized_str = str(value)

    return normalized_str + '\n'


def _get_item_prepend(item_status):
    if item_status == 'removed':
        prepend = '- '
    elif item_status == 'added':
        prepend = '+ '
    elif item_status == 'unchanged' or item_status is None:
        prepend = '  '

    return prepend
