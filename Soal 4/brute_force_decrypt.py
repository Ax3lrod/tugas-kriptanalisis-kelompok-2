import numpy as np
import string
import itertools

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
    Menghitung invers dari matriks 3x3 secara modular (mod modulus).
    """
    det = int(round(np.linalg.det(matrix))) % modulus
    inv_det = mod_inverse(det, modulus)
    
    cof = np.zeros((3, 3), dtype=int)
    for i in range(3):
        for j in range(3):
            # Hapus baris i dan kolom j untuk mendapatkan minor
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cof[i, j] = ((-1) ** (i + j)) * int(round(np.linalg.det(minor)))
    
    adjugate = cof.T
    inv_matrix = (inv_det * adjugate) % modulus
    return inv_matrix

def text_to_numbers(text):
    """Mengubah teks (A-Z) menjadi list angka 0-25."""
    return [string.ascii_uppercase.index(char) for char in text]

def numbers_to_text(numbers):
    """Mengubah list angka 0-25 menjadi teks (A-Z)."""
    return ''.join([string.ascii_uppercase[num % 26] for num in numbers])

def decrypt_hill(ciphertext, key_matrix):
    """
    Mendekripsi ciphertext menggunakan Hill Cipher dengan key_matrix 3x3.
    Panjang ciphertext harus merupakan kelipatan 3.
    """
    modulus = 26
    if key_matrix.shape != (3, 3):
        raise ValueError("Key matrix harus berukuran 3x3")
    
    inv_key = matrix_mod_inv(key_matrix, modulus)
    
    if len(ciphertext) % 3 != 0:
        raise ValueError("Panjang ciphertext harus kelipatan 3")
    
    plaintext = ""
    for i in range(0, len(ciphertext), 3):
        block = ciphertext[i:i+3]
        block_nums = np.array(text_to_numbers(block)).reshape(3, 1)
        decrypted_nums = np.dot(inv_key, block_nums) % modulus
        plaintext += numbers_to_text(decrypted_nums.flatten().tolist())
    return plaintext

def is_invertible(matrix, modulus):
    """Memeriksa apakah matriks 3x3 invertible modulo modulus."""
    try:
        _ = matrix_mod_inv(matrix, modulus)
        return True
    except Exception:
        return False

def brute_force_decrypt(ciphertext, crib, modulus=26, key_range=range(5)):
    """
    Melakukan brute force terhadap kunci Hill Cipher 3x3.
    
    Parameters:
    - ciphertext: string ciphertext (tanpa spasi, huruf kapital)
    - crib: fragmen plaintext yang diketahui muncul pada dekripsi yang benar
    - modulus: biasanya 26 untuk alfabet A-Z
    - key_range: rentang nilai yang akan dicoba untuk setiap elemen kunci
    
    Catatan: Untuk ruang pencarian penuh (0-25) jumlah kunci adalah 26^9, sehingga sangat lambat.
    """
    total_keys = len(key_range) ** 9
    print(f"Total kemungkinan kunci yang akan diuji: {total_keys}")
    
    counter = 0
    for key_tuple in itertools.product(key_range, repeat=9):
        counter += 1
        if counter % 1000000 == 0:
            print(f"Telah mencoba {counter} kunci...")
        key_matrix = np.array(key_tuple).reshape(3, 3)
        if not is_invertible(key_matrix, modulus):
            continue
        try:
            plaintext = decrypt_hill(ciphertext, key_matrix)
            if crib in plaintext:
                print("Kunci ditemukan!")
                print("Key matrix:")
                print(key_matrix)
                print("Plaintext:")
                print(plaintext)
                return key_matrix, plaintext
        except Exception:
            continue
    print("Tidak ditemukan kunci yang menghasilkan dekripsi dengan crib yang diberikan dalam ruang pencarian ini.")
    return None, None

if __name__ == "__main__":
    # Ciphertext yang diberikan (harus berupa huruf kapital tanpa spasi dan panjangnya kelipatan 3)
    ciphertext = (
        "CDECCZDKQFYRYRWYWXKVTSBQABTRVRITRXVVKWKJKEMUEVKLYUPUAFSPPSFSKZVGJKKNLWNFXSMUDVHKSWMFERVUWEVZTZQVOGWALCAYTKXAKNKYDTZMTWATADALYSANZSBMIGPUGNTMHFJRSKSTLQKFRXAKHMOHEYQDUMSFIAMOBSKBFWZKGZEVAKSHQHPGJUKKLNSZAIFCWUKUKWMMJUDVVOWHWXEAVWODIAMOBSDNNNUYYRVRWMPQPYJDZRXDZBJUKOPUXIZQTHSKKHEYATYCONMHOACPMNIESNKZZYBKTZHXCGOABREJCIDCJCRVRWNFCJPCUWYNQGCGSLJDWLCHBWNFLCMGNNTDLMPTLSYFWAUMGWFMWQCCWPLAMTSZXAULWDEADALPBQIDUTSJGSWPGKBIAMOBSOKSPGFBDDLMECGVUDVEEZYCORCJEIOMXENEQUMGZHUUSOSCNSFSMDPALWXAHIDEWNFJOQJLLELRNAUVOQQDUINZIKVMSSSGOMGRHSKZWJVOQASVCKVIZGIQWPIQGJKLWURYLIQBOAZMHOACPMNIESNCUKXWSGIYEBHTYIBEIMHOACPMNIESNSKKHEYOOPTSOFRFHSGBZHXCXATDOOFNOEWKQXHJYCUYUZBPXSMDESDJDOZGANUGMFWSMMLMCYZEVECXLFNUACWPYMHOBSWQCQWROHPVUMDOTEMXBGDANZKNUCSLFSKPCJUGAURCOQZOUEXTFWNFETPUPLZMTAVZQOZCJCRVRWNFYILHSXUSQBXBNSIFSFCWPHAVOHVWCRTNPIWQWLYTEEEQXEMXBUPCAFBXBPGMPGVTFDTDLNGOCPMPUYXHWVZNMVDMZGOZDGQHSGWAQXLZGPGSYUZAPVSBQBXBPGMPGVTFDVGGAWQOPAAVZDSSNLJANNSETBGXSSBFCJ"
        "DWLCHBWNFMULCJCRVRNWJIUIFFVBVLHYCKKSTRZPQICAQUUPEKMEYLECLAHACASRIADDUVDHIQWZAIORLZMCAIEOMJNGONEDVCCOGXQMPXHJYCUYUZJOQDTJMXFWQCEQXQJOMJPOJIABTRVRPUYEDSDDHSUOFIUTQJFESFWGATDZQVZVHBHZAPVSBQCBOXUNFQGZZPKSQQDUWUTGYNXLXFYEVZAYRFLAMDUNZUMPVDZZDMETGIVHMDNHXAXPLLNCAYNSVDNAXSMVVLYDTCRPLRFLAMTSZXAULWDHCVAKKOHPVUMKJOSQGQBWYKLKRQSKKMMJLWWWTCYKEUGNWBGKNLWUTRYYYBLOIDNWREQXACLBEVUDVDECEQXMFWFRFUMONGIENMOEY"
    )
    
    # Known plaintext (crib)
    crib = "HELLOCYBERFOXATTACKERHERE"
    
    # Untuk demonstrasi, batasi ruang kunci. Ubah key_range jika diperlukan.
    brute_force_decrypt(ciphertext, crib, modulus=26, key_range=range(5))
