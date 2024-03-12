# Programer: Ralph
# Date: 3.12.24
# Program: Password Generator
# Resources: https://www.zdnet.com/article/how-to-write-better-chatgpt-prompts-in-5-steps/

import hashlib


def hash_password(password, salt):
    # Concatenate password and salt
    salted_password = password + salt
    # Hash the salted password using SHA-256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password


def main():
    # Accept password input from the user
    password = input("Enter your password: ")

    # Generate a random salt (for simplicity, you can use a fixed salt if needed)
    salt = "S@ltY&*^"

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)


if __name__ == "__main__":
    main()