# This code is a test of using the binary search process in a program


def hi_lo():
    low = 1
    high = 1000
    guess_count = 0

    print("Please think of a number between {0} and {1}.".format(low, high))
    input("Press enter to start: ")

    while True:
        # The below formula is used to perform a binary search
        # It will find the midpoint based off the low and high values
        # Depending on if the guess is too high or low, it will find a new \
        # mid-point next time
        # A computer can always guess any number between 1 and 1023 in 10 \
        # guesses
        guess = low + (high - low) // 2
        guess_count += 1
        if guess_count == 0:
            print("\nMy first guess will be {0}.".format(guess))
        elif guess_count == 10:
            print("\nMy final guess will be {0}.".format(guess))
        elif guess_count == 11:
            print("\nI have run out of guesses and lost the game!")
            print("Well done human, you have beaten me!")
            exit()
        else:
            print("\nMy next guess will be {0}.".format(guess))
        if guess_count == 1:
            print("I have used {0} guess so far.".format(guess_count))
        else:
            print("I have used {0} guesses so far.".format(guess_count))
        print("\nIs that correct, too high or too low?")
        print("Type: 'c' for correct, 'h' for too high and 'l' for to low.")
        guess_loop = True
        while guess_loop:
            user_input = input("Your answer: ")
            user_input.casefold()
            if user_input == 'c':
                if guess_count == 1:
                    print("\nI got the answer correct on my first guess!")
                    exit()
                elif guess_count == 10:
                    print("\nThat was lucky, I got it right on my last guess!")
                    exit()
                else:
                    print("\nI got the correct answer in {0} guesses!"
                          .format(guess_count))
                    exit()
            elif user_input == 'h':
                print("\nOkay, I will guess lower next time...")
                high = guess - 1
                guess_loop = False
            elif user_input == 'l':
                print("\nOkay, I will guess higher next time...")
                low = guess + 1
                guess_loop = False
            else:
                print("\nI am sorry, please type 'c' for correct, 'h' for too "
                      "high and 'l' for too low.")


hi_lo()
