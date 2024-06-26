# This code is for a very special psychic guessing game.
# It is guaranteed to guess any number you pick on the first try.

# Importing the sleep function from time to allow waits in the print outputs.
from time import sleep


def jespers_hi_lo() -> None:
    """
    A game that will guess your number correctly first time, guaranteed.

    Error handling for incorrect user input prompts another entry attempt.
    The code handles when a player lies abut it having guessed their number.
    """
    low = 1
    high = 1000

    print("Please think of a number between {0} and {1}.".format(low, high))
    print("I will use my amazing psychic power to guess your number!")
    print("\nPlease enter the number here so you can remember it easily.")
    while True:
        try:
            number_input = int(input("Your number: "))
            if 0 < number_input < 1001:
                break
            else:
                print("Please enter a number between {0} and {1}."
                      .format(low, high))
        except ValueError:
            print("Please enter a number between {0} and {1}."
                  .format(low, high))
    sleep(1.5)
    print("\nThank you, now let me gaze into the veil...")
    sleep(1)
    print("Consulting the mysteries of the crystal ball...")
    sleep(1)
    print("""\n                        -----------         
                    @  --    ' '  --    @     
                 @    -- '  '   '  --     @     
              @     @  --  '  '   --         @
                        ------------
                  @   --def c_ball()--    @
                      ________________""")
    sleep(3)
    print("\nIs your number {0}?".format(number_input))
    print("Enter 'y' for yes and 'n' for no.")

    while True:
        answer = input("Your answer?: ")
        answer.casefold()
        if answer == 'y':
            print("\nYes, my psychic power knows no bounds!")
            sleep(1)
            print("I win again!")
            exit()
        elif answer == 'n':
            sleep(2)
            print("\n'No'? What do you mean 'no'!?")
            print("I won't play with a cheater!")
            sleep(1)
            print("\nGoodbye!")
            exit()
        else:
            (print("I am sorry, please enter between 'y' for yes and 'n' "
                   "for no."))


jespers_hi_lo()
