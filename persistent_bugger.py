def persistence(n):
    number = n
    string_number = str(number)
    digits = len(string_number)
    
    persistence = 0
    while digits > 1:
        persistence += 1
        number = 1
        for character in string_number:
            number = number * int(character)
        string_number = str(number)
        digits = len(string_number)
    
    return persistence
