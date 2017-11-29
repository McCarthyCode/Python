string = " x"
for i in range(1,13):
    string += '{}'.format(str(i)).rjust(4)
print string
for i in range(1,13):
    string = '{}'.format(str(i)).rjust(2)
    for j in range(1,13):
        string += '{}'.format(str(i * j)).rjust(4)
    print string