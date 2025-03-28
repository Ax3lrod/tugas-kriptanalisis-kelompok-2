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

### 1. Tabel Frekuensi Digram dalam Bahasa Inggris

![image.png](image.png)

![image.png](image%201.png)

1. **Tabel Frekuensi Digram dalam Ciphertext**

![image.png](image%202.png)

![image.png](image%203.png)