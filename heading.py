def left_heading(heading):

    if heading.lower() == 'n':
        new_heading = 'w'

    elif heading.lower() == 'w':
        new_heading = 's'

    elif heading.lower() == 's':
        new_heading = 'e'

    else:
        new_heading = 'n'

    return new_heading

def right_heading(heading):
    if heading.lower() == 'n':
        new_heading = 'e'

    elif heading.lower() == 'e':
        new_heading = 's'

    elif heading.lower() == 's':
        new_heading = 'w'

    else:
        new_heading = 'n'

    return new_heading