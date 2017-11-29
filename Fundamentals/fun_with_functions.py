def even_odd():
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is", str(i) + ". This is an even number."
        else:
            print "Number is", str(i) + ". This is an odd number."

def multiply(l, x):
    ret = []
    for i in l:
        ret.append(i * x)
    return ret

def layered_multiples(l):
    ret = []
    for i in range(len(l)):
        ret.append([])
        for j in range(l[i]):
            ret[i].append(1)
    return ret

even_odd()
x = multiply([2,4,10,16], 5)
print x
y = layered_multiples(multiply([2,4,5], 3))
print y