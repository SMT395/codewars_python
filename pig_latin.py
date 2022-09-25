def pig_it(text):
    my_list=text.split(" ")
    my_list_2=[]
    for word in my_list:
        if not word.isalpha():
            my_list_2.append(word)
        else:
            a_string=word[1:]+word[0]+"ay"
            my_list_2.append(a_string)
    res=" ".join(my_list_2)
    return res