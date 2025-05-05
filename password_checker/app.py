from password_strength import check_password_strength

def main():
    print("Password Complexity Checker")
    password = input("Enter a password: ")
    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(" -", tip)

if __name__ == "__main__":
    main()
