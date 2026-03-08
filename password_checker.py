import re

common_passwords = ["123456", "password", "12345678", "qwerty", "abc123"]

def password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase password length (minimum 8 characters).")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Common password check
    if password.lower() in common_passwords:
        feedback.append("This is a commonly used password. Choose something unique.")
        score = 0

    return score, feedback


def strength_meter(score):
    bars = "█" * score + "-" * (6 - score)
    return f"[{bars}]"


# Main Program
print(" Advanced Password Strength Checker ")
password = input("Enter your password: ")

score, feedback = password_strength(password)

print("\n--- Password Analysis Report ---")
print("Strength Score:", score, "/ 6")
print("Strength Meter:", strength_meter(score))

if score <= 2:
    print("Overall Strength: Weak ")
elif score <= 4:
    print("Overall Strength: Medium ")
else:
    print("Overall Strength: Strong ")

if feedback:
    print("\nSuggestions to Improve:")
    for tip in feedback:
        print("•", tip)
else:
    print("\nGreat job! Your password is strong ")