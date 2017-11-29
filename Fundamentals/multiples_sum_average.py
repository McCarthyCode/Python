# Multiples
for i in range(1, 1001):
    print i
for i in range(5, 1000001, 5):
    print i

# Sum
def sum(x):
    sum = 0
    for i in x:
        sum += i
    return sum

a = [1, 2, 5, 10, 255, 3]
print sum(a)

# Average
def avg(x):
    return sum(x)/len(x)

print avg(a)