import os

def main_menu():
    """This prints the main menu, setting up a input to be used later"""
    while True:
        print("CAESAR CIPHER MESSSGING")
        print("------------------------")
        print("1. Start a message")
        print("2. Read and reply to a message")
        print("3. Quit")
        User_input = input("Input the nomber: ").strip()
        if User_input == "1":
            print("Message running...")
            return User_input
        elif User_input == "2":
            print("Read and reply running...")
            return User_input
        elif User_input == "3":
            print("Leaving...")
            return User_input
        else:
            print("Needs to be one of the nomber\n")

def Start_message():
    """This function Starts the message part of this program, mainly getting the Caesar Cipher for the next function, End_message"""
    while True:
        alphi = input("Please input a series of characters, no repeats and not empty: ").strip()
        if alphi == "":
            print("Error, there needs to be something\n")
        elif len(alphi) != len(set(alphi)):
            print("Error, No duplicate characters allowed\n")
        else:
            print("Valid message...")
            shift = int(input("How much would you like to shift: "))
            break
    letters = list(alphi)
    Caesar_Cipher = {}
    for i in range(len(letters)):
        Caesar_Cipher[letters[i]] = letters[(i + shift) % len(letters)]
    return Caesar_Cipher, alphi, shift

def new_message(message, alphabet, shift):
    encrypted = ""

    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % len(alphabet)
            encrypted += alphabet[new_position]
        else:
            encrypted += letter

    return encrypted

def End_message(Caesar_Cipher):
    """This functions finishes the message part of this program, showing the encripted message"""
    message = input("Input a message to use: ")
    new_message = ""
    for letter in message:
        if letter in Caesar_Cipher:
            new_message += Caesar_Cipher[letter]
        else:
            new_message += letter
    print(new_message)
    return new_message

def make_file1(alphi, new_message, shift):
    file_path = "encripted_message.txt"
    """This functions makes a file that shows the info of the Start message"""
    if os.path.exists(file_path):
        perm = input("This file already exists. Overwrite it? (Y/N): \n").upper()

        if perm == "Y":
            with open(file_path, "w") as file:
                file.write(f"Your alphabet: {alphi}\nYour shifting: {shift}\nYour message: {new_message}")
        else:
            print("File was not overwritten.")

    else:
        with open(file_path, "w") as file:
            file.write(f"Your alphabet: {alphi}\nYour shifting: {shift}\nYour message: {new_message}")


def Open_file():
    """Function that opens and reads a file and returns the values from it"""
    while True:
        filename = input("Enter filename: ")
        if os.path.exists(filename):
            with open(filename, "r") as file:
                reading = file.readlines()
                alphi = reading[0].strip().split(": ")[1]
                shift = int(reading[1].strip().split(": ")[1])
                for number, line in enumerate(reading[2:], start=1):
                    message = line.strip().split(": ")[1]
                    decrypted = new_message(message, alphi, -shift)
                    print(f"{number}. {decrypted}")
                print(f"You shifted {shift}")
                print(f"Your alphabet: {alphi}")
                return alphi, shift, filename
        else:
            print("File does not exist\n")
def Reply(new_message, alphabet, shift, filename):
    """Takes the reply from the user and adds it to the original file."""
    while True:
        reply = input("Enter your reply: ").strip()

        if reply != "":
            break
        else:
            print("Your reply cannot be empty.\n")
    encrypted = new_message(reply, alphabet, shift)
    print(f"Reply: {encrypted}")
    with open(filename, "a") as file:
        file.write(f"\nYour message: {encrypted}")
    print(f"Your reply has been saved to {file}.\n")

#alphabet, shift, filename = Open_file()
#Reply(new_message, alphabet, shift, filename)
#Caesar_Cipher, alphi, shift = Start_message()
#new_message = End_message(Caesar_Cipher)
#make_file1(alphi, new_message, shift)
while True:
    User_input = main_menu()
    if User_input == "1":
        Caesar_Cipher, alphi, shift = Start_message()
        new_message = End_message(Caesar_Cipher)
        make_file1(alphi, new_message, shift)
    elif User_input == "2":
        alphabet, shift, filename = Open_file()
        Reply(new_message, alphabet, shift, filename)
    elif User_input == "3":
        break
    else:
        print("This shouln't happen")
        break
