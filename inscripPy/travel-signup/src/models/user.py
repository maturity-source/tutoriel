from utils.validators import validate_email, validate_password, validate_username
import hashlib  # For password hashing

class SignupService:
    def __init__(self, user_model):
        self.user_model = user_model

    def register_user(self, name, email, password):
        if not self.validate_user_data(name, email, password):
            raise ValueError("Invalid user data")
        
        hashed_password = self.hash_password(password)
        new_user = self.user_model(name=name, email=email, password=hashed_password)
        
        # Here you would typically save the user to a database
        self.send_confirmation_email(email)
        return new_user

    def validate_user_data(self, name, email, password):
        if not validate_username(name):
            print("Invalid username")
            return False
        if not validate_email(email):
            print("Invalid email")
            return False
        if not validate_password(password):
            print("Invalid password")
            return False
        return True

    def send_confirmation_email(self, email):
        # Placeholder for email sending logic
        print(f"Confirmation email sent to {email}")

    def hash_password(self, password):
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()