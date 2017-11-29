def dict_to_tuples(values):
    ret = []
    for key in values:
        ret.append((key, values[key]))
    return ret

my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

print my_dict
print dict_to_tuples(my_dict)
