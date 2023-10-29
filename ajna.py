# Ajna Topic
def encode(password):  # Function returns encoded password
    list = []
    b = 0
    for a in password:  # For loop iterates through the each character in a password
        if int(a) == 1 or int(a) == 2 or int(a) == 3 or int(a) == 4 or int(a) == 5 or int(a) == 6 or int(a) == 7 or int(
                a) == 8 or int(a) == 9:
            list.append(str(int(a) + 3))
            b += 1  # Counter for the number of digits
        else:  # All values should be integers
            raise ValueError('Must be integers!')
    if b != 8:  # There should be exactly 8 digits in a password and otherwise the error is raised
        raise ValueError('Must be 8 digits!')
    encoded_password = ''.join(list)  # List is joined into a string
    return encoded_password  # Encoded password is returned


def decode():
    pass


if __name__ == "__main__":  # Main function

    print("Menu\n"  # Menu is printed out 
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

    menu_one = 0
    o = int(input("Please enter an option: "))  # First menu value input
    while o != 3:   # While loop controls the program depending on user's input- terminates if 3 is chosen

        if o == 1:  # Menu value one
            try:
                menu_one = 1
                password = input("Please enter your password to encode: ")  # Input of user's password
                encoded = encode(password)  # Encode function encodes the password and stores it in "encoded" variable
                print("Your password has been encoded and stored!")
            except ValueError as excpt:
                print(excpt)    # If password is invalid, exception is run
                print('Add a new password')
        elif o == 2:    # Menu value two
            if menu_one == 1:   # Menu one should be chosen before menu two
                try:
                    print(f"The encoded password is {encoded}, and the original password is {decode(encoded_pass)}.")
                except ValueError as excpt: # Exception
                    print(excpt)
                    print('Add a new password')

            else:   # If menu 2 is called before menu 1
                print("Menu one must be called before menu two.")

        elif o == 3:    # Menu option three terminates the program
            break
        else:   # If menu option doesn't exist, invalid input is printed out
            print("Invalid input.")

        print("\nMenu\n"    # Menu is printed out again
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")
        o = int(input("\nPlease enter an option: "))    # User is prompted to input the next menu value
