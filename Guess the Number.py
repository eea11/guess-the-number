# This def basically does the same thing as the def later in the script.
# (See line 21)


def clear():
    print """
    Welcome to ...

    GUESS THE NUMBER!!!!!!!

    The number is somewhere between 1 and 100.

    Do not type any letters or the program will fail.

    You may end the program by entering CTRL + C or COMMAND + C

    If you choose to exit it will give an error but it is not a problem

    Good Luck! :)
    """
# That was my exciting intro senctence and some information about how to choose
# the number.
    import time
    import random
    import os
# I imported the functions time so I can delay things, random so I can choose a
# random string or number, and os which allows me to run commands at assigned
# times in the script.
    number = random.randint(1, 100)
# random.randint chooses a random number which I have set to choose a number
# between 1 and 100.
    rightnum = round(number, 0)
# I round it so the decimal is not long.
# The def make it that whenever I put guess_again it will loop it back here


def guess_again():
    # The number will be inputed by the user
    print "Choose a number "
    user = (input("> "))
    if user == rightnum:
        print "Congratulations you have selected the correct number!"
# This will come up if you guess the random number correctly.
        time.sleep(5)
# The time.sleep(2) will  the loop = 0 for 2 seconds
        os.system('cls')
# The "os.system('cls') stand for the command "clear" that clears the screen.
        clear()
# Once again,clear will bring me back to the "def clear()" at the beginning.

