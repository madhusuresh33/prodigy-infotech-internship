from image_cipher import encrypt_image, decrypt_image
from utils import file_exists, get_valid_key

def main():
    print("Image Encryption Tool")

    choice = input("Choose: (e)ncrypt or (d)ecrypt: ").lower()
    path = input("Enter the image file path: ")

    if not file_exists(path):
        print("File not found.")
        return

    key = get_valid_key()
    output_path = input("Enter output file path: ")

    if choice == 'e':
        encrypt_image(path, output_path, key)
    elif choice == 'd':
        decrypt_image(path, output_path, key)
    else:
        print("Invalid choice. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()
