# Ajna Topic
def encode(password):
    list=[]
    b=0
    for a in password:
        if int(a)==1 or int(a) == 2 or int(a)==3 or int(a)== 4 or int(a)==5 or int(a)== 6 or int(a)== 7 or int(a) == 8 or int(a) == 9:
            list.append(str(int(a)+3))
            b+=1
        else:
            raise ValueError('Must be integers!')
    if b!=8:
        raise ValueError('Must be 8 digits!')
    encoded_password = ''.join(list)
    return encoded_password

def decode():
    pass
if __name__ == "__main__":

    print("Menu\n"
    "-------------\n"
    "1. Encode\n"
    "2. Decode\n"
    "3. Quit\n")

    menu_one=0
    o = int(input("Please enter an option: "))
    while o != 3:

        if o == 1:
            try:
                    menu_one=1
                    password = input("Please enter your password to encode: ")
                    encoded=encode(password)
                    print("Your password has been encoded and stored!")
            except ValueError as excpt:
                    print(excpt)
                    print('Add a new password')
        elif o == 2:
            if menu_one == 1:
                try:
                    print(f"The encoded password is {encoded}, and the original password is ORIGINALPASSWORD.")
                except ValueError as excpt:
                    print(excpt)
                    print('Add a new password')

            else:
                print("Menu one must be called before menu two.")

        elif o == 3:
            break
        else:
            print("Invalid input.")

        print("\nMenu\n"
        "-------------\n"
        "1. Encode\n"
        "2. Decode\n"
        "3. Quit")
        o = int(input("\nPlease enter an option: "))



