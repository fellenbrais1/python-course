# A function to gather user data and print out a story about them


def story_of_you(
        name='',
        age='',
        hobbies='',
):
    if name == '':
        name = input("What is your name? ".capitalize())
    else:
        pass
    if age == '':
        age = input("How old are you? ") + "-years-old."
    else:
        pass
    hobbies = list(hobbies)
    if not hobbies:
        hobbies.append(input("What is your first hobby?: "))
        hobbies.append(input("What is your second hobby?: "))
        hobbies.append(input("What is your third hobby?: "))
    else:
        pass
    print("\nYour name is ", name, ".", sep="")
    print("You are", age, ".", sep="")
    print("Your hobbies are:")
    for item in hobbies:
        print(item)
    print("This was the story of", name, ".", sep="")
    print("Goodbye!")


if __name__ == "__main__":
    story_of_you(name='', age='', hobbies='')

# Code not needed for now

# COMMENTED OUT FOR NOW
# input_hobbies = []
# input_name = input("What is your name? ".capitalize())
# input_age = input("How old are you? ") + "-years-old"
# input_hobbies.append(input("What is your first hobby? "))
# input_hobbies.append(input("What is your second hobby? "))
# input_hobbies.append(input("What is your third hobby? "))
