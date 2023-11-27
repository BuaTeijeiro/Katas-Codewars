def is_palindrome(number):
    if str(number)[::-1] == str (number):
        return True
    else:
        return False
    
def is_rounded(number):
    l = len(str(number))
    if number % 10 ** (l-1) == 0:
        return True
    else:
        return False

incremental_numbers = '1234567890'
decrimental_numbers = '9876543210'
    
    
def is_monotone(number):
    if str(number) in incremental_numbers or str(number) in decrimental_numbers:
        return True
    else:
        return False


def is_number_awesome(number, awesome_phrases):
    if number < 100:
        return False
    elif number in awesome_phrases:
        return True
    elif is_palindrome(number):
        return True
    elif is_rounded(number):
        return True
    elif is_monotone(number):
        return True
    else:
        return False

def is_interesting(number, awesome_phrases):
    print(number)
    if is_number_awesome(number, awesome_phrases):
        return 2
    elif is_number_awesome(number + 1, awesome_phrases) or is_number_awesome(number + 2, awesome_phrases):
        return 1
    else:
        return 0