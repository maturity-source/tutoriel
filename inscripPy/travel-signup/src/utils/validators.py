import re  # Import moved to the top

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))

def validate_password(password):
    return (
        len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isalpha() for char in password)
    )