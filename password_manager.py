# password_manager.py
from cryptography.fernet import Fernet

# Step 1: Generate a secret key (do this only once)
key = Fernet.generate_key()
print("Your secret key is:", key.decode())

# Step 2: Create a Fernet object
cipher = Fernet(key)

# Step 3: Encrypt a password
password = "MySuperSecret123"
encrypted_password = cipher.encrypt(password.encode())
print("Encrypted password:", encrypted_password)

# Step 4: Decrypt it
decrypted_password = cipher.decrypt(encrypted_password).decode()
print("Decrypted password:", decrypted_password)
