from cryptography.fernet import Fernet

# Step 1: Create and save the key (only run this once)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Uncomment the next line to run it and generate the key file
write_key()

# Step 2: Load the key (this will be used later to encrypt and decrypt)
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Now we can use this key to encrypt and decrypt
key = load_key()  # Load the key from the file

# Step 3: Create a Fernet object
cipher = Fernet(key)

# Step 4: Encrypt a password
password = "MySuperSecret123"
encrypted_password = cipher.encrypt(password.encode())
print("Encrypted password:", encrypted_password)

# Step 5: Decrypt the password
decrypted_password = cipher.decrypt(encrypted_password).decode()
print("Decrypted password:", decrypted_password)
