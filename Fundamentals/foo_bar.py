def squares():
    ret = []
    for i in range(1, 317):
        ret.append(i*i)
    return ret

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

squares = squares()
for i in range(100, 100001):
    string = "{}".format(str(i)).rjust(6)
    string += ": FooBar" if not(isPrime(i)) and not(i in squares) else ""
    string += ": Foo" if isPrime(i) else ""
    string += ": Bar" if i in squares else ""
    print string
