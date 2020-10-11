def generate_internal_structure(config1, config2):
    structure = {}
    config1_keys, config2_keys = set(config1), set(config2)

    # Adding removed items
    for key in sorted(config1_keys.difference(config2_keys)):
        structure[key] = _removed_key_data(config1[key])

    # Adding added items
    for key in sorted(config2_keys.difference(config1_keys)):
        structure[key] = _added_key_data(config2[key])

    for key in sorted(config1_keys.intersection(config2_keys)):
        value1, value2 = config1[key], config2[key]

        # Adding unchanged items
        if value1 == value2:
            structure[key] = _unchagned_key_data(value1)
        # Adding items with updated children
        elif isinstance(value1, dict) and isinstance(value2, dict):
            structure[key] = _children_updated_key_data()
            structure[key]['children'].update(
                generate_internal_structure(value1, value2)
            )
        # Adding updated items
        else:
            structure[key] = _updated_key_data(value1, value2)

    return structure


def _removed_key_data(value):
    return {'status': 'removed', 'value': value}


def _added_key_data(value):
    return {'status': 'added', 'value': value}


def _unchagned_key_data(value):
    return {'status': 'unchanged', 'value': value}


def _children_updated_key_data():
    return {'status': 'children_updated', 'children': {}}


def _updated_key_data(old_value, new_value):
    return {'status': 'updated', 'old_value': old_value, 'new_value': new_value}
