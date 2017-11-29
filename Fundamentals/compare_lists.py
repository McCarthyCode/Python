def compare(list_one, list_two):
    if len(list_one) != len(list_two):
        return False
    
    for i in range(len(list_one)):
        if list_one[i] != list_two[i]:
            return False
    
    return True

print "True" if compare([1,2,5,6,2], [1,2,5,6,2]) else "False"
print "True" if compare([1,2,5,6,5], [1,2,5,6,5,3]) else "False"
print "True" if compare([1,2,5,6,5,16], [1,2,5,6,5]) else "False"
print "True" if compare(['celery','carrots','bread','milk'], ['celery','carrots','bread','cream']) else "False"