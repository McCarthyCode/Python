def make_dict(list1, list2):
    if len(list1) < len(list2):
        temp = list1
        list1 = list2
        list2 = temp

    new_dict = {}
    for i in range(len(list2)):
        new_dict[list1[i]] = list2[i]
    for i in range(len(list2), len(list1)):
        new_dict[list1[i]] = ""

    return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

print make_dict(name, favorite_animal)
