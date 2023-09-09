import bcrypt

# Function to hash a password
def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Function to verify a password
def verify_password(input_password, hashed_password):
    # Check if the input password matches the hashed password
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

# Example usage
if __name__ == "__main__":
    # User registration: Hash the user's password before storing it in the database
    user_password = "my_secure_password"
    hashed_password = hash_password(user_password)

    # Simulate user login: Verify the entered password with the hashed password in the database
    entered_password = "my_secure_password"  # This would typically come from the user
    if verify_password(entered_password, hashed_password):
        print("Password is correct. User authenticated.")
    else:
        print("Incorrect password. Authentication failed.")
