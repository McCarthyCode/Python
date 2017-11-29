import random

def score_grade(x):
    if x <= 100 and x >= 90:
        print "Score: " + "{}".format(str(x)).rjust(3) + "; Your grade is A"
    elif x <= 89 and x >= 80:
        print "Score:  " + str(x) + "; Your grade is B"
    elif x <= 79 and x >= 70:
        print "Score:  " + str(x) + "; Your grade is C"
    elif x <= 69 and x >= 60:
        print "Score:  " + str(x) + "; Your grade is D"

print "Scores and Grades"

for i in range(10):
    score_grade(random.randint(60,100))

print "End of the program. Bye!"