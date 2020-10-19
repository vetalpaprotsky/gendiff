def generate_diff_structure(config1, config2):
    structure = {}
    config1_keys, config2_keys = set(config1), set(config2)

    # Adding removed items
    for key in sorted(config1_keys.difference(config2_keys)):
        structure[key] = {'status': 'removed', 'value': config1[key]}

    # Adding added items
    for key in sorted(config2_keys.difference(config1_keys)):
        structure[key] = {'status': 'added', 'value': config2[key]}

    for key in sorted(config1_keys.intersection(config2_keys)):
        value1, value2 = config1[key], config2[key]

        # Adding unchanged items
        if value1 == value2:
            structure[key] = {'status': 'unchanged', 'value': value1}
        # Adding items with updated children
        elif isinstance(value1, dict) and isinstance(value2, dict):
            structure[key] = {
                'status': 'children_updated',
                'children': generate_diff_structure(value1, value2),
            }
        # Adding updated items
        else:
            structure[key] = {
                'status': 'updated',
                'old_value': value1,
                'new_value': value2,
            }

    return structure
