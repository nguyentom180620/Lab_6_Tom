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


def decode(encoded_password: str) -> str:
    decoded = []
    for char in encoded_password:
        if char.isdigit():
            # Decrement the number by 3 and take modulo 10 to wrap around between 0-9
            decoded_char = str((int(char) - 3) % 10)
        else:
            decoded_char = char  # If it's not a digit, keep it unchanged
        decoded.append(decoded_char)
    return ''.join(decoded)


def main():
    run = True
    while run:
        display_menu()
        option = input("Please enter an option: ")
        if option == "1":
            orig_password = input("Please enter your password to encode: ")
            encoded_password = encode(orig_password)
            print("Your password has been encoded and stored!")
            print()
        elif option == "2":
            print(f"The encoded password is {encoded_password},"
                  f" and the original password is {decode(encoded_password)}.\n")
        else:
            run = False


if __name__ == "__main__":
    main()
