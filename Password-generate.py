import string
import random

def generate_password(length):
    # Define possible character sets
    letters = string.ascii_letters     # A-Z, a-z
    digits = string.digits             # 0-9
    symbols = string.punctuation       # Special characters like @, #, $, etc.

    # Combine all character sets
    all_characters = letters + digits + symbols

    # Ensure at least one character from each type for better strength
    if length < 4:
        return "⚠️ Password length should be at least 4 for good security."

    # Randomly choose characters
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the remaining length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

def main():
    print("===== PASSWORD GENERATOR =====")
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        return

    password = generate_password(length)
    print(f"\n🔑 Generated Password: {password}")
    print("==============================")

if __name__ == "__main__":
    main()
