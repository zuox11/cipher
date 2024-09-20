import numpy as np

def hill_encrypt(plaintext, key_matrix):
    plaintext = ''.join([c.upper() for c in plaintext if c.isalpha()])
    n = key_matrix.shape[0]
    # Padding jika diperlukan
    while len(plaintext) % n != 0:
        plaintext += 'X'
    ciphertext = ""
    for i in range(0, len(plaintext), n):
        vector = np.array([ord(c) - 65 for c in plaintext[i:i+n]])
        cipher_vector = np.dot(key_matrix, vector) % 26
        ciphertext += ''.join([chr(num + 65) for num in cipher_vector])
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = pow(det, -1, 26)
    adjugate = det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    plaintext = ""
    n = key_matrix.shape[0]
    for i in range(0, len(ciphertext), n):
        vector = np.array([ord(c) - 65 for c in ciphertext[i:i+n]])
        plain_vector = np.dot(adjugate, vector) % 26
        plaintext += ''.join([chr(num + 65) for num in plain_vector])
    return plaintext
