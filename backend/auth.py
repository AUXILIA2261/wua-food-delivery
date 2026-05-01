import re
import hashlib

def hash_password(password):
    """Hash a password using SHA256."""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email):
    """Validate email format using regex."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def register_user(name, email, student_id, password):
    """Register a new user with validated email and hashed password."""
    if not validate_email(email):
        return {"error": "Invalid email format"}
    return {"name": name, "email": email,
            "student_id": student_id, "password": hash_password(password)}

def login_user(email, password):
    """Login an existing user."""
    if not validate_email(email):
        return {"status": "failed", "error": "Invalid email"}
    return {"status": "success", "email": email}