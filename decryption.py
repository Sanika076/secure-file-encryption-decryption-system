from cryptography.fernet import Fernet
import hashlib
import base64
import os

def generate_key(password):
    password_bytes = password.encode()
    hashed_password = hashlib.sha256(password_bytes).digest()
    key = base64.urlsafe_b64encode(hashed_password)
    return key

def decrypt_file(file_path, password):
    key = generate_key(password)

    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    filename = os.path.basename(file_path)

    if filename.endswith(".encrypted"):
        filename = filename[:-10]

    output_path = os.path.join(
        "decrypted_files",
        filename
    )

    with open(output_path, "wb") as file:
        file.write(decrypted_data)

    return output_path


if __name__ == "__main__":

    test_file = input("Enter encrypted file path: ")

    password = input("Enter password: ")

    decrypted_file = decrypt_file(test_file, password)

    print("\nDecryption Successful!")
    print("Decrypted file saved at:")
    print(decrypted_file)