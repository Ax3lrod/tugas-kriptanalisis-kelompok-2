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
