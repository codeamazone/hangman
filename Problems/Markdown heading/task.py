def heading(input_heading, heading_level=1):
    if heading_level < 1:
        x = 1 * '#'
    elif heading_level > 6:
        x = 6 * '#'
    else:
        x = heading_level * '#'
    return f'{x} {input_heading}'
