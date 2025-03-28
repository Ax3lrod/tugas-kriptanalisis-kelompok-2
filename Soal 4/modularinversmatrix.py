import numpy as np

def mod_inverse(a, m):
    """
    Menghitung invers modular dari a modulo m.
    Mengembalikan x sehingga (a * x) % m == 1, jika ada.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Tidak ada invers modular untuk {a} modulo {m}")

def matrix_mod_inv(matrix, modulus):
    """
    Menghitung invers dari matriks 3x3 secara modular.
    
    Langkah-langkah:
    1. Hitung determinan matriks dan ambil modulo modulus.
    2. Hitung invers dari determinan tersebut (modular inverse).
    3. Hitung matriks kofaktor dan ambil transpose (adjugate).
    4. Kalikan adjugate dengan invers determinan dan ambil modulo modulus.
    """
    # Hitung determinan dan ambil modulo modulus
    det = int(round(np.linalg.det(matrix))) % modulus
    inv_det = mod_inverse(det, modulus)
    
    # Hitung matriks kofaktor
    cof = np.zeros((3, 3), dtype=int)
    for i in range(3):
        for j in range(3):
            # Hapus baris i dan kolom j untuk mendapatkan minor
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cof[i, j] = ((-1) ** (i + j)) * int(round(np.linalg.det(minor)))
    
    # Matriks adjugate adalah transpose dari matriks kofaktor
    adjugate = cof.T
    inv_matrix = (inv_det * adjugate) % modulus
    return inv_matrix

if __name__ == "__main__":
    # Matriks kunci yang digunakan
    key = np.array([
        [6, 13, 20],
        [24, 16, 17],
        [1, 10, 15]
    ])
    modulus = 26  # Untuk Hill cipher biasanya menggunakan modulo 26
    
    try:
        inverse_key = matrix_mod_inv(key, modulus)
        print("Invers matriks kunci (mod 26):")
        print(inverse_key)
    except Exception as e:
        print("Terjadi kesalahan:", e)
