# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def encode_password(password):
    encoded_password = ''
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password


def decode_password(encoded_password):
    decoded_password = ''
    for digit in encoded_password:
        new_digit = str((int(digit) - 3) % 10)
        decoded_password += new_digit
    return decoded_password


def decoder(user_password):
    numbers = []
    decoded_value = 0
    for num in user_password:
        string_to_num = int(num)
        decoded_value = string_to_num - 3
        if decoded_value == -1:
            decoded_value = 9
        elif decoded_value == -2:
            decoded_value = 8
        elif decoded_value == -3:
            decoded_value = 7

        numbers.append(str(decoded_value))

    numbers = ''.join(numbers)

    return numbers


while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = input("Please enter an option: ")

    if choice == '1':
        password = input("Please enter your password to encode: ")
        encoded_password = encode_password(password)
        print("Your password has been encoded and stored!")
        print("Encoded password: " + encoded_password)
    elif choice == '2':
        encoded_password = input("Please enter your password to decode: ")
        decoded_password = decoder(encoded_password)
        print("Your password has been decoded and stored!")
        print("Decoded password: " + decoded_password)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
