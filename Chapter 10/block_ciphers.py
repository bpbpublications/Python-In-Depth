import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes)

def encrypt_3DES(key, iv, plaintext):
    # Build a 3DES-CBC Cipher
    encryptor = Cipher(
        algorithm=algorithms.TripleDES(key),
        mode=modes.CBC(iv),
        backend=default_backend()).encryptor()
    # Padding
    while len(plaintext) % 8 != 0:
        plaintext += b" "

    ciphertext = encryptor.update(plaintext)+ (encryptor.finalize())
    return (iv, ciphertext)

def decrypt_3DES(key, iv, ciphertext):
    # Build a Cipher object, with the key, iv
    decryptor = Cipher(
        algorithm=algorithms.TripleDES(key),
        mode=modes.CBC(iv),
        backend=default_backend()).decryptor()
    return  decryptor.update(ciphertext) + decryptor.finalize()


