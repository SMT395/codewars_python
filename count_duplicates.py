def duplicate_count(text):
    text=text.lower()
    elements = {}
    for char in text:
        if elements.get(char,None) != None:
            elements[char]+=1
        else:
            elements[char] = 1
    count = 0
    for char, iter in elements.items():
        if iter>1:
            count+=1
        else:
            pass
    return count