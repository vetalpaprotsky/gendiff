from gendiff.renderers import stylish, plain, json


def get_renderer(output_format):
    if output_format == 'stylish':
        renderer = stylish
    elif output_format == 'plain':
        renderer = plain
    elif output_format == 'json':
        renderer = json
    else:
        raise ValueError('Invalid output format')

    return renderer
