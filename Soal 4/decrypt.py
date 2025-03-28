import numpy as np
import string

def mod_inverse(a, m):
    """Menghitung modular inverse dari a modulo m.
       Mengembalikan x sehingga (a*x) % m == 1, jika ada.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Tidak ada modular inverse untuk {a} modulo {m}")

def matrix_mod_inv(matrix, modulus):
    """Menghitung invers dari matriks 3x3 modulo modulus."""
    det = int(round(np.linalg.det(matrix)))  # hitung determinan asli
    det = det % modulus
    inv_det = mod_inverse(det, modulus)
    
    # Hitung matriks kofaktor
    cof = np.zeros((3,3), dtype=int)
    for i in range(3):
        for j in range(3):
            # Mengambil minor dari elemen (i, j)
            minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
            cof[i][j] = ((-1)**(i+j)) * int(round(np.linalg.det(minor)))
    
    # Matriks adjugate adalah transpose dari kofaktor
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
    modulus = 26
    key_matrix = np.array(key_matrix)
    if key_matrix.shape != (3,3):
        raise ValueError("Key matrix harus berukuran 3x3")
    
    inv_key = matrix_mod_inv(key_matrix, modulus)
    
    # Pastikan panjang ciphertext adalah kelipatan 3
    if len(ciphertext) % 3 != 0:
        raise ValueError("Panjang ciphertext harus kelipatan 3")
    
    plaintext = ""
    # Proses setiap blok 3 huruf
    for i in range(0, len(ciphertext), 3):
        block = ciphertext[i:i+3]
        block_nums = np.array(text_to_numbers(block)).reshape(3, 1)
        decrypted_nums = np.dot(inv_key, block_nums) % modulus
        decrypted_block = numbers_to_text(decrypted_nums.flatten().tolist())
        plaintext += decrypted_block
    return plaintext

if __name__ == "__main__":
    # Key matriks 3x3 sesuai permintaan:
    key = [
        [6, 13, 20],
        [24, 16, 17],
        [1, 10, 15]
    ]
    
    # Ciphertext yang diberikan (pastikan hanya huruf kapital tanpa spasi)
    ciphertext = ("CDECCZDKQFYRYRWYWXKVTSBQABTRVRITRXVVKWKJKEMUEVKLYUPUAFSPPSFSKZVGJKKNLWNFXSMUDVHKSWMFERVUWEVZTZQVOGWALCAYTKXAKNKYDTZMTWATADALYSANZSBMIGPUGNTMHFJRSKSTLQKFRXAKHMOHEYQDUMSFIAMOBSKBFWZKGZEVAKSHQHPGJUKKLNSZAIFCWUKUKWMMJUDVVOWHWXEAVWODIAMOBSDNNNUYYRVRWMPQPYJDZRXDZBJUKOPUXIZQTHSKKHEYATYCONMHOACPMNIESNKZZYBKTZHXCGOABREJCIDCJCRVRWNFCJPCUWYNQGCGSLJDWLCHBWNFLCMGNNTDLMPTLSYFWAUMGWFMWQCCWPLAMTSZXAULWDEADALPBQIDUTSJGSWPGKBIAMOBSOKSPGFBDDLMECGVUDVEEZYCORCJEIOMXENEQUMGZHUUSOSCNSFSMDPALWXAHIDEWNFJOQJLLELRNAUVOQQDUINZIKVMSSSGOMGRHSKZWJVOQASVCKVIZGIQWPIQGJKLWURYLIQBOAZMHOACPMNIESNCUKXWSGIYEBHTYIBEIMHOACPMNIESNSKKHEYOOPTSOFRFHSGBZHXCXATDOOFNOEWKQXHJYCUYUZBPXSMDESDJDOZGANUGMFWSMMLMCYZEVECXLFNUACWPYMHOBSWQCQWROHPVUMDOTEMXBGDANZKNUCSLFSKPCJUGAURCOQZOUEXTFWNFETPUPLZMTAVZQOZCJCRVRWNFYILHSXUSQBXBNSIFSFCWPHAVOHVWCRTNPIWQWLYTEEEQXEMXBUPCAFBXBPGMPGVTFDTDLNGOCPMPUYXHWVZNMVDMZGOZDGQHSGWAQXLZGPGSYUZAPVSBQBXBPGMPGVTFDVGGAWQOPAAVZDSSNLJANNSETBGXSSBFCJ")
    ciphertext += ("DWLCHBWNFMULCJCRVRNWJIUIFFVBVLHYCKKSTRZPQICAQUUPEKMEYLECLAHACASRIADDUVDHIQWZAIORLZMCAIEOMJNGONEDVCCOGXQMPXHJYCUYUZJOQDTJMXFWQCEQXQJOMJPOJIABTRVRPUYEDSDDHSUOFIUTQJFESFWGATDZQVZVHBHZAPVSBQCBOXUNFQGZZPKSQQDUWUTGYNXLXFYEVZAYRFLAMDUNZUMPVDZZDMETGIVHMDNHXAXPLLNCAYNSVDNAXSMVVLYDTCRPLRFLAMTSZXAULWDHCVAKKOHPVUMKJOSQGQBWYKLKRQSKKMMJLWWWTCYKEUGNWBGKNLWUTRYYYBLOIDNWREQXACLBEVUDVDECEQXMFWFRFUMONGIENMOEY")
    
    try:
        hasil = decrypt_hill(ciphertext, key)
        print("Plaintext:", hasil)
    except Exception as e:
        print("Terjadi kesalahan:", e)
