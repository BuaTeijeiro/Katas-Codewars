import string
def get_score(word):
    
    alphabet = string.ascii_lowercase
    points = 0
    
    for letter in word:
        points += alphabet.index(letter) + 1
        
    return points

def high(x):
    words = x.split(' ')
    
    winner_word = ''
    winner_score = 0
    for word in words:
        points = get_score(word)
        
        if points <= winner_score:
            continue
        else:
            winner_word = word
            winner_score = points
            
    return winner_word