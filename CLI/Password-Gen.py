import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        chars = string.ascii_lowercase
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits
    elif complexity == "high":
        chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# prompt the user for password length and complexity
while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Password length must be greater than zero")
        break
    except ValueError:
        print("Invalid password length. Please enter a positive integer greater than zero.")

while True:
    complexity = input("Enter password complexity (low, medium, high): ")
    if complexity not in ["low", "medium", "high"]:
        print("Invalid complexity level. Please choose from 'low', 'medium', or 'high'.")
    else:
        break

# generate the password
password = generate_password(length=length, complexity=complexity)
print("Your generated password is:", password)
