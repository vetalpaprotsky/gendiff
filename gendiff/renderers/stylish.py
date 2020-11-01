INDENT = 4
ADDED_PREPEND = '+ '
REMOVED_PREPEND = '- '


def render(diff):
    return _render(diff, 0).rstrip('\n')


def _render(diff, shift):
    result = ['{\n']
    shift += INDENT

    for key, data in diff.items():
        if data['status'] == 'children_updated':
            result.append(' ' * shift + key + ': ')
            result.append(_render(data['children'], shift))
        elif data['status'] == 'updated':
            result.extend([
                _render_item(key, data['old_value'], shift, REMOVED_PREPEND),
                _render_item(key, data['new_value'], shift, ADDED_PREPEND),
            ])
        elif data['status'] == 'added':
            result.append(
                _render_item(key, data['value'], shift, ADDED_PREPEND)
            )
        elif data['status'] == 'removed':
            result.append(
                _render_item(key, data['value'], shift, REMOVED_PREPEND)
            )
        elif data['status'] == 'unchanged':
            result.append(_render_item(key, data['value'], shift))

    result.append(' ' * (shift - INDENT) + '}\n')
    return ''.join(result)


def _render_item(key, value, shift, prepend=''):
    result = [' ' * (shift - len(prepend)) + prepend + key + ': ']

    # Complex item value
    if isinstance(value, dict):
        result.append('{\n')
        for k, v in value.items():
            result.append(_render_item(k, v, shift + INDENT))
        result.append(' ' * shift + '}\n')
    # Plain item value
    else:
        result.append(_to_str(value) + '\n')

    return ''.join(result)


def _to_str(value):
    if value is None:
        result = 'null'
    elif value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    else:
        result = str(value)

    return result
