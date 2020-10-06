from gendiff.file_loader import load_config_file


def generate_diff(file1_path, file2_path):
    config1 = load_config_file(file1_path)
    config2 = load_config_file(file2_path)
    diff = generate_diff_structure(config1, config2)
    return ''.join(render_diff(diff))


def render_diff(diff, cur_result=None, shift=0):
    cur_result = cur_result or []
    cur_result += ['{', '\n']
    shift += 4

    for key, item in sorted(diff.items()):
        if item['status'] in {'removed', 'added', 'unchanged'}:
            render_diff_item(
                key, item['value'], item['status'], cur_result, shift
            )
        elif item['status'] == 'changed':
            render_diff_item(key, item['old'], 'removed', cur_result, shift)
            render_diff_item(key, item['new'], 'added', cur_result, shift)
        elif item['status'] == 'children_changed':
            cur_result += [' ' * shift, key, ': ']
            render_diff(item['children'], cur_result, shift)

    shift -= 4
    cur_result += [' ' * shift, '}', '\n']
    return cur_result


def render_diff_item(key, value, status, cur_result, shift=0):
    if status == 'removed':
        prepend = '- '
    elif status == 'added':
        prepend = '+ '
    elif status == 'unchanged' or status is None:
        prepend = '  '

    cur_result += [' ' * (shift - 2), prepend, key, ': ']

    if isinstance(value, dict):
        cur_result += ['{', '\n']
        for key, item in sorted(value.items()):
            render_diff_item(key, item, None, cur_result, shift + 4)
        cur_result += [' ' * shift, '}', '\n']
    else:
        cur_result += [to_diff_item_value(value), '\n']


def generate_diff_structure(config1, config2, structure=None):
    if structure is None:
        structure = {}

    config1_keys, config2_keys = set(config1), set(config2)

    # Adding removed items
    for key in config1_keys.difference(config2_keys):
        structure[key] = {'status': 'removed', 'value': config1[key]}

    # Adding added items
    for key in config2_keys.difference(config1_keys):
        structure[key] = {'status': 'added', 'value': config2[key]}

    for key in config1_keys.intersection(config2_keys):
        value1, value2 = config1[key], config2[key]

        # Adding unchanged items
        if value1 == value2:
            structure[key] = {'status': 'unchanged', 'value': value1}
        # Adding items with changed children
        elif isinstance(value1, dict) and isinstance(value2, dict):
            structure[key] = {'status': 'children_changed', 'children': {}}
            generate_diff_structure(value1, value2, structure[key]['children'])
        # Adding changed items
        else:
            structure[key] = {'status': 'changed', 'old': value1, 'new': value2}

    return structure


def to_diff_item_value(value):
    if value is None:
        result = 'null'
    elif value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    else:
        result = str(value)

    return result
