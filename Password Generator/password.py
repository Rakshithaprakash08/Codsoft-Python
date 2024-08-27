import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars
    
    
    if not all_chars:
        raise ValueError("At least one character type must be selected.")
    
    password = [
        random.choice(lowercase_chars) if lowercase_chars else '',
        random.choice(uppercase_chars) if uppercase_chars else '',
        random.choice(digit_chars) if digit_chars else '',
        random.choice(special_chars) if special_chars else ''
    ]
    

    password += [random.choice(all_chars) for _ in range(length - len(password))]
    
    
    random.shuffle(password)
    
    
    return ''.join(password)


if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Do you want to include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Do you want to include digits? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Do you want to include special characters? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print("Generated Password:", password)



