# cipher
Quiz Kriptografi
Penjelasan Kode
A. Vigenère Cipher:
- generate_key_vigenere: Menghasilkan kunci sepanjang pesan dengan mengulang kunci asli jika diperlukan.
- encrypt_vigenere: Mengenkripsi pesan dengan Vigenère Cipher.
- decrypt_vigenere: Mendekripsi pesan dengan Vigenère Cipher.

B. Playfair Cipher:
- generate_playfair_matrix: Membuat matriks Playfair 5x5 berdasarkan kunci yang diberikan.
- find_position: Mencari posisi suatu karakter dalam matriks.
- process_text_playfair: Memproses teks menjadi bigram (pasangan dua huruf), menambahkan 'X' jika diperlukan.
- playfair_encrypt: Mengenkripsi pesan menggunakan Playfair Cipher.
- playfair_decrypt: Mendekripsi pesan menggunakan Playfair Cipher.

C. Hill Cipher:
- calculate_determinant: Menghitung determinan untuk matriks 2x2.
- matrix_inverse: Menghitung invers matriks 2x2 modulo 26.
- generate_key_matrix_hill: Membuat matriks kunci dan inversnya.
- multiply_matrix_vector: Mengalikan matriks dengan vektor.
- hill_encrypt: Mengenkripsi pesan menggunakan Hill Cipher dengan matriks 2x2.
- hill_decrypt: Mendekripsi pesan menggunakan Hill Cipher dengan matriks 2x2.

D. GUI Setup (Class CipherApp):
- Pemilihan Cipher: Dropdown menu untuk memilih antara Vigenère, Playfair, dan Hill Cipher.
- Input Pesan: Text widget untuk memasukkan pesan secara langsung.
- Upload File: Tombol untuk mengupload file .txt dan memasukkan isinya ke input pesan.
- Input Kunci: Entry widget untuk memasukkan kunci (minimal 12 karakter).
- Enkripsi dan Dekripsi: Tombol untuk melakukan enkripsi atau dekripsi berdasarkan cipher yang dipilih.
- Hasil: Text widget untuk menampilkan hasil enkripsi atau dekripsi.
- Simpan Hasil: Tombol untuk menyimpan hasil ke file .txt.

E. Main:
Membuat dan menjalankan aplikasi Tkinter.

F. Contoh Penggunaan

Vigenère Cipher:
1. Pilih Cipher: Pilih "Vigenere" dari dropdown menu.
2. Masukkan Pesan: Ketikkan "HELLO WORLD" di area pesan.
3. Masukkan Kunci: Masukkan "CRYPTOGRAPHYKEY" (minimal 12 karakter).
4. Enkripsi: Klik "Enkripsi".
5. Hasil: Ciphertext akan ditampilkan, misalnya "BMNDZBXDKYBE".
6. Dekripsi: Klik "Dekripsi" untuk mengembalikan ciphertext ke plaintext asli, hasilnya akan "HELXLOWORLD".

Playfair Cipher:
1. Pilih Cipher: Pilih "Playfair" dari dropdown menu.
2. Masukkan Pesan: Ketikkan "HELLO WORLD" di area pesan.
3. Masukkan Kunci: Masukkan "CRYPTOGRAPHYKEY" (minimal 12 karakter).
4. Enkripsi: Klik "Enkripsi".
5. Hasil: Ciphertext akan ditampilkan sesuai dengan aturan Playfair Cipher.
6. Dekripsi: Klik "Dekripsi" untuk mengembalikan ciphertext ke plaintext asli, hasilnya akan "HELXLOWORLD".

Hill Cipher:
1. Pilih Cipher: Pilih "Hill" dari dropdown menu.
2. Masukkan Pesan: Ketikkan "HELLOWORLD" di area pesan.
3. Masukkan Kunci: Masukkan "GYBNQKURPXXX" (pastikan minimal 12 karakter untuk matriks 2x2).
4. Enkripsi: Klik "Enkripsi".
5. Hasil: Ciphertext akan ditampilkan sesuai dengan aturan Hill Cipher.
6. Dekripsi: Klik "Dekripsi" untuk mengembalikan ciphertext ke plaintext asli, hasilnya akan "HELLOWORLD".

