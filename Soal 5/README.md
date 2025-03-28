# Soal 5 : Affine Cipher

## **1. Analisis Ciphertext dan Persamaan**

Affine Cipher dalam ruang 256 karakter menggunakan formula:

$$
C = (m×P+b)mod  256
$$

Untuk mendekripsi, kita perlu menemukan nilai m dan b menggunakan dua pasangan plaintext-ciphertext yang diketahui:

- P1=0xFF (255), C1=0xB7 (183)
- P2=0xD8 (216), C2=0x32 (50)

Dari sini, kita membentuk sistem persamaan modular:

$$
183 = (m×255+b) mod 256
$$

$$
50 = (m×216+b) mod  256
$$

Kemudian, kita menyelesaikan sistem ini untuk mendapatkan nilai m dan b.

### **2. Perhitungan untuk Mendapatkan Nilai m dan b**

Gunakan kode python atau perhitungan secara manual untuk menyelesaikan sistem persamaan:

```jsx
import sympy as sp

# Diketahui pasangan plaintext-ciphertext:
P1, C1 = 0xFF, 0xB7  # (255, 183)
P2, C2 = 0xD8, 0x32  # (216, 50)
n = 256  # Ruang karakter

# Mencari nilai m dan b dari persamaan modular
mod_diff = (C1 - C2) % n  # (183 - 50) % 256
plain_diff = (P1 - P2) % n  # (255 - 216) % 256

# Mencari invers modular dari plain_diff modulo n
m_value = sp.mod_inverse(plain_diff, n) * mod_diff % n

# Setelah mendapatkan m, mencari b
b_value = (C1 - m_value * P1) % n

print(f"Nilai m: {m_value}, Nilai b: {b_value}")
```

Ditemukan bahwa:

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcpRUlPA2UiIf69aUoTgDupkp02jkDPypY6YY3-M0udEu9tj1UqDZc_4kgrcKzQmrJze7GpJBcu_J7uc3d2ojXRGXcVsb5ZQXbZFwi2H1y9uc3357krr5hlkcYzlxOQF0N2hFvx?key=BWl4315OOuI2mE2xbK8K5AW9)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfqiF2EHnsrNHI1Gdv5TPBfk8Ve2VxAgLPr_dD3HiaiC9ywMXE86YkOvbjXTGFhV3t6jwT6gVQ04TKNGlNuJf0bq6wMoZcNY3yR2zXOPDYRG9T2lGtDWHbF9K3-hhfc1e3BnqnssQ?key=BWl4315OOuI2mE2xbK8K5AW9)

Nilai m 115 dan nilai b 42

## **3. Kode untuk Memulihkan Gambar**

```jsx
import sympy as sp

def read_image_to_hex(image_path):
    """Membaca file gambar dan mengonversi ke array heksadesimal."""
    with open(image_path, "rb") as image:
        return [hex(byte) for byte in image.read()]

def affine_decrypt(cipher_hex, m, b, n):
    """Mendekripsi setiap byte gambar menggunakan Affine Cipher."""
    decrypted_hex = []
    m_inv = sp.mod_inverse(m, n)
    
    for hex_value in cipher_hex:
        if hex_value.startswith('0x'):
            hex_value = hex_value[2:]
        C = int(hex_value, 16)
        P = (m_inv * (C - b)) % n
        decrypted_hex.append(P)
    
    return bytearray(decrypted_hex)

def save_decrypted_image(output_path, decrypted_bytes):
    """Menyimpan gambar hasil dekripsi."""
    with open(output_path, "wb") as file:
        file.write(decrypted_bytes)

# Jalankan proses dekripsi
image_path = "affinecipher.jpeg"
cipher_hex = read_image_to_hex(image_path)
decrypted_bytes = affine_decrypt(cipher_hex, 115, 42, 256)
save_decrypted_image("decrypted_image.jpeg", decrypted_bytes)
print("Gambar berhasil didekripsi dan disimpan sebagai decrypted_image.jpeg")
```

Setelah mendapatkan array heksadesimal hasil dekripsi, kita mengubahnya kembali ke dalam file gambar dan menyimpan hasilnya.

### **4. Hasil Dekripsi**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcz4Q5i175BiX9Jk_wh6Sf4o4U2gtT-57hZO-75xGyDZPyEFSzpxA3EGa3i7QO_0FP58Ckxb3AmaZa3eldRjiQJtudCHpp9Y8_bgvqpkubAb_iRvv8aARPAtrDviQ-SctSQ3lwRpQ?key=BWl4315OOuI2mE2xbK8K5AW9)

### **5. Waktu Kriptanalisis**

Proses analisis dan dekripsi diselesaikan dalam sekitar 20 **menit**.

### **6. Perbandingan dengan Pendekatan Brute Force / Exhaustive Key Attack (Optional)**

Pendekatan brute force dalam Affine Cipher memerlukan pencarian semua kemungkinan pasangan hingga menemukan kombinasi yang menghasilkan dekripsi yang valid.

Dalam ruang 256 karakter, nilai m harus relatif prima dengan 256.  Namun, kita hanya bisa menggunakan bilangan ganjil sebagai m, karena semua bilangan genap memiliki faktor 2 dan tidak memiliki invers modular dalam mod 256. Dari 128 bilangan yang relatif prima terhadap 256, hanya 95 bilangan yang ganjil yang dapat digunakan sebagai m. Sehingga total kemungkinan pasangan:

128 x 256 = 24320

Pendekatan brute force akan membutuhkan iterasi melalui setiap pasangan, menguji hasil dekripsi, dan memeriksa apakah menghasilkan gambar yang valid. Jika dibandingkan dengan pendekatan aljabar modular yang kita gunakan, metode sistem persamaan jauh lebih cepat dan efisien dibanding brute force, yang memakan waktu signifikan lebih lama.

Kode eksplorasi brute force untuk mencari nilai m dan b :

```jsx
from itertools import product
import sympy as sp
import math

n = 256
known_plaintext = [(0xFF, 0xB7), (0xD8, 0x32)]
for m, b in product(range(n), repeat=2):
    if math.gcd(m, n) == 1:  # m harus memiliki invers modular
        if all((m * P + b) % n == C for P, C in known_plaintext):
            print(f"Ditemukan: m = {m}, b = {b}")
            break
```
