# password_util.py
import hashlib

def encrypt_password(password):
    # Simple hash function for demonstration purposes
    return hashlib.md5(password.encode()).hexdigest()

def check_password(current_password, entered_password):
    return encrypt_password(entered_password) == current_password
