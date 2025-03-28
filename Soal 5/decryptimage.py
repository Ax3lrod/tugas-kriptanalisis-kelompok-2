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