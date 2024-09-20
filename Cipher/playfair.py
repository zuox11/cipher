import string

def generate_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' digantikan oleh 'I'
    key = "".join([c.upper() for c in key if c.isalpha()]).replace("J", "I")
    matrix = []
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def process_text(text, for_encrypt=True):
    text = "".join([c.upper() for c in text if c.isalpha()]).replace("J", "I")
    processed = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if (i + 1) < len(text):
            b = text[i + 1]
            if a == b:
                b = 'X'  # Insert 'X' if same letters
                i += 1
            else:
                i += 2
        else:
            b = 'X'
            i += 1
        processed += a + b
    return processed

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = process_text(plaintext, for_encrypt=True)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i + 1]
        pos_a = find_position(matrix, a)
        pos_b = find_position(matrix, b)

        if pos_a and pos_b:
            row_a, col_a = pos_a
            row_b, col_b = pos_b

            if row_a == row_b:
                # Jika kedua huruf dalam satu baris, geser ke kanan
                ciphertext += matrix[row_a][(col_a + 1) % 5]
                ciphertext += matrix[row_b][(col_b + 1) % 5]
            elif col_a == col_b:
                # Jika kedua huruf dalam satu kolom, geser ke bawah
                ciphertext += matrix[(row_a + 1) % 5][col_a]
                ciphertext += matrix[(row_b + 1) % 5][col_b]
            else:
                # Jika tidak sama baris dan kolom, tukar kolom
                ciphertext += matrix[row_a][col_b]
                ciphertext += matrix[row_b][col_a]
        else:
            # Jika salah satu karakter tidak ditemukan dalam matriks
            ciphertext += a + b

    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = generate_playfair_matrix(key)
    ciphertext = process_text(ciphertext, for_encrypt=False)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i + 1]
        pos_a = find_position(matrix, a)
        pos_b = find_position(matrix, b)

        if pos_a and pos_b:
            row_a, col_a = pos_a
            row_b, col_b = pos_b

            if row_a == row_b:
                # Jika kedua huruf dalam satu baris, geser ke kiri
                plaintext += matrix[row_a][(col_a - 1) % 5]
                plaintext += matrix[row_b][(col_b - 1) % 5]
            elif col_a == col_b:
                # Jika kedua huruf dalam satu kolom, geser ke atas
                plaintext += matrix[(row_a - 1) % 5][col_a]
                plaintext += matrix[(row_b - 1) % 5][col_b]
            else:
                # Jika tidak sama baris dan kolom, tukar kolom
                plaintext += matrix[row_a][col_b]
                plaintext += matrix[row_b][col_a]
        else:
            # Jika salah satu karakter tidak ditemukan dalam matriks
            plaintext += a + b

    return plaintext

