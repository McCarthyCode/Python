def find_characters(word_list, char):
    new_list = []
    for i in word_list:
        if i.find(char) > -1:
            new_list.append(i)
    
    return new_list

print find_characters(['hello','world','my','name','is','Anna'], 'o')