def getbase(expr):
    base = expr.split("^")[0]
    return base [1:-1]

def getexponent(expr):
    exponent = expr.split("^")[1]
    return int(exponent)

def getletter(base):
    for character in base:
        if character.isalpha():
            return character

def getnumbers(base):
    letter = getletter(base)
    coeficient, number = base.split(letter)
    if coeficient == '':
        coeficient = '1'
    elif coeficient == '-':
        coeficient = '-1'
    return coeficient, number

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

def combinatory(i, total):
    return factorial(total)/(factorial(i)*factorial(total-i))

def expand(expr):
    base = getbase(expr)
    exponent = getexponent(expr)
    if exponent == 0:
        return "1"
    elif exponent == 1:
        return base
    else:
        letter = getletter(base)
        coeficient, number = getnumbers(base)
        expansion = ''
        for i in range(exponent + 1):
            n = exponent - i
            new_coeficient = int(int(coeficient) ** (n) * int(number) ** i * combinatory(i, exponent))
            if n == 0:
                new_letter = ''
            elif n == 1:
                new_letter = letter
            elif n > 1:
                new_letter = letter + '^' + str(n)
            if i != 0 and new_coeficient > 0:
                expansion += '+'
            
            if new_coeficient == 1 and n != 0:
                new_coeficient = ''
            elif new_coeficient == -1 and n != 0:
                new_coeficient == '-'
            new_coeficient = str(new_coeficient)
            expansion += new_coeficient + new_letter
            
        return expansion