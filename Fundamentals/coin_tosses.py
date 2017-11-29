import random

def coin_toss():
    return True if round(random.random()) else False

def coin_tosses():
    num_heads = 0
    num_tails = 0

    for i in range(1,5001):
        string = "Attempt " + "#{}".format(str(i)).rjust(5)
        string += ": Throwing a coin... It's a "
        if coin_toss():
            string += "head"
            num_heads += 1
        else:
            string += "tail"
            num_tails += 1
        string += "! ... Got " + "{}".format(str(num_heads)).rjust(4)
        string += " head(s) so far and " + "{}".format(str(num_tails)).rjust(4)
        string += " tail(s) so far"

        print string

print "Starting the program..."
coin_tosses()
print "Ending the program, thank you!"