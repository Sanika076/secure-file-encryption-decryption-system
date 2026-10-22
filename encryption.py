from cryptography.fernet import Fernet
import base64
import hashlib
import os


def generate_key(password):
    password_bytes = password.encode()
    hashed_password = hashlib.sha256(password_bytes).digest()
    key = base64.urlsafe_b64encode(hashed_password)
    return key


def encrypt_file(file_path, password):
    key = generate_key(password)

    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher.encrypt(file_data)

    filename = os.path.basename(file_path)

    output_path = os.path.join(
        "encrypted_files",
        filename + ".encrypted"
    )

    with open(output_path, "wb") as file:
        file.write(encrypted_data)

    return output_path


if __name__ == "__main__":

    test_file = input("Enter file path: ")

    password = input("Enter password: ")

    encrypted_file = encrypt_file(test_file, password)

    print("\nEncryption Successful!")
    print("Encrypted file saved at:")
    print(encrypted_file)