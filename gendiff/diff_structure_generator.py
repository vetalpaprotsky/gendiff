def generate_diff_structure(old_data, new_data):
    structure = {}
    old_data_keys, new_data_keys = set(old_data), set(new_data)

    # Adding removed items
    for key in sorted(old_data_keys.difference(new_data_keys)):
        structure[key] = {'status': 'removed', 'value': old_data[key]}

    # Adding added items
    for key in sorted(new_data_keys.difference(old_data_keys)):
        structure[key] = {'status': 'added', 'value': new_data[key]}

    for key in sorted(old_data_keys.intersection(new_data_keys)):
        old_value, new_value = old_data[key], new_data[key]

        # Adding unchanged items
        if old_value == new_value:
            structure[key] = {'status': 'unchanged', 'value': old_value}
        # Adding items with updated children
        elif isinstance(old_value, dict) and isinstance(new_value, dict):
            structure[key] = {
                'status': 'children_updated',
                'children': generate_diff_structure(old_value, new_value),
            }
        # Adding updated items
        else:
            structure[key] = {
                'status': 'updated',
                'old_value': old_value,
                'new_value': new_value,
            }

    return structure
