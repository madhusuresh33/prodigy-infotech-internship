def get_valid_shift():
    while True:
        try:
            return int(input("Enter the shift value (integer): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_choice():
    while True:
        choice = input("Choose an option: (e)ncrypt or (d)ecrypt: ").lower()
        if choice in ['e', 'd']:
            return choice
        print("Invalid choice. Enter 'e' or 'd'.")
