import math
import string

def evaluate_password_strength(password):
    # calculate the length of the password
    length = len(password)

    # calculate the entropy of the password
    entropy = 0
    for char in password:
        if char in string.ascii_lowercase:
            entropy += math.log2(26)
        elif char in string.ascii_uppercase:
            entropy += math.log2(26)
        elif char in string.digits:
            entropy += math.log2(10)
        elif char in string.punctuation:
            entropy += math.log2(32)

    # calculate the estimated time to crack the password
    seconds_to_crack = 2 ** entropy / 1_000_000_000 # assuming 1 billion guesses per second

    # convert the estimated time to crack to a human-readable format
    if seconds_to_crack < 60:
        time_to_crack = f"{seconds_to_crack:.2f} seconds"
    elif seconds_to_crack < 60 * 60:
        time_to_crack = f"{seconds_to_crack / 60:.2f} minutes"
    elif seconds_to_crack < 60 * 60 * 24:
        time_to_crack = f"{seconds_to_crack / (60 * 60):.2f} hours"
    else:
        time_to_crack = f"{seconds_to_crack / (60 * 60 * 24):.2f} days"

    # determine the strength of the password
    if entropy < 28:
        strength = "very weak"
    elif entropy < 36:
        strength = "weak"
    elif entropy < 60:
        strength = "reasonable"
    elif entropy < 128:
        strength = "strong"
    else:
        strength = "very strong"

    # return a dictionary containing the password evaluation results
    return {
        "password": password,
        "length": length,
        "entropy": entropy,
        "strength": strength,
        "time_to_crack": time_to_crack
    }

# prompt the user for a password to evaluate
password = input("Enter a password to evaluate: ")

# evaluate the password and print the results
result = evaluate_password_strength(password)
print(f"Password: {result['password']}")
print(f"Length: {result['length']}")
print(f"Entropy: {result['entropy']:.2f}")
print(f"Strength: {result['strength']}")
print(f"Time to crack: {result['time_to_crack']}")
