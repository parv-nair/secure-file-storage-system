# 🔐 Secure File Storage System with AES Encryption

A simple Python-based command-line tool that lets you **encrypt and decrypt files** using **AES-256 (Fernet)** encryption. The tool logs all actions (encryption & decryption) and verifies file integrity using **SHA-256** hashes.


---
This project has bee done using python.

## 🚀 Features of SFSSWAESE

- 🔐 AES-256 encryption/decryption via `cryptography`
- 📁 Works on any file format (text, image, etc.)
- 🧾 Logs file name, timestamps, hashes, and actions
- 🗝️ Secure key generation and reuse
- 💻 Command-line interface (CLI)



---

## 🛠️ Technologies Used

- Python 3.11+
- [cryptography](https://pypi.org/project/cryptography/)
- `hashlib`, `json`, `os`, `datetime`

---

## 📦 Project Structure

```

secure-file-storage-system/
├── main.py               # Main script
├── files/                # Add files to encrypt/decrypt here
├── keys/                 # Contains the AES key (auto-generated)
│   └── secret.key
├── logs/                 # Logs actions (auto-generated)
│   └── log.json
```

---

## 🧪 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/parv-nair/secure-file-storage-system.git
cd secure-file-storage-system
```

### 2. Install Dependencies
```bash
pip install cryptography
```

### 3. Run the Script
```bash
python main.py
```

### 4. Follow Menu Options:
```
1. Generate Key
2. Encrypt File
3. Decrypt File
```

- Add your test files to the `files/` folder.
- The script auto-generates `keys/secret.key` and `logs/log.json`.

---

## 📝 Example

```bash
> python main.py
1. Generate Key
2. Encrypt File
3. Decrypt File
Choose: 1
Key generated and saved.

Choose: 2
Enter file path to encrypt: files/hello.txt
Encrypted: files/hello.txt.enc
```

---

## 📜 License

MIT License © [Parvathy V Nair](https://github.com/parv-nair)

---

## 🌐 Live Link

GitHub Repo: [https://github.com/parv-nair/secure-file-storage-system](https://github.com/parv-nair/secure-file-storage-system)

---

## 🙌 Contributions

Pull requests are welcome! For major changes, open an issue first to discuss what you would like to change.
