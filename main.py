# https://www.programiz.com/python-programming/online-compiler/

print("Roll it 13")


# loop for testing purposes

while True:
    want_instructions = inupt("Do you want to read the instructions? ").lower()

    if want_instructions == "yes":
        print("you chose yes")
    elif want_instructions == "no":
        print("you chose no")
    else:
        print("You did not choose a valid response")


# Main routine
want_instructions