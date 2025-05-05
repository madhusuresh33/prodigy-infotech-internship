from caesar_cipher import caesar_encrypt, caesar_decrypt
from utils import get_choice, get_valid_shift

def main():
    print("Welcome to Caesar Cipher Tool!")
    choice = get_choice()
    message = input("Enter your message: ")
    shift = get_valid_shift()

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted Message:", encrypted)
    else:
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()
