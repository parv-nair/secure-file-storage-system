import os, hashlib, json
from cryptography.fernet import Fernet
from datetime import datetime

KEY_PATH = "keys/secret.key"
LOG_PATH = "logs/log.json"

def generate_key():
    key = Fernet.generate_key()
    os.makedirs("keys", exist_ok=True)
    with open(KEY_PATH, "wb") as f:
        f.write(key)
    print("Key generated and saved.")

def load_key():
    return open(KEY_PATH, "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    enc_file = filename + ".enc"
    with open(enc_file, "wb") as file:
        file.write(encrypted)
    log_file(filename, enc_file, "encrypted")
    print(f"Encrypted: {enc_file}")

def decrypt_file(enc_filename):
    key = load_key()
    fernet = Fernet(key)
    with open(enc_filename, "rb") as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    dec_file = enc_filename.replace(".enc", ".dec")
    with open(dec_file, "wb") as file:
        file.write(decrypted)
    log_file(enc_filename, dec_file, "decrypted")
    print(f"Decrypted: {dec_file}")

def sha256sum(filename):
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def log_file(input_name, output_name, action):
    os.makedirs("logs", exist_ok=True)
    log_entry = {
        "timestamp": str(datetime.now()),
        "action": action,
        "input_file": input_name,
        "output_file": output_name,
        "hash": sha256sum(output_name)
    }
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as log_file:
            data = json.load(log_file)
    else:
        data = []
    data.append(log_entry)
    with open(LOG_PATH, "w") as log_file:
        json.dump(data, log_file, indent=2)

if __name__ == "__main__":
    os.makedirs("files", exist_ok=True)
    print("1. Generate Key\n2. Encrypt File\n3. Decrypt File")
    choice = input("Choose: ")
    if choice == "1":
        generate_key()
    elif choice == "2":
        file = input("Enter file path to encrypt: ")
        encrypt_file(file)
    elif choice == "3":
        file = input("Enter .enc file path to decrypt: ")
        decrypt_file(file)
    else:
        print("Invalid choice.")
