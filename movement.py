def new_coordinates(max_x_ord, max_y_ord, current_x_ord, current_y_ord, heading):
    min_x_ord = 0
    min_y_ord = 0

    if heading.lower() == 'n':
        current_y_ord = int(current_y_ord) + 1

    elif heading.lower() == 's':
        current_y_ord = int(current_y_ord) - 1

    elif heading.lower() == 'w':
        current_x_ord = int(current_x_ord) - 1

    else:
        current_x_ord = int(current_x_ord) + 1

    if (int(current_x_ord) > int(max_x_ord)) or (int(current_x_ord) < min_x_ord) or (int(current_y_ord) > int(max_y_ord)) or (int(current_y_ord) < min_y_ord):
        print("Invalid movement input. Exceeding the plateau")
        return

    return current_x_ord, current_y_ord