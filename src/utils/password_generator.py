import random
import string

def generate_password(length):
    """Generates a random password of a given length."""
    if length < 8 or length > 20:
        raise ValueError("Password length must be between 8 and 20 characters.")
    
    # Define possible characters: uppercase, lowercase, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
