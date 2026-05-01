def register_user(name, email, student_id, password):
    user = {
        "name": name,
        "email": email,
        "student_id": student_id,
        "password": password
    }
    return user

def login_user(email, password):
    if email and password:
        return {"status": "success", "email": email}
    return {"status": "failed"}