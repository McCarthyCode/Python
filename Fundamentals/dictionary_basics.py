def print_dict(pairs):
    for key in pairs:
        print "My " + str(key) + " is " + str(pairs[key])

x = {
    "name": "Matt",
    "age": 24,
    "country of birth": "The United States",
    "favorite language": "Python"}

print_dict(x)
