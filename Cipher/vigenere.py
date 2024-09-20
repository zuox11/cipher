def vigenere_encrypt(plaintext, key):
    ciphertext = []
    key_length = len(key)
    key_int = [ord(i.upper()) for i in key]
    for i, char in enumerate(plaintext):
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            cipher_char = chr((ord(char.upper()) + key_int[i % key_length] - 2 * 65) % 26 + offset)
            ciphertext.append(cipher_char)
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key_length = len(key)
    key_int = [ord(i.upper()) for i in key]
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            plain_char = chr((ord(char.upper()) - key_int[i % key_length] + 26) % 26 + offset)
            plaintext.append(plain_char)
        else:
            plaintext.append(char)
    return ''.join(plaintext)
