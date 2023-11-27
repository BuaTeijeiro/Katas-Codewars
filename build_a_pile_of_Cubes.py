def find_nb(m):
    suma = 0
    i = 0
    while suma < m:
        i += 1
        suma += i ** 3
        
    if suma == m:
        return  i
    else:
        return -1