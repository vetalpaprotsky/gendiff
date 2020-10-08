NEW_LEVEL_SHIFT = 4


def render_diff(internal_structure, shift=0):
    result = [__render_open_braket()]
    shift += NEW_LEVEL_SHIFT

    for item in internal_structure:
        if item['status'] == 'children_changed':
            result.append(__render_item_key(item['key'], shift))
            result.append(render_diff(item['children'], shift))
        else:
            result.append(__render_item(
                item['key'],
                item['value'],
                item['status'],
                shift,
            ))

    result.append(__render_closed_braket(shift - NEW_LEVEL_SHIFT))
    return ''.join(result)


def __render_item(key, value, status, shift=0):
    prepend = __get_item_prepend(status)
    result = [__render_item_key(key, shift - len(prepend), prepend)]

    # Complex item value
    if isinstance(value, dict):
        result.append(__render_open_braket())
        for k, v in value.items():
            result.append(__render_item(k, v, None, shift + NEW_LEVEL_SHIFT))
        result.append(__render_closed_braket(shift))
    # Plain item value
    else:
        result.append(__render_item_plain_value(value))

    return ''.join(result)


def __render_open_braket(shift=0):
    return ' ' * shift + '{\n'


def __render_closed_braket(shift=0):
    return ' ' * shift + '}\n'


def __render_item_key(key, shift=0, prepend=''):
    return ' ' * shift + prepend + key + ': '


def __render_item_plain_value(value):
    return __to_normalized_str(value) + '\n'


def __get_item_prepend(item_status):
    if item_status == 'removed':
        prepend = '- '
    elif item_status == 'added':
        prepend = '+ '
    elif item_status == 'unchanged' or item_status is None:
        prepend = '  '

    return prepend


def __to_normalized_str(value):
    if value is None:
        result = 'null'
    elif value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    else:
        result = str(value)

    return result
