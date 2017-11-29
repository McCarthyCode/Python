# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.replace("day", "month")

# Min and Max
x = [2,54,-2,7,12,98]
print "Minimum:", str(min(x))
print "Maximum:", str(max(x))

# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x)-1]

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = [x[:len(x)/2]]
x = x[len(x)/2:]
for i in x:
    y.append(i)
print y