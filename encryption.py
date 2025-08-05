from cryptography.fernet import Fernet
import os

# Function to generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("A new secret key has been generated and saved to 'secret.key'.")

# Function to load the key from a file
def load_key():
    if not os.path.exists("secret.key"):
        generate_key()  # Generate a key if it doesn't exist
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"{file_name} has been encrypted.")

# Function to decrypt and show the contents of a file
def decrypt_and_show(file_name):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(file_name, "rb") as encrypted_file:
            encrypted = encrypted_file.read()

        decrypted = fernet.decrypt(encrypted)
        print("\nFile contents:")
        print(decrypted.decode('utf-8'))
    except Exception as e:
        print(f"Error: {e}\n"
              "Possible causes:\n"
              "1. Wrong key was entered\n"
              "2. The file wasn't encrypted with this key\n"
              "3. The file is corrupted")

# Main program
if __name__ == "__main__":
    # Specify the file to encrypt
    file_name = "myfile.txt"  # Change this to your file name

    # Encrypt the file
    encrypt_file(file_name)

    # Prompt for the secret key to view the contents
    secret_key = input("Enter your secret key to view the file contents: ").strip()

    # Attempt to decrypt and show the contents
    try:
        # Set the key from user input
        fernet = Fernet(secret_key.encode())
        decrypt_and_show(file_name)
    except Exception as e:
        print(f"Failed to decrypt the file: {e}")
