def longest_consec(strarr, k):
    
    longest_string = ''
    
    for i in range(len(strarr) + 1 - k):
        
        concatenation = ''
        for j in range(k):
            concatenation += strarr[i + j]
            
        if len(concatenation) > len(longest_string):
            longest_string = concatenation
        else:
            continue
    
    return longest_string