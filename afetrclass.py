import random

def generate_password(length):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    punctuation = "!@#$%^&*()-_=+[]{};:,.<>?/|\\`~"
    characters = lowercase + uppercase + digits + punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter the desired password length: "))
print("Your random password is:", generate_password(length))
