def array_diff(a, b):
    
    substraction = []
    
    for number in a:
        if number not in b:
            substraction.append(number)
        else:
            continue
            
    return substraction
