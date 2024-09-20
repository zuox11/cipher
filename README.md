# cipher
Quiz Kriptografi
Penjelasan Kode
1. Vigenère Cipher:
- generate_key_vigenere: Menghasilkan kunci sepanjang pesan dengan mengulang kunci asli jika diperlukan.
- encrypt_vigenere: Mengenkripsi pesan dengan Vigenère Cipher.
- decrypt_vigenere: Mendekripsi pesan dengan Vigenère Cipher.

2. Playfair Cipher:
- generate_playfair_matrix: Membuat matriks Playfair 5x5 berdasarkan kunci yang diberikan.
- find_position: Mencari posisi suatu karakter dalam matriks.
- process_text_playfair: Memproses teks menjadi bigram (pasangan dua huruf), menambahkan 'X' jika diperlukan.
- playfair_encrypt: Mengenkripsi pesan menggunakan Playfair Cipher.
- playfair_decrypt: Mendekripsi pesan menggunakan Playfair Cipher.

3. Hill Cipher:
- calculate_determinant: Menghitung determinan untuk matriks 2x2.
- matrix_inverse: Menghitung invers matriks 2x2 modulo 26.
- generate_key_matrix_hill: Membuat matriks kunci dan inversnya.
- multiply_matrix_vector: Mengalikan matriks dengan vektor.
- hill_encrypt: Mengenkripsi pesan menggunakan Hill Cipher dengan matriks 2x2.
- hill_decrypt: Mendekripsi pesan menggunakan Hill Cipher dengan matriks 2x2.

4. GUI Setup (Class CipherApp):
- Pemilihan Cipher: Dropdown menu untuk memilih antara Vigenère, Playfair, dan Hill Cipher.
- Input Pesan: Text widget untuk memasukkan pesan secara langsung.
- Upload File: Tombol untuk mengupload file .txt dan memasukkan isinya ke input pesan.
- Input Kunci: Entry widget untuk memasukkan kunci (minimal 12 karakter).
- Enkripsi dan Dekripsi: Tombol untuk melakukan enkripsi atau dekripsi berdasarkan cipher yang dipilih.
- Hasil: Text widget untuk menampilkan hasil enkripsi atau dekripsi.
- Simpan Hasil: Tombol untuk menyimpan hasil ke file .txt.

5. Main:
Membuat dan menjalankan aplikasi Tkinter.

6. Contoh Penggunaan
Vigenère Cipher:

Plaintext: "HELLO WORLD"
Kunci: "CRYPTOGRAPHYKEY"
Ciphertext: "BMNDZBXDKYBE"
Decrypted Text: "HELXLOWORLD"
Playfair Cipher:

Plaintext: "HELLO WORLD"
Kunci: "CRYPTOGRAPHYKEY"
Ciphertext: "BMNDZBXDKYBE" (Contoh, hasil dapat bervariasi)
Decrypted Text: "HELXLOWORLD"
Hill Cipher:

Plaintext: "HELLOWORLD"
Kunci: "GYBNQKURP" (Untuk matriks 3x3, sesuaikan kunci)
Ciphertext: "RFKTMBXVVW"
Decrypted Text: "HELLOWORLD"
