# This def basically does the same thing as the def later in the script.(See line 21)
def clear():
    print """
    Welcome to ...

    GUESS THE NUMBER!!!!!!!

    The number is somewhere between 1 and 100.

    You may end the program by entering CTRL + C or COMMAND + C.

    Good Luck! :)
    """
    # That was my exciting intro senctence and some information about how to choose the number.
    import time, random, os
    # I imported the functions time so I can delay things, random so I can choose a random string or number, and os which allows me to run commands at assigned times in the script.
    number = random.randint(1,100)
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
            # The time.sleep(5) will  the loop = 0 for 5 seconds
            os.system('cls')
            # The "os.system('cls') stand for the terminal command "clear" that clears the screen.
            clear()
            # Once again, clear will bring me back to the former "def clear()" at the beginning..
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
clear()
