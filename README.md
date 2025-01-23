# Python CFMX_COMPAT ColdFusion Encryption/Decryption

This project provides a Python implementation of the ColdFusion <a href="https://helpx.adobe.com/coldfusion/cfml-reference/coldfusion-functions/functions-e-g/encrypt.html">encrypt</a> and <a href="https://helpx.adobe.com/coldfusion/cfml-reference/coldfusion-functions/functions-c-d/Decrypt.html">decrypt</a> functions with the default configuration. This project provides the exact same functionality as ColdFusion's built-in encryption and decryption, ensuring compatibility for applications that need to work with ColdFusion-encrypted data.

The implementation is based on the open-source <a href="https://github.com/getrailo/railo">Railo project</a>, ensuring accuracy and compatibility with ColdFusion's encryption standards.

⚠️ The CFMX_COMPAT algorithm, used in ColdFusion for encryption, is known for its significant security weaknesses. It should NOT be used for encryption of any data.

Instead, it can be used for:
- Interoperability with ColdFusion
- Decoding ColdFusion-Encrypted Data
- ColdFusion to Python Migration
- Reverse Engineering & Security Audits

## Features

- Compatible with ColdFusion's default encryption and decryption functions.
- **UUCoder**: Implements encoding and decoding using UUEncoding format.
- **Transformer**: Implements a LFSR-based transformation algorithm for encryption/decryption.
- **CFMXCompat**: Provides a high-level interface for encrypting and decrypting data using both the UUCoder and Transformer.



## Requirements

- Python 3.x
- No external dependencies are required, only built-in Python libraries.

## Usage

### Run right away
```bash
$ git clone https://github.com/typek22/cfmx_compat_python
$ cd cfmx_compat_python
$ python main.py
```

### Adjust the parameter in main.py and run
```python
key = "86090ec89fa81d7b"
encrypted_text = "#2 B+"
plain_text = "Cat"
```
```console
$ python main.py

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
This is the same as following CFML code
```cfm
<cfscript>
    key = "e3548384e1ee4c26";
    encrypted_text = "&6%Z,LJ6Z"
    plain_text = "Rabbit"
	
    decrypted = decrypt(encrypted_text, key);
    encrypted = encrypt(plain_text, key);
</cfscript>
```
