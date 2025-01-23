# UUCoder and Transformer Encryption/Decryption

This project provides a Python implementation of a custom encryption/decryption algorithm that uses an encoding system similar to UUEncoding. It also includes a transformation algorithm utilizing Linear Feedback Shift Registers (LFSRs) for data encryption. The project supports encoding and decoding text using this transformation and encoding.

## Project Structure


## Requirements

- Python 3.x
- No external dependencies are required, only built-in Python libraries.

## Features

- **UUCoder**: Implements encoding and decoding using UUEncoding format.
- **Transformer**: Implements a custom LFSR-based transformation algorithm for encryption/decryption.
- **CFMXCompat**: Provides a high-level interface for encrypting and decrypting data using both the UUCoder and Transformer.

## Usage

### Run right away
```bash
$ python main.py
```

### Adjust the parameter in main.py and run
```python
key = "86090ec89fa81d7b"
encrypted_text = "#2 B+"
plain_text = "Cat"
```
```bash
$ python main.py
```
```console
ENCRYPTION original: 'Cat', encrypted: '#3P:8'.
DECRYPTION original: '#2 B+', decrypted: 'Dog'.
```


### Or incorporate into your project
```python
from crypt.cfmx_compat import CFMXCompat

key = "e3548384e1ee4c26"
encrypted_text = "&6%Z,LJ6Z"
plain_text = "Rabbit"

decrypted = CFMXCompat.decrypt(encrypted_text, key)
encrypted = CFMXCompat.encrypt(plain_text, key)
```

