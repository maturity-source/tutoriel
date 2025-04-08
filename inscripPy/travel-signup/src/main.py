def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    return False

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True

def validate_username(username):
    # Username must be alphanumeric and between 3-20 characters
    if len(username) < 3 or len(username) > 20:
        return False
    if not username.isalnum():
        return False
    return True

def validate_phone_number(phone_number):
    import re
    phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format
    if re.match(phone_regex, phone_number):
        return True
    return False

def validate_age(age):
    # Age must be a positive integer and at least 18
    if not isinstance(age, int) or age < 18:
        return False
    return True