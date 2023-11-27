def is_valid_walk(walk):
    
    if len(walk) != 10:
        return False
    
    x_pos = 0
    y_pos = 0
    
    for direction in walk:
        if direction == 'w':
            x_pos += 1
        elif direction == 'e':
            x_pos -= 1
        elif direction == 'n':
            y_pos += 1
        else:
            y_pos -= 1
    
    if x_pos == 0 and y_pos == 0:
        return True
    else:
        return False