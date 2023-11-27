def encoder(data):
    coded = {'': 0}
    encoded_word = ''
    new_word = ''
    index = 0
    for character in data:
        new_word += character
        if new_word in coded:
            continue
        else:
            encoded_word += str(coded[new_word[:-1]]) + new_word[-1]
            index += 1
            coded[new_word] = index
            new_word = ''
    if new_word:
        encoded_word += str(coded[new_word])
    return encoded_word


def decoder(data):
    print(data)
    coded = {0: ''}
    decoded_word = ''
    index = 1
    key = ''
    for character in data:
        if character.isdigit():
            key += character
        elif character.isalpha():
            decoded_word += coded[int(key)] + character
            coded[index] = coded[int(key)] + character
            index += 1
            key = ''
    if key:
        decoded_word += coded[int(key)]
    return decoded_word