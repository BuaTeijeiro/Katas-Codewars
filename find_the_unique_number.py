def find_uniq(arr):
    first_number = arr[0]
    if arr.count(first_number) > 1:
        i = 0
        number = arr[i]
        while number == first_number:
            i += 1
            number = arr[i]
        return number
        
    else:
        return first_number

    return 