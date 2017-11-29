def type_list(l):
    hasInt    = False
    hasFloat  = False
    hasString = False

    total = 0
    string = ""

    for i in l:
        if isinstance(i, int):
            hasInt = True
            total += i
        elif isinstance(i, float):
            hasFloat = True
            total += i
        elif isinstance(i, str):
            hasString = True
            string += " " + i
        else:
            print "What kind of variable is " + str(i) + "?"

    if hasInt and not(hasFloat) and not(hasString):
        print "The list you entered is of integer type."
    elif not(hasInt) and hasFloat and not(hasString):
        print "The list you entered is of float type."
    elif not(hasInt) and not(hasFloat) and hasString:
        print "The list you entered is of string type."
    else:
        print "The list you entered is of mixed type."

    if hasString:
        print "String:" + string
    if hasInt or hasFloat:
        print "Sum:", str(total)

type_list(['magical unicorns',19,'hello',98.98,'world'])
type_list([2,3,1,7,4,12])
type_list(['magical','unicorns'])