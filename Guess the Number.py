print """
Welcome to ...

GUESS THE NUMBER!!!!!!!

The number is somewhere between 1 and 100.

Good Luck! :)
"""
# That was my exciting intro senctence and some information about how to choose the number.
import time, random
# I imported the functions time so I can delay things and random so I can choose a random string or number.
number = random.randint(0,100)
    # random.randint chooses a random number which I have set to choose a number between 1 and 100.
rightnum = round (number, 0)
    # I round it so the decimal is not long. I have it so you must put and integer and add .0 for it to work.
    # The def will make so that whenever I put guess_again it will loop it back to here.
def guess_again():
    # The number will be inputed by the user
    user = float(raw_input("Choose a number "))
    if user ==  rightnum:
        print "Congratulations you have selected the correct number!"
        # This will come up if you guess the random number correctly.
        time.sleep(5)
        # The time.sleep(5) will delay the loop = 0 for 5 seconds
        loop = 0
        # loop = 0 ends the file
    elif user < rightnum:
        print "That number you have selected is too low try again"
        # This is the message that will display if your number the user inputted is to less than 38.
        guess_again()
        # This will send you back to the line under def guess_again so you can choose a new number.
    elif user > rightnum:
        print "The number you have selected is too high try again"
        # This is the message that will display if your chosen number is higher than 38.
        # Once again, this will send you back to the line under def guess_again choose a new number.
        guess_again()
    else:
        # This is what would happen if you wrote something that isn't a number.
        "That is not a number please try again."
        guess_again
# The guess_again will return me to the line under def guess_again.s

guess_again()
