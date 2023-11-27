def first_n_smallest(array, n):
    array_sorted = sorted(array)[:n]
    numbers_smallest = []
    index = 0
    while array_sorted:
        number = array[index]
        if number in array_sorted:
            numbers_smallest.append(number)
            array_sorted.remove(number)
        index += 1
            
    return numbers_smallest