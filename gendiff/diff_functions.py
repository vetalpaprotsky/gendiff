import json


# TODO: Refactor me.
def generate_diff(filepath1, filepath2):
    config1 = json.load(open(filepath1))
    config2 = json.load(open(filepath2))
    unique_keys = set(config1.keys()).union(config2.keys())
    difference = {}

    for key in unique_keys:
        difference[key] = {}
        if key in config1:
            if key in config2:
                if config1[key] == config2[key]:
                    difference[key] = 'unchanged'
                else:
                    difference[key] = 'changed'
            else:
                difference[key] = 'removed'
        else:
            # If it's not in config1 dict, then it's definitely in config2 dict.
            difference[key] = 'added'

    result = ['{']
    for key, status in difference.items():
        if status == 'unchanged':
            result.append(f"    {key}: {__to_str_json_type(config1[key])}")
        elif status == 'changed':
            result.append(f"  - {key}: {__to_str_json_type(config1[key])}")
            result.append(f"  + {key}: {__to_str_json_type(config2[key])}")
        elif status == 'removed':
            result.append(f"  - {key}: {__to_str_json_type(config1[key])}")
        elif status == 'added':
            result.append(f"  + {key}: {__to_str_json_type(config2[key])}")
    result.append('}')

    return "\n".join(result)


def __to_str_json_type(value):
    if value is None:
        result = 'null'
    elif value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    else:
        result = str(value)

    return result
