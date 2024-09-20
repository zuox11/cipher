import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

from hill import hill_decrypt, hill_encrypt
from playfair import playfair_decrypt, playfair_encrypt
from vigenere import vigenere_decrypt, vigenere_encrypt

# Fungsi-fungsi cipher di sini

class CipherApp:
    def __init__(self, master):
        self.master = master
        master.title("Kriptografi Cipher")

        # Pemilihan Cipher
        self.cipher_var = tk.StringVar(value="Vigenere")
        tk.Label(master, text="Pilih Cipher:").grid(row=0, column=0, padx=10, pady=10)
        tk.OptionMenu(master, self.cipher_var, "Vigenere", "Playfair", "Hill").grid(row=0, column=1)

        # Input Plainteks
        tk.Label(master, text="Input Plainteks:").grid(row=1, column=0, padx=10, pady=10)
        self.plaintext_entry = tk.Text(master, height=5, width=40)
        self.plaintext_entry.grid(row=1, column=1)

        tk.Button(master, text="Upload File", command=self.upload_file).grid(row=1, column=2, padx=10)

        # Input Kunci
        tk.Label(master, text="Kunci (min 12 char):").grid(row=2, column=0, padx=10, pady=10)
        self.key_entry = tk.Entry(master, width=30)
        self.key_entry.grid(row=2, column=1)

        # Tombol Enkripsi dan Dekripsi
        tk.Button(master, text="Enkripsi", command=self.encrypt).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(master, text="Dekripsi", command=self.decrypt).grid(row=3, column=1, padx=10, pady=10)

        # Output Cipherteks
        tk.Label(master, text="Hasil:").grid(row=4, column=0, padx=10, pady=10)
        self.result_entry = tk.Text(master, height=5, width=40)
        self.result_entry.grid(row=4, column=1)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                data = file.read()
                self.plaintext_entry.delete('1.0', tk.END)
                self.plaintext_entry.insert(tk.END, data)

    def encrypt(self):
        plaintext = self.plaintext_entry.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()
        cipher = self.cipher_var.get()

        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter.")
            return

        if cipher == "Vigenere":
            ciphertext = vigenere_encrypt(plaintext, key)
        elif cipher == "Playfair":
            ciphertext = playfair_encrypt(plaintext, key)
        elif cipher == "Hill":
            key_matrix = self.get_key_matrix(key)
            if key_matrix is None:
                messagebox.showerror("Error", "Matriks kunci tidak valid.")
                return
            ciphertext = hill_encrypt(plaintext, key_matrix)
        else:
            messagebox.showerror("Error", "Cipher tidak dikenali.")
            return

        self.result_entry.delete('1.0', tk.END)
        self.result_entry.insert(tk.END, ciphertext)

    def decrypt(self):
        ciphertext = self.plaintext_entry.get("1.0", tk.END).strip()
        key = self.key_entry.get().strip()
        cipher = self.cipher_var.get()

        if len(key) < 12:
            messagebox.showerror("Error", "Kunci harus minimal 12 karakter.")
            return

        if cipher == "Vigenere":
            plaintext = vigenere_decrypt(ciphertext, key)
        elif cipher == "Playfair":
            plaintext = playfair_decrypt(ciphertext, key)
        elif cipher == "Hill":
            key_matrix = self.get_key_matrix(key)
            if key_matrix is None:
                messagebox.showerror("Error", "Matriks kunci tidak valid.")
                return
            plaintext = hill_decrypt(ciphertext, key_matrix)
        else:
            messagebox.showerror("Error", "Cipher tidak dikenali.")
            return

        self.result_entry.delete('1.0', tk.END)
        self.result_entry.insert(tk.END, plaintext)

    def get_key_matrix(self, key):
        # Contoh untuk Hill Cipher 2x2
        # Pastikan panjang kunci sesuai dengan ukuran matriks
        key = ''.join([c.upper() for c in key if c.isalpha()])
        size = 2
        if len(key) < size*size:
            return None
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(ord(key[i*size + j]) - 65)
            matrix.append(row)
        return np.array(matrix)

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
