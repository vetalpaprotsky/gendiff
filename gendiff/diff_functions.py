from gendiff.file_loader import load_file
from collections import OrderedDict


def generate_diff(file1_path, file2_path):
    config1 = load_file(file1_path)
    config2 = load_file(file2_path)
    # Remove duplicate keys while preserving the order.
    unique_keys = list(
        OrderedDict.fromkeys(list(config1.keys()) + list(config2.keys()))
    )

    result = ['{']
    for key in unique_keys:
        if key in config1:
            if key in config2:
                if config1[key] == config2[key]:
                    # Value is unchanged in config2
                    result.append(__get_item_diff_str(key, config1[key]))
                else:
                    # Value is changed in config2
                    result.append(__get_item_diff_str(key, config1[key], '-'))
                    result.append(__get_item_diff_str(key, config2[key], '+'))
            else:
                # Value is removed from config2
                result.append(__get_item_diff_str(key, config1[key], '-'))
        else:
            # Value is added to config2
            result.append(__get_item_diff_str(key, config2[key], '+'))

    result.append('}')
    return "\n".join(result)


def __get_item_diff_str(key, value, prepend=' '):
    if value is None:
        value = 'null'
    elif value is True:
        value = 'true'
    elif value is False:
        value = 'false'

    return f"  {prepend} {key}: {value}"
