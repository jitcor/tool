import binascii
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter


def int_of_string(s):
    return int(binascii.hexlify(s), 16)


def encrypt_message(key, plaintext):
    iv = os.urandom(16)
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return iv + aes.encrypt(plaintext)


def decrypt_message(key, ciphertext):
    iv = ciphertext[:16]
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext[16:])


key = bytes([0x6B, 0x66, 0xD0, 0xEF, 0x0B, 0x58, 0x21, 0xBC, 0x46, 0x1E, 0x6D, 0x86, 0xCD, 0xD9, 0xB7, 0x6C])
print(decrypt_message(key, encrypt_message(key, "1234567".encode('utf-8'))))
