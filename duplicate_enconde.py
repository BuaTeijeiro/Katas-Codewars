def duplicate_encode(word):
    word_caseless = word.casefold()
    new_string = ''
    for letter in word_caseless:
        if word_caseless.count(letter) == 1:
            new_string += '('
        else:
            new_string += ')'
    return new_string
