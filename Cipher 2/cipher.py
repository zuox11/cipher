import tkinter as tk
from tkinter import filedialog, messagebox

# ============================== Vigenère Cipher ==============================

def generate_key_vigenere(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(plaintext, key):
    ciphertext = []
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            x = (ord(plaintext[i].upper()) + ord(key[i].upper()) - 2 * ord('A')) % 26
            x += ord('A')
            ciphertext.append(chr(x))
        else:
            ciphertext.append(plaintext[i])
    return "".join(ciphertext)

def decrypt_vigenere(ciphertext, key):
    plaintext = []
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            x = (ord(ciphertext[i].upper()) - ord(key[i].upper()) + 26) % 26
            x += ord('A')
            plaintext.append(chr(x))
        else:
            plaintext.append(ciphertext[i])
    return "".join(plaintext)

# ============================== Playfair Cipher ==============================

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

def process_text_playfair(text, for_encrypt=True):
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
    plaintext = process_text_playfair(plaintext, for_encrypt=True)
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
    ciphertext = process_text_playfair(ciphertext, for_encrypt=False)
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

# ============================== Hill Cipher ==============================

def calculate_determinant(matrix):
    # Untuk matriks 2x2
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def matrix_inverse(matrix):
    # Untuk matriks 2x2
    det = calculate_determinant(matrix)
    det = det % 26
    if det == 0:
        return None
    # Cari invers det modulo 26
    det_inv = None
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    if det_inv is None:
        return None
    # Adjugate matriks
    adjugate = [
        [ matrix[1][1], -matrix[0][1]],
        [-matrix[1][0],  matrix[0][0]]
    ]
    # Kembalikan invers matriks modulo 26
    inverse = []
    for row in adjugate:
        inverse_row = []
        for element in row:
            inv_element = (det_inv * element) % 26
            inverse_row.append(inv_element)
        inverse.append(inverse_row)
    return inverse

def generate_key_matrix_hill(key, size=2):
    key = "".join([c.upper() for c in key if c.isalpha()]).replace("J", "I")
    if len(key) < size * size:
        raise ValueError(f"Kunci harus memiliki minimal {size * size} karakter untuk matriks {size}x{size}.")
    key_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(ord(key[i * size + j]) - 65)
        key_matrix.append(row)
    inverse = matrix_inverse(key_matrix)
    if inverse is None:
        raise ValueError("Matriks kunci tidak invertible modulo 26.")
    return key_matrix, inverse

def multiply_matrix_vector(matrix, vector):
    result = []
    for row in matrix:
        sum = 0
        for i in range(len(vector)):
            sum += row[i] * vector[i]
        result.append(sum % 26)
    return result

def hill_encrypt(plaintext, key, size=2):
    plaintext = ''.join([c.upper() for c in plaintext if c.isalpha()]).replace("J", "I")
    # Padding jika diperlukan
    while len(plaintext) % size != 0:
        plaintext += 'X'
    ciphertext = ""
    key_matrix, _ = generate_key_matrix_hill(key, size)

    for i in range(0, len(plaintext), size):
        vector = [ord(c) - 65 for c in plaintext[i:i+size]]
        cipher_vector = multiply_matrix_vector(key_matrix, vector)
        ciphertext += ''.join([chr(num + 65) for num in cipher_vector])
    return ciphertext

def hill_decrypt(ciphertext, key, size=2):
    ciphertext = ''.join([c.upper() for c in ciphertext if c.isalpha()]).replace("J", "I")
    plaintext = ""
    key_matrix, inverse_matrix = generate_key_matrix_hill(key, size)

    for i in range(0, len(ciphertext), size):
        vector = [ord(c) - 65 for c in ciphertext[i:i+size]]
        plain_vector = multiply_matrix_vector(inverse_matrix, vector)
        plaintext += ''.join([chr(num + 65) for num in plain_vector])
    return plaintext

# ============================== GUI Setup ==============================

class CipherApp:
    def __init__(self, master):
        self.master = master
        master.title("Kriptografi Cipher")
        master.geometry("800x500")
        master.resizable(False, False)

        # Pemilihan Cipher
        self.cipher_var = tk.StringVar(value="Vigenere")
        cipher_label = tk.Label(master, text="Pilih Cipher:", font=("Arial", 12))
        cipher_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        cipher_options = ["Vigenere", "Playfair", "Hill"]
        self.cipher_menu = tk.OptionMenu(master, self.cipher_var, *cipher_options)
        self.cipher_menu.config(width=15, font=("Arial", 12))
        self.cipher_menu.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        # Input Plainteks/Cipherteks
        message_label = tk.Label(master, text="Pesan:", font=("Arial", 12))
        message_label.grid(row=1, column=0, padx=10, pady=10, sticky='nw')
        self.message_entry = tk.Text(master, height=8, width=60, font=("Arial", 12))
        self.message_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        # Tombol Upload File
        self.upload_button = tk.Button(master, text="Upload File", command=self.open_file, font=("Arial", 10))
        self.upload_button.grid(row=1, column=3, padx=10, pady=10, sticky='n')

        # Input Kunci
        key_label = tk.Label(master, text="Kunci (min 12 karakter):", font=("Arial", 12))
        key_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.key_entry = tk.Entry(master, width=60, font=("Arial", 12))
        self.key_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # Tombol Enkripsi dan Dekripsi
        self.encrypt_button = tk.Button(master, text="Enkripsi", command=self.encrypt_message, font=("Arial", 12), bg="green", fg="white")
        self.encrypt_button.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        self.decrypt_button = tk.Button(master, text="Dekripsi", command=self.decrypt_message, font=("Arial", 12), bg="blue", fg="white")
        self.decrypt_button.grid(row=3, column=2, padx=10, pady=10, sticky='w')

        # Label untuk menampilkan hasil enkripsi/dekripsi
        result_label = tk.Label(master, text="Hasil:", font=("Arial", 12))
        result_label.grid(row=4, column=0, padx=10, pady=10, sticky='nw')
        self.result_text = tk.Text(master, height=8, width=60, font=("Arial", 12), fg="blue")
        self.result_text.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

        # Tombol Simpan Hasil
        self.save_button = tk.Button(master, text="Simpan Hasil", command=self.save_file, font=("Arial", 10))
        self.save_button.grid(row=4, column=3, padx=10, pady=10, sticky='n')

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    message = file.read()
                    self.message_entry.delete('1.0', tk.END)  # Kosongkan input pesan
                    self.message_entry.insert(tk.END, message)  # Masukkan pesan dari file ke input
            except Exception as e:
                messagebox.showerror("Error", f"Gagal membuka file: {str(e)}")

    def save_file(self):
        result = self.result_text.get('1.0', tk.END).strip()
        if not result:
            messagebox.showerror("Error", "Tidak ada hasil untuk disimpan.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(result)
                messagebox.showinfo("Sukses", "Hasil berhasil disimpan.")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyimpan file: {str(e)}")

    def encrypt_message(self):
        cipher = self.cipher_var.get()
        message = self.message_entry.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter.")
            return

        try:
            if cipher == "Vigenere":
                key_gen = generate_key_vigenere(message, key)
                ciphertext = encrypt_vigenere(message, key_gen)
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, ciphertext)
            elif cipher == "Playfair":
                ciphertext = playfair_encrypt(message, key)
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, ciphertext)
            elif cipher == "Hill":
                size = 2  # Menggunakan matriks 2x2
                ciphertext = hill_encrypt(message, key, size)
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, ciphertext)
            else:
                messagebox.showerror("Error", "Cipher tidak dikenali.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mengenkripsi: {str(e)}")

    def decrypt_message(self):
        cipher = self.cipher_var.get()
        ciphertext = self.message_entry.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()

        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter.")
            return

        try:
            if cipher == "Vigenere":
                key_gen = generate_key_vigenere(ciphertext, key)
                plaintext = decrypt_vigenere(ciphertext, key_gen)
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, plaintext)
            elif cipher == "Playfair":
                plaintext = playfair_decrypt(ciphertext, key)
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, plaintext)
            elif cipher == "Hill":
                size = 2  # Sesuaikan dengan ukuran matriks yang digunakan
                plaintext = hill_decrypt(ciphertext, key, size)
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, plaintext)
            else:
                messagebox.showerror("Error", "Cipher tidak dikenali.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mendekripsi: {str(e)}")

# ============================== Main ==============================

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
