print("login.py loaded")
def login(user, password):
    print(f"Logging in user: {user}")
    # Simulate login logic
    if user == "admin" and password == "password":
        return True
    return False
