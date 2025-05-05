import os

def file_exists(path):
    return os.path.isfile(path)

def get_valid_key():
    while True:
        try:
            return int(input("Enter an encryption key (integer): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
