def search_element_with(number,list):
    for word in list:
        if str(number) in word:
            return word
        else:
            continue
    return ''

def order(sentence):
    
    word_list = sentence.split(" ")
    ordered_words = []
    
    for index in range(len(word_list)):
        ordered_words.append(search_element_with(index + 1, word_list))
        
    return " ".join(ordered_words)
