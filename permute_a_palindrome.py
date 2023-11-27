def permute_a_palindrome(input):
    
    odd_letters = ""
    letter_index = 0
    
    while len(odd_letters) < 2 and letter_index < len(input):
        
        letter = input[letter_index]
        letter_count = input.count(letter)
        letter_index += 1
                
        if letter not in odd_letters and letter_count % 2 == 1:
            
            odd_letters = odd_letters + letter
            
    return len(odd_letters) < 2