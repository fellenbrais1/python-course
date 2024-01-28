

def password_creation():
    middle_name = ""
    favourite_pasta = ""
    number = ""
    loop_count = 0

    print("Now we are going to make you a new password")

    while loop_count == 0:
        print("Please type your middle name in all letters:")
        middle_name = str(input(">>> "))
        middle_name = middle_name.replace(" ", "")
        middle_name = middle_name.capitalize()
        print("You have typed in:", middle_name)
        if middle_name.isalpha():
            print("That middle name is acceptable")
            loop_count = 1
        else:
            print("That input is not acceptable")

    while loop_count == 1:
        print("Please type in your favourite type of pasta in all letters:")
        favourite_pasta = str(input(">>> "))
        favourite_pasta = favourite_pasta.replace(" ", "")
        favourite_pasta = favourite_pasta.casefold()
        print("You have typed in:", favourite_pasta)
        if favourite_pasta.isalpha():
            print("That answer is acceptable")
            loop_count = 2
        else:
            print("That input is not acceptable")

    while loop_count == 2:
        print("Please input a number using only digits:")
        number = str(input(">>> "))
        number = number.replace(" ", "")
        print("You have typed in:", number)
        if number.isdigit():
            print("That number is acceptable")
            loop_count = 3
        else:
            print("That input is not acceptable")

    while loop_count == 3:
        created_password = middle_name.capitalize() + favourite_pasta.casefold() + number.casefold()
        created_password = created_password.replace(" ", "")
        return created_password


password = password_creation()
password_done = False
answer = ""

while not password_done:
    password_done = False
    answer = ""
    while answer != "y" and answer != "n":
        print("Your new password is:", password)
        print("Is this password acceptable? (Y) Or would you like to try again? (N)")
        answer = str(input(">>> "))
        answer = answer.casefold()
    else:
        if answer == "y":
            password_done = True
        elif answer == "n":
            print("Let's try again shall we?")
            answer = ""
            password = password_creation()
        else:
            while answer != "y" and answer != "n":
                print("Please choose between Y and N")
                answer = str(input(">>> "))
                answer = answer.casefold()
            else:
                answer = ""
else:
    print("Well done, please use the password:", password, "in future")
    exit()