import string


def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char in string.ascii_lowercase:
            shifted_index = (string.ascii_lowercase.index(char) + key) % 26
            ciphertext += string.ascii_lowercase[shifted_index]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char in string.ascii_lowercase:
            shifted_index = (string.ascii_lowercase.index(char) - key) % 26
            plaintext += string.ascii_lowercase[shifted_index]
        else:
            plaintext += char
    return plaintext
if __name__ == '__main__':
    message = "hello world!"
    
    ciphertext = encrypt(message, 10)
    print(ciphertext)
    plaintext = decrypt(ciphertext, 10)
    print(plaintext)