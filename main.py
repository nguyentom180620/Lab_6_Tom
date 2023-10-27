"""
Lab 6: Software Engineering
Authors: Tom Nguyen
Class: COP3502C
Section: 22282
Description: A simple password encoder/decoder program that is uploaded to GitHub and then worked on by a partner.
Allows practice with version control systems and developing familiarity with them.
"""


# Simple menu display function
def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


# Encoder using list and append method to return encoded password
def encode(password):
    encoded_password_list = []
    for i in password:
        if int(i) < 7:
            encoded_password_list.append(str(int(i) + 3))
        else:
            encoded_password_list.append(str(int(i) - 7))
    encoded_password = "".join(encoded_password_list)
    return encoded_password


# FIXME: Make a decoder and add it to option 2 to the main program below!
def main():
    run = True
    while run:
        display_menu()
        option = input("Please enter an option: ")
        if option == "1":
            orig_password = input("Please enter your password to encode: ")
            encoded_password = encode(orig_password)
            print("Your password has been encoded and stored!")
            print(f"Your encoded one is {encoded_password}")
            print()
        elif option == "2":
            pass
        else:
            run = False


if __name__ == "__main__":
    main()
