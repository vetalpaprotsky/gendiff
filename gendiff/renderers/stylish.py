INDENT = 4
NO_PREPEND = '  '
ADDED_PREPEND = '+ '
REMOVED_PREPEND = '- '


def render_diff(diff_structure, shift=0):
    result = ['{\n']
    shift += INDENT

    for key, data in diff_structure.items():
        if data['status'] == 'children_updated':
            result.append(' ' * shift + key + ': ')
            result.append(render_diff(data['children'], shift))
        elif data['status'] == 'updated':
            result.extend([
                _render_item(key, data['old_value'], REMOVED_PREPEND, shift),
                _render_item(key, data['new_value'], ADDED_PREPEND, shift),
            ])
        else:
            result.append(_render_item(
                key, data['value'], _get_item_prepend(data['status']), shift
            ))

    result.append(' ' * (shift - INDENT) + '}\n')
    return ''.join(result)


def _render_item(key, value, prepend, shift=0):
    result = [' ' * (shift - len(prepend)) + prepend + key + ': ']

    # Complex item value
    if isinstance(value, dict):
        result.append('{\n')
        for k, v in value.items():
            result.append(_render_item(k, v, NO_PREPEND, shift + INDENT))
        result.append(' ' * shift + '}\n')
    # Plain item value
    else:
        result.append(_to_normalized_str(value) + '\n')

    return ''.join(result)


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


def _get_item_prepend(item_status):
    if item_status == 'removed':
        prepend = REMOVED_PREPEND
    elif item_status == 'added':
        prepend = ADDED_PREPEND
    elif item_status == 'unchanged':
        prepend = NO_PREPEND

    return prepend
