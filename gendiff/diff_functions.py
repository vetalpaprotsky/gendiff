from gendiff.file_loader import load_config_file


def generate_diff(file1_path, file2_path):
    config1 = load_config_file(file1_path)
    config2 = load_config_file(file2_path)
    structure = generate_diff_structure(config1, config2)
    return render_diff_structure(structure)


NEW_LEVEL_SHIFT = 4


def render_diff_structure(diff_structure, shift=0):
    result = [render_open_braket()]
    shift += NEW_LEVEL_SHIFT

    for item in diff_structure:
        if item['status'] == 'children_changed':
            result.append(render_diff_item_key(item['key'], shift))
            result.append(render_diff_structure(item['children'], shift))
        else:
            result.append(render_diff_item(
                item['key'],
                item['value'],
                item['status'],
                shift,
            ))

    result.append(render_closed_braket(shift - NEW_LEVEL_SHIFT))
    return ''.join(result)


def render_diff_item(key, value, status, shift=0):
    prepend = get_diff_item_prepend(status)
    result = [render_diff_item_key(key, shift - len(prepend), prepend)]

    if isinstance(value, dict):
        result.append(render_open_braket())
        for k, v in value.items():
            result.append(render_diff_item(k, v, None, shift + NEW_LEVEL_SHIFT))
        result.append(render_closed_braket(shift))
    else:
        result.append(render_diff_item_plain_value(value))

    return ''.join(result)


def render_open_braket(shift=0):
    return ' ' * shift + '{\n'


def render_closed_braket(shift=0):
    return ' ' * shift + '}\n'


def render_diff_item_key(key, shift=0, prepend=''):
    return ' ' * shift + prepend + key + ': '


def render_diff_item_plain_value(value):
    return to_normalized_str(value) + '\n'


def get_diff_item_prepend(item_status):
    if item_status == 'removed':
        prepend = '- '
    elif item_status == 'added':
        prepend = '+ '
    elif item_status == 'unchanged' or item_status is None:
        prepend = '  '

    return prepend


def to_normalized_str(value):
    if value is None:
        result = 'null'
    elif value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    else:
        result = str(value)

    return result


def generate_diff_structure(config1, config2):
    structure = []
    config1_keys, config2_keys = set(config1), set(config2)

    # Adding removed items
    for key in sorted(config1_keys.difference(config2_keys)):
        structure.append({
            'key': key,
            'value': config1[key],
            'status': 'removed',
        })

    # Adding added items
    for key in sorted(config2_keys.difference(config1_keys)):
        structure.append({
            'key': key,
            'value': config2[key],
            'status': 'added',
        })

    for key in sorted(config1_keys.intersection(config2_keys)):
        value1, value2 = config1[key], config2[key]

        # Adding unchanged items
        if value1 == value2:
            structure.append({
                'key': key,
                'value': value1,
                'status': 'unchanged',
            })
        # Adding items with changed children
        elif isinstance(value1, dict) and isinstance(value2, dict):
            children = []
            structure.append({
                'key': key,
                'children': children,
                'status': 'children_changed',
            })
            children.extend(generate_diff_structure(value1, value2))
        # Adding changed items
        else:
            structure.append({
                'key': key,
                'value': value1,
                'status': 'removed',
            })
            structure.append({
                'key': key,
                'value': value2,
                'status': 'added',
            })

    return structure
