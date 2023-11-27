import string

def alphabet_position(text):
    
    alphabet = string.ascii_lowercase
    
    text_lowercase = text.lower()
    
    text_in_numbers = ''
    
    for character in text_lowercase:
        
        if character in alphabet:
            text_in_numbers += str(alphabet.index(character)+1)+" "
        
            
    return text_in_numbers[:-1]