import logging  # Import logging for messages
from cryptography.fernet import Fernet  # Import Fernet for encryption/decryption

# Set up logging configuration
logging.basicConfig(level=logging.INFO)  # Show INFO level logs and above

# -----------------------------
# STEP 1: Create and save a key
# -----------------------------
def write_key():
    """
    Generates a new encryption key and saves it to a file.
    Only run this ONCE unless you want to overwrite your current key.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    logging.info("Key has been written to key.key")  # Log key written

# Uncomment the line below to generate the key the first time
# write_key()

# --------------------------
# STEP 2: Load the key
# --------------------------
def load_key():
    """
    Loads the encryption key from the key file.
    Needed before creating a Fernet cipher object.
    """
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
        logging.info("Key has been loaded from key.key")  # Log success
        return key
    except FileNotFoundError:
        logging.error("Error: 'key.key' file not found. Please generate the key file first.")  # Log error if key not found
        raise

# ---------------------------------
# STEP 3: Encrypt the password text
# ---------------------------------
def encrypt_password(cipher, password):
    """
    Encrypts a plaintext password using the Fernet cipher.
    """
    try:
        encrypted_password = cipher.encrypt(password.encode())  # Convert to bytes and encrypt
        logging.info("Password encrypted successfully.")  # Log encryption success
        return encrypted_password
    except Exception as e:
        logging.error(f"Error encrypting password: {e}")  # Log error if encryption fails
        raise

# -----------------------------------------------
# STEP 4: Save the encrypted password to a file
# -----------------------------------------------
def save_encrypted_password(encrypted_password):
    """
    Saves the encrypted password to a file on disk.
    """
    try:
        with open("encrypted_password.txt", "wb") as file:
            file.write(encrypted_password)
        logging.info("Encrypted password saved to 'encrypted_password.txt'.")  # Log save success
    except Exception as e:
        logging.error(f"Error saving encrypted password: {e}")  # Log save error
        raise

# ---------------------------------------------
# STEP 5: Decrypt an encrypted password string
# ---------------------------------------------
def decrypt_password(cipher, encrypted_password):
    """
    Decrypts an encrypted password using the Fernet cipher.
    """
    try:
        decrypted_password = cipher.decrypt(encrypted_password).decode()  # Decrypt and decode to string
        logging.info("Password decrypted successfully.")  # Log decryption success
        return decrypted_password
    except Exception as e:
        logging.error(f"Error decrypting password: {e}")  # Log error if decryption fails
        raise

# ------------------------------------------------------
# STEP 6: Load an encrypted password from a saved file
# ------------------------------------------------------
def load_encrypted_password():
    """
    Loads the encrypted password from a file to decrypt later.
    """
    try:
        with open("encrypted_password.txt", "rb") as file:
            encrypted_password = file.read()
            logging.info("Encrypted password loaded from 'encrypted_password.txt'.")  # Log load success
            return encrypted_password
    except FileNotFoundError:
        logging.error("Error: 'encrypted_password.txt' file not found.")  # Log error if file not found
        raise

# ---------------------------
# Main menu: User interface
# ---------------------------
def menu():
    """
    Presents the user with a menu to either encrypt a password or decrypt a saved password.
    """
    print("Choose an option:")
    print("1. Encrypt a new password")
    print("2. Decrypt a saved password")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        password = input("Enter the password you want to encrypt: ")  # User input for password
        encrypt_and_save(password)
    elif choice == "2":
        decrypt_and_display()
    else:
        logging.error("Invalid choice. Please select either 1 or 2.")  # Log if input is invalid

# ---------------------------
# Encrypt and save password
# ---------------------------
def encrypt_and_save(password):
    """
    Encrypts the password entered by the user and saves it to a file.
    """
    try:
        key = load_key()  # Load the encryption key
        cipher = Fernet(key)  # Create the cipher
        encrypted_password = encrypt_password(cipher, password)  # Encrypt password
        save_encrypted_password(encrypted_password)  # Save the encrypted password
    except Exception as e:
        logging.error(f"An error occurred while encrypting the password: {e}")  # Log error if encryption fails

# ---------------------------
# Decrypt and display password
# ---------------------------
def decrypt_and_display():
    """
    Loads and decrypts the encrypted password from the file and displays it.
    """
    try:
        key = load_key()  # Load the encryption key
        cipher = Fernet(key)  # Create the cipher
        encrypted_password = load_encrypted_password()  # Load the encrypted password
        decrypted_password = decrypt_password(cipher, encrypted_password)  # Decrypt the password
        print("Decrypted password:", decrypted_password)  # Show decrypted password to the user
    except Exception as e:
        logging.error(f"An error occurred while decrypting the password: {e}")  # Log error if decryption fails

# -------------------------
# Run the menu
# -------------------------
if __name__ == "__main__":
    menu()  # Display the menu to the user
