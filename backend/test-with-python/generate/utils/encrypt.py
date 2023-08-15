from cryptography.fernet import Fernet

# Fixed encryption key (replace with your own key)
# key = Fernet.generate_key()
encryption_key = b'D5s9W_xr7Otl5bxJuwDYRoL8g_2NpioOMzy6RX6IWlg='


def encrypt_string(plain_text):
    # Create a Fernet cipher instance with the encryption key
    cipher = Fernet(encryption_key)

    # Convert the plain text to bytes
    plain_text_bytes = plain_text.encode()

    # Encrypt the bytes using the cipher
    encrypted_bytes = cipher.encrypt(plain_text_bytes)

    # Convert the encrypted bytes to a string
    encrypted_string = encrypted_bytes.decode()

    return encrypted_string


def decrypt_string(encrypted_string):
    # Create a Fernet cipher instance with the encryption key
    cipher = Fernet(encryption_key)

    # Convert the encrypted string to bytes
    encrypted_bytes = encrypted_string.encode()

    # Decrypt the bytes using the cipher
    decrypted_bytes = cipher.decrypt(encrypted_bytes)

    # Convert the decrypted bytes to a string
    decrypted_string = decrypted_bytes.decode()

    return decrypted_string


# Example usage
message = "Hello, World!"

# Encrypt the message
encrypted_message = encrypt_string(message)
print("Encrypted Message:", encrypted_message)

# Decrypt the encrypted message
decrypted_message = decrypt_string(encrypted_message)
print("Decrypted Message:", decrypted_message)
