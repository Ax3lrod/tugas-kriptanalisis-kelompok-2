# Soal 3 : Playfair Cipher

## Deskripsi

Cyber Fox menemukan sebuah dokumen terenkripsi yang ternyata tidak cocok dengan pola Vigenère cipher. Setelah analisis lebih lanjut, diketahui bahwa bagian dari dokumen ini dienkripsi menggunakan Playfair cipher. Playfair cipher menggunakan tabel 5x5 untuk mengenkripsi pasangan huruf (digram). Tujuan dari kriptanalisis ini adalah untuk mendekripsi teks dan menemukan kunci enkripsi yang digunakan.

## Langkah-langkah Analisis

1. **Menghitung Frekuensi Digram dalam Bahasa Inggris**
    - Menggunakan dataset teks dalam bahasa Inggris untuk membangun tabel frekuensi digram umum.
    - Membandingkan dengan referensi frekuensi umum dalam literatur kriptografi.
2. **Menghitung Frekuensi Digram dalam Ciphertext**
    - Mengidentifikasi pola pasangan huruf dalam teks terenkripsi.
    - Menghitung frekuensi kemunculannya dan membandingkannya dengan distribusi normal dalam bahasa Inggris.
3. **Menganalisis Struktur Ciphertext**
    - Mengamati pola repetisi dan aturan dalam Playfair cipher.
    - Mengidentifikasi pasangan huruf yang sering muncul sebagai petunjuk awal.
4. **Merekonstruksi Matriks Kunci Playfair**
    - Berdasarkan analisis distribusi digram, mencoba menyusun kemungkinan matriks kunci 5x5.
    - Menggunakan metode substitusi untuk menyesuaikan matriks hingga cocok dengan pola ciphertext.
5. **Mendekripsi Ciphertext**
    - Menggunakan matriks kunci yang telah ditemukan untuk membalikkan proses enkripsi.
    - Memeriksa apakah hasil dekripsi masuk akal dalam bahasa Inggris.
6. **Validasi & Penyempurnaan Kunci**
    - Jika hasil dekripsi masih kurang masuk akal, melakukan iterasi pada kemungkinan matriks kunci.
    - Memeriksa konsistensi dalam hasil dekripsi untuk memastikan keakuratan kunci.

## Hasil Analisis

1. Tabel Frekuensi Digram dalam Bahasa Inggris
    ![Screenshot 2025-03-28 224114](https://github.com/user-attachments/assets/aa1affb4-0e2c-49a8-b39f-434f37218dc9)
    ![Screenshot 2025-03-28 224135](https://github.com/user-attachments/assets/24e757fc-b790-4c77-ac8b-127772d5106d)

2. **Tabel Frekuensi Digram dalam Ciphertext**

   ![Screenshot 2025-03-28 224312](https://github.com/user-attachments/assets/c7dadec5-8c64-4fb0-8fb9-8a89dde8082c)
   ![Screenshot 2025-03-28 224340](https://github.com/user-attachments/assets/157f9e7e-26e1-4a27-8830-04ffbded1356)

   

   
