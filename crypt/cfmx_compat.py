from crypt.transformer import Transformer
from coder.uucoder import UUCoder

class CFMXCompat:
    DEFAULT_ENCODING = "uu"
    UU = "uu"

    def __init__(self):
        pass

    @staticmethod
    def encrypt(plain, key, encoding=DEFAULT_ENCODING):
        transformer = Transformer()
        if encoding.lower() == CFMXCompat.UU:
            return UUCoder.encode(transformer.transform_string(key, plain.encode())).strip()
        else:
            return None

    @staticmethod
    def decrypt(encrypted, key, encoding=DEFAULT_ENCODING):
        transformer = Transformer()
        if encoding.lower() == CFMXCompat.UU:
            return transformer.transform_string(key, UUCoder.decode(encrypted)).decode()
        else:
            return None
