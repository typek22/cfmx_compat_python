from crypt.cfmx_compat import CFMXCompat

if __name__ == "__main__":
    # Generate a secure 16-character key
    # import secrets
    # key = secrets.token_hex(8)

    key = "e3548384e1ee4c26"
    encrypted_text = "&6%Z,LJ6Z"
    plain_text = "Rabbit"

    decrypted = CFMXCompat.decrypt(encrypted_text, key)
    encrypted = CFMXCompat.encrypt(plain_text, key)

    print(f"ENCRYPTION original: '{plain_text}', encrypted: '{encrypted}'.")
    print(f"DECRYPTION original: '{encrypted_text}', decrypted: '{decrypted}'.")
