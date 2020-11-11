def generate_diff_tree(old_dict, new_dict):
    tree = {}
    old_dict_keys, new_dict_keys = set(old_dict), set(new_dict)

    # Adding removed items
    for key in sorted(old_dict_keys.difference(new_dict_keys)):
        tree[key] = {'status': 'removed', 'value': old_dict[key]}

    # Adding added items
    for key in sorted(new_dict_keys.difference(old_dict_keys)):
        tree[key] = {'status': 'added', 'value': new_dict[key]}

    for key in sorted(old_dict_keys.intersection(new_dict_keys)):
        old_value, new_value = old_dict[key], new_dict[key]

        # Adding unchanged items
        if old_value == new_value:
            tree[key] = {'status': 'unchanged', 'value': old_value}
        # Adding items with updated children
        elif isinstance(old_value, dict) and isinstance(new_value, dict):
            tree[key] = {
                'status': 'children_updated',
                'children': generate_diff_tree(old_value, new_value),
            }
        # Adding updated items
        else:
            tree[key] = {
                'status': 'updated',
                'old_value': old_value,
                'new_value': new_value,
            }

    return tree
