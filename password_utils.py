import re
import hashlib

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must include at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Password must include at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Password must include at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password must include at least one special character."
    return "Strong"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
