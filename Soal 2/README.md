# Soal 2 : Vigenere Cipher

## Ciphertext:

<aside>
🔑

UIGVTZGBSGPEPWAIKRKXUNIKDIWRETNCSWMMULRNAEOONQOBERBOOYWSLYQTCZMZMKQTGDYCLVUYIEICSEQTTPGBSCXGREOPVRQRYWIPWWWXBTLVAFVYOQPOGGTKWZRVVNQJEPNCMIQTGEHOKVKARTTIGWJUTSSDGIMJAYDDJRVYMTTDWULGTLCBQGBUGCAZZZKSENHKFZASSFNNWIXONPSCWEBOAWPBGKWIOWSZSIBOCFLKJCGZRLNCHFZZLLYOJJMIUCIDQKTYWSIMZWIIIWIDSKMYRZBEKKMTCCYZLZWTANRYKJVAMPRYMJIVPWIMSKQUNDHYOVDKROECHZBKIESCAXVOFTCKFTMIRJPDGXZGPSYSKZVNECEXLCGJEWIMSKMOTDSOULZOTJCKFSMKNEIBWCGIOXPBGDQYEOBISJQTGWENWJQMNQLKOFZIOOIXYDQYTLKOUFVBEYTSGEIRSZFDORZKTPSDAEOGPARYSTPKSDUMZRAANTTDWJBONRABWZVGDPQESKMLOCDOLVKZIYGFMCVKRLBSDZBOEDIXUIGVTZGBSGPOCDYCLVUYIYSDWRLZHPIBKVKARTTIAJDGLTDKLVLZHCOEYYZOGZRYMJUGTSEWSKQIAWAXSCGYIDAXVWWXMLLZJFWLSOEWGEAZRLTSFXIJHPROFTMZOPSCWEBOAWSOULZOTJPBAEKOPWECLYMYEARYGWAUFEEXVVXKNOOXJVIYOYALDVIYSFMZLZWTSEOCMSAZAYTSSKMZHPIBUCIOMDOXWFNZHPEKJCQKSEPYDPIRPSALWKQIEYCBQGBOOYTOUYVOQFECAJBNEGIQWEZKCTPRWILKVPLYHVLONEHOLYKKNEUBQLVRIVECADXREDULKKQZUEIYFTQVHPRCNZOKNCEOFTZEPEIYFVUVLZYCSIMVELTSFXSKYHOBVKWJEEEBEZVKLPTDWIANIQTCERSONRIDEFZKRPSSKKITTEOPJVYAEYCISEIRYDICXFZIEYTEJZMYIEWKKTWTSTDOJVLANMROSBIHLPDEWKWOTDCYEGTKXTTIUFUVACENLFUUNZAVHYIHEEIMUZXNECSRGNMBECIDAJVUWPACACGJENIZZVZKDFSSFXBKCSNSILMYSFCRSJBNEVACAJSOEIAWAEIZIZNYJWZKQFEXUPITAWYCAJWLRPPOSKQTGAADLVZTSTNDZVKOPSEBLVFZDPSZAKMOTDHSKKWXINAVADXUREAXUVBNEGIQWEZKCTPRWIVULZNQWIXXOGINWJIJEBUKLVAKCFRSLPPOGSLSYYBONRAUWPXXIYCSHCMONXONWIVIRJPDGXZGPSYDJLMVRZTOUKQUNCEVAVATOEOXDPWTSPCBWTGHUEAVKFWTSERYFXUGTSEWSKQIAWFYMELGTTOXKRVJCZMZMKIZIZNKDZVLELSSTZTOTJ

</aside>

## Langkah-langkah pemecahan:

### A. Mencari panjang kemungkinan kunci:

1. Memakai metode kasiski untuk mengetahui panjang pola pengulangan. Metode kasiski akan menghasilkan panjang kunci dan frekuensinya. Langkah ini bisa diselesaikan menggunakan tools [https://asecuritysite.com/cracking/kasiski](https://asecuritysite.com/cracking/kasiski)
    
    Hasilnya sebagai berikut:
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfRJ7PXfik7ZzcnAWQBDVxERzm4FY8INNOqYpysJKioOujuACUavtAgniY6yrjVUvksbDroaRE3KuL7jMLmf11B69ysMaG1WFWnbNtIb07bB5D-oKsIGI_3I4XRYeXWxaUPeOMDMg?key=Tw4qhX_reK5k-AFVZaTFTvVX)
    
    Outputnya adalah daftar jumlah huruf dan frekuensi pengulangannya dan prediksi panjang kunci yaitu (2 4 8 16 3 6 12 13 11 5 10 7 14 9 15). Frekuensi paling tinggi adalah panjang 2 huruf, yaitu 371. Disusul dengan panjang 4 huruf 354, panjang 8 huruf 347, panjang 16 huruf 175 dan seterusnya. Namun, tidak bisa langsung disimpulkan bahwa frekuensi tertinggi berarti kunci yang benar. Kita harus melakukan analisis IC (Index Coincidence).
    
2. Menentukan panjang kunci yang berkemungkinan besar menjadi panjang kunci yang benar dengan IC (Indeks coincidence).
    
    IC atau *Index coincidence* adalah indeks untuk mengukur seberapa sering pasangan huruf yang sama muncul dalam sebuah teks.
    
    Rumusnya adalah sebagai berikut:
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcEgB3KqOdGFbE5Dww9a6841sKwjafD4l5WqlAEub1kHvGdx_wv38QcfhaWk8cLchu00Rkgs3hxvME-WLI4tzQ1Pug9g_LOeq6T01ei0pNA0m9P0MyHWg_iVfq0907CXqVXpxMw?key=Tw4qhX_reK5k-AFVZaTFTvVX)
    
    N = panjang teks yang dianalisis
    
    *nc* = adalah frekuensi c *letters* dari *alphabet*
    
    c = jumlah alphabet yaitu 26
    
    Langkah ini bisa diselesaikan dengan menggunakan tools [https://www.dcode.fr/index-coincidence](https://www.dcode.fr/index-coincidence)
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc_vGxiEq2a9DYN1_1lwYzO7EfEIvt37NwkZYOwRcmi-JSS1eZ0elHc_DJjKcE1y17VUjUpyBtTg1H_SVAsKWLt_RfMpkU2mq0R6xY1xESYUJTEWAXJhb95q-cVdmbVY3BTNaDlJQ?key=Tw4qhX_reK5k-AFVZaTFTvVX)
    
    Hasil lengkap analisa IC tiap panjang kunci adalah sebagai berikut:
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf7ZyVAX3Uz1djzYHzBsrZ7o3qfay_FtZFtOTG5q9P3iWOWCUrXkLSP-8qMwv9efi6wBO6IMOwG_c9XcOFQT0EQiYa7O7XeUkDRQ-RKoEebge6Y9sn0o_l5AM6ASst4GaOobTc2?key=Tw4qhX_reK5k-AFVZaTFTvVX)
    
    Dari hasil di atas, nampak bahwa panjang kunci 16 memiliki IC tertinggi yaitu 0.06631, yang artinya jika kita membagi ciphertext menjadi 16 kelompok, maka setiap kelompok itu punya distribusi huruf yang mirip dengan bahasa Inggris alami. Namun, mengingat nanti kita akan melakukan pendekatan bruteforce (meski hanya sebagai pembanding) yang berarti memakai kombinasi, angka 16 sangatlah besar. Maka ambil angka yang IC-nya besar dengan panjang yang tak terlalu besar yaitu 8.
    

### B. Menemukan kunci enkripsi

Jika memakai tools [https://www.dcode.fr/vigenere-cipher](https://www.dcode.fr/vigenere-cipher) tinggal mengisi kolom Knowing the key-length/size, number of letters = 8

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdeD5BrhN4jqvuo8L7LevL9wMQzNAo2bF_Afz43cCH-vxYCrceTPjItDtbzwEvijCp9k8VsEuGA4CwkyduTqtQle_M-b4HlISgyvOpnQBDbsqWr77JWUmEmHZ8VrwQKmsNdp_38?key=Tw4qhX_reK5k-AFVZaTFTvVX)

Kemudian decrypt dan akan muncul berbagai kemungkinan kunci enkripsi dan hasil enkripsinya. Dokumentasi di bawah sudah terurut dari hasil yang paling mungkin:

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfiOWCG2EW7IGJPc_4puaePfA9LyzLph9QUP4Bn3jcAWWIYg_v-FEZAfGqSICNsAUoj7W6dlj-bR_N_wW0v6C0CeOJjRwxZ9ZwnPNAgrx2puy9waVjSGkXtK-qvgHwdm_e06MPy?key=Tw4qhX_reK5k-AFVZaTFTvVX)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcW02obKnJrdrwm2sTjqugbiLLD2-00d4wRPqJoBYmgGvy-4Hmv6eI3NQr32CA53QldMjhPsGpOLjQ6l4wg04SHbDHCPMmiASG7sf4xIZJHHPg1rQu-DXkkFc_2_b_E8Ltxx6iuVg?key=Tw4qhX_reK5k-AFVZaTFTvVX)

Dari hasil di atas, ditemukan bahwa kunci enkripsi paling mungkin adalah “**SRIGALAK**”

### C. Tabel substitusi huruf

Memakai rumus:

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd3SLDKWCDQTSe4_z0f5gQcOXQpbvI4G3xo8G39e1qDvOLHEXmHJJvXu8I8WE9ywIwWYBuSzIXb-EG_3ceOzp76m3y4Z1fyWcZT3LkxYzX0HVlWIssk_U-7WKcFGWlutzX6Wa-RMQ?key=Tw4qhX_reK5k-AFVZaTFTvVX)

C = ciphertext (huruf terenkripsi)

P = plaintext (huruf asli)

K = key (huruf kunci)

Automasi menggunakan kode python:

```jsx
# Fungsi untuk mendekripsi dengan Vigenère Cipher
def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key_repeated = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
   
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')  # Konversi ke indeks 0-25
        k = ord(key_repeated[i]) - ord('A')  # Konversi kunci ke indeks 0-25
        p = (c - k) % 26  # Dekripsi karakter
        plaintext.append(chr(p + ord('A')))  # Kembalikan ke huruf

    return ''.join(plaintext)

# Data input
ciphertext = "UIGVTZGBSGPEPWAIKRKXUNIKDIWRETNCSWMMULRNAEOONQOBERBOOYWSLYQTCZMZMKQTGDYCLVUYIEICSEQTTPGBSCXGREOPVRQRYWIPWWWXBTLVAFVYOQPOGGTKWZRVVNQJEPNCMIQTGEHOKVKARTTIGWJUTSSDGIMJAYDDJRVYMTTDWULGTLCBQGBUGCAZZZKSENHKFZASSFNNWIXONPSCWEBOAWPBGKWIOWSZSIBOCFLKJCGZRLNCHFZZLLYOJJMIUCIDQKTYWSIMZWIIIWIDSKMYRZBEKKMTCCYZLZWTANRYKJVAMPRYMJIVPWIMSKQUNDHYOVDKROECHZBKIESCAXVOFTCKFTMIRJPDGXZGPSYSKZVNECEXLCGJEWIMSKMOTDSOULZOTJCKFSMKNEIBWCGIOXPBGDQYEOBISJQTGWENWJQMNQLKOFZIOOIXYDQYTLKOUFVBEYTSGEIRSZFDORZKTPSDAEOGPARYSTPKSDUMZRAANTTDWJBONRABWZVGDPQESKMLOCDOLVKZIYGFMCVKRLBSDZBOEDIXUIGVTZGBSGPOCDYCLVUYIYSDWRLZHPIBKVKARTTIAJDGLTDKLVLZHCOEYYZOGZRYMJUGTSEWSKQIAWAXSCGYIDAXVWWXMLLZJFWLSOEWGEAZRLTSFXIJHPROFTMZOPSCWEBOAWSOULZOTJPBAEKOPWECLYMYEARYGWAUFEEXVVXKNOOXJVIYOYALDVIYSFMZLZWTSEOCMSAZAYTSSKMZHPIBUCIOMDOXWFNZHPEKJCQKSEPYDPIRPSALWKQIEYCBQGBOOYTOUYVOQFECAJBNEGIQWEZKCTPRWILKVPLYHVLONEHOLYKKNEUBQLVRIVECADXREDULKKQZUEIYFTQVHPRCNZOKNCEOFTZEPEIYFVUVLZYCSIMVELTSFXSKYHOBVKWJEEEBEZVKLPTDWIANIQTCERSONRIDEFZKRPSSKKITTEOPJVYAEYCISEIRYDICXFZIEYTEJZMYIEWKKTWTSTDOJVLANMROSBIHLPDEWKWOTDCYEGTKXTTIUFUVACENLFUUNZAVHYIHEEIMUZXNECSRGNMBECIDAJVUWPACACGJENIZZVZKDFSSFXBKCSNSILMYSFCRSJBNEVACAJSOEIAWAEIZIZNYJWZKQFEXUPITAWYCAJWLRPPOSKQTGAADLVZTSTNDZVKOPSEBLVFZDPSZAKMOTDHSKKWXINAVADXUREAXUVBNEGIQWEZKCTPRWIVULZNQWIXXOGINWJIJEBUKLVAKCFRSLPPOGSLSYYBONRAUWPXXIYCSHCMONXONWIVIRJPDGXZGPSYDJLMVRZTOUKQUNCEVAVATOEOXDPWTSPCBWTGHUEAVKFWTSERYFXUGTSEWSKQIAWFYMELGTTOXKRVJCZMZMKIZIZNKDZVLELSSTZTOTJ"
key = "SRIGALAK"

# Dekripsi ciphertext
plaintext = vigenere_decrypt(ciphertext, key)

# Membuat tabel manual untuk 50 huruf pertama
print("===================================================")
print("| Pos | Ciphertext | Kunci | Plaintext |")
print("===================================================")
for i in range(50):
    print(f"| {i+1:3} |     {ciphertext[i]}      |   {key[i % len(key)]}   |     {plaintext[i]}     |")
    print("---------------------------------------------------")
```

Kode di atas bisa diatur untuk mengeluarkan jumlah baris output yang diinginkan, saya memilih 50 output sebagai sample. Berikut outputnya dalam bentuk tabel substitusi huruf:

<aside>
👉🏻

===================================================

| Pos | Ciphertext | Kunci | Plaintext |

===================================================

|   1 |     U      |   S   |     C     |

- --------------------------------------------------

|   2 |     I      |   R   |     R     |

- --------------------------------------------------

|   3 |     G      |   I   |     Y     |

- --------------------------------------------------

|   4 |     V      |   G   |     P     |

- --------------------------------------------------

|   5 |     T      |   A   |     T     |

- --------------------------------------------------

|   6 |     Z      |   L   |     O     |

- --------------------------------------------------

|   7 |     G      |   A   |     G     |

- --------------------------------------------------

|   8 |     B      |   K   |     R     |

- --------------------------------------------------

|   9 |     S      |   S   |     A     |

- --------------------------------------------------

|  10 |     G      |   R   |     P     |

- --------------------------------------------------

|  11 |     P      |   I   |     H     |

- --------------------------------------------------

|  12 |     E      |   G   |     Y     |

- --------------------------------------------------

|  13 |     P      |   A   |     P     |

- --------------------------------------------------

|  14 |     W      |   L   |     L     |

- --------------------------------------------------

|  15 |     A      |   A   |     A     |

- --------------------------------------------------

|  16 |     I      |   K   |     Y     |

- --------------------------------------------------

|  17 |     K      |   S   |     S     |

- --------------------------------------------------

|  18 |     R      |   R   |     A     |

- --------------------------------------------------

|  19 |     K      |   I   |     C     |

- --------------------------------------------------

|  20 |     X      |   G   |     R     |

- --------------------------------------------------

|  21 |     U      |   A   |     U     |

- --------------------------------------------------

|  22 |     N      |   L   |     C     |

- --------------------------------------------------

|  23 |     I      |   A   |     I     |

- --------------------------------------------------

|  24 |     K      |   K   |     A     |

- --------------------------------------------------

|  25 |     D      |   S   |     L     |

- --------------------------------------------------

|  26 |     I      |   R   |     R     |

- --------------------------------------------------

|  27 |     W      |   I   |     O     |

- --------------------------------------------------

|  28 |     R      |   G   |     L     |

- --------------------------------------------------

|  29 |     E      |   A   |     E     |

- --------------------------------------------------

|  30 |     T      |   L   |     I     |

- --------------------------------------------------

|  31 |     N      |   A   |     N     |

- --------------------------------------------------

|  32 |     C      |   K   |     S     |

- --------------------------------------------------

|  33 |     S      |   S   |     A     |

- --------------------------------------------------

|  34 |     W      |   R   |     F     |

- --------------------------------------------------

|  35 |     M      |   I   |     E     |

- --------------------------------------------------

|  36 |     M      |   G   |     G     |

- --------------------------------------------------

|  37 |     U      |   A   |     U     |

- --------------------------------------------------

|  38 |     L      |   L   |     A     |

- --------------------------------------------------

|  39 |     R      |   A   |     R     |

- --------------------------------------------------

|  40 |     N      |   K   |     D     |

- --------------------------------------------------

|  41 |     A      |   S   |     I     |

- --------------------------------------------------

|  42 |     E      |   R   |     N     |

- --------------------------------------------------

|  43 |     O      |   I   |     G     |

- --------------------------------------------------

|  44 |     O      |   G   |     I     |

- --------------------------------------------------

|  45 |     N      |   A   |     N     |

- --------------------------------------------------

|  46 |     Q      |   L   |     F     |

- --------------------------------------------------

|  47 |     O      |   A   |     O     |

- --------------------------------------------------

|  48 |     B      |   K   |     R     |

- --------------------------------------------------

|  49 |     E      |   S   |     M     |

- --------------------------------------------------

|  50 |     R      |   R   |     A     |

- --------------------------------------------------
</aside>

### D. Plaintext hasil dekripsi

<aside>
🔓

CRYPTOGRAPHYPLAYSACRUCIALROLEINSAFEGUARDINGINFORMATIONWITHINCOMPUTINGSYSTEMSITISANINTEGRALPARTOFDAILYLIFEFORBILLIONSOFPEOPLEWORLDWIDEENSURINGTHESECURITYOFBOTHSTOREDANDTRANSMITTEDDATACRYPTOGRAPHICMECHANISMSUNDERPINESSENTIALPROTOCOLSPARTICULARLYTRANSPORTLAYERSECURITYTLSWHICHFACILITATESROBUSTENCRYPTIONACROSSNUMEROUSAPPLICATIONSHOWEVERDESPITEITSSIGNIFICANCECRYPTOGRAPHYISINHERENTLYDELICATEITSSECURITYCANBEENTIRELYCOMPROMISEDBYASINGLEDESIGNFLAWORCODINGMISTAKECONVENTIONALSOFTWARETESTINGAPPROACHESSUCHASUNITTESTINGAREINADEQUATEFORDETECTINGVULNERABILITIESINCRYPTOGRAPHICSYSTEMSINSTEADTHEIRSECURITYISVALIDATEDTHROUGHRIGOROUSMATHEMATICALANALYSISANDFORMALPROOFSDEMONSTRATINGADHERENCETOESSENTIALSECURITYPRINCIPLESTHESEPROOFSOFTENDEPENDONREASONABLEASSUMPTIONSTOSUBSTANTIATETHEIRCLAIMSONEOFTHEEARLIESTPOLYALPHABETICENCRYPTIONTECHNIQUESISTHEVIGENRECIPHERDEVELOPEDINTHETHCENTURYUNLIKESIMPLESUBSTITUTIONCIPHERSVIGENREENCRYPTIONEMPLOYSAREPEATINGKEYWORDTODETERMINELETTERSHIFTSMAKINGITMORERESISTANTTOFREQUENCYANALYSISFORCENTURIESITWASCONSIDEREDUNBREAKABLEDUETOITSCOMPLEXITYCOMPAREDTOMONOALPHABETICCIPHERSHOWEVERITISNOWEASILYDECIPHEREDUSINGTECHNIQUESSUCHASTHEKASISKIEXAMINATIONORFREQUENCYANALYSISOFREPEATINGPATTERNSINTHECIPHERTEXTDESPITEITSHISTORICALIMPORTANCETHEVIGENRECIPHERNOLONGERPROVIDESADEQUATESECURITYHIGHLIGHTINGAKEYPRINCIPLEINMODERNCRYPTOGRAPHYTRUEPROTECTIONRELIESNOTONLYONSECRECYBUTALSOONSTRONGMATHEMATICALFOUNDATIONSANDCOMPUTATIONALINFEASIBILITY

</aside>

### E. Waktu kriptanalisis yang dibutuhkan

Tools yang digunakan ada 3 tautan sebagai berikut:

1. [https://asecuritysite.com/cracking/kasiski](https://asecuritysite.com/cracking/kasiski)
2. [https://www.dcode.fr/index-coincidence](https://www.dcode.fr/index-coincidence)
3. [https://www.dcode.fr/vigenere-cipher](https://www.dcode.fr/vigenere-cipher)

Anggap rata-rata waktu membuka dan menjalankan analisis di tiap website adalah 25 detik, ditambah waktu membuat dan menjalankan skrip tabel substitusi sekitar 2-4 menit maka hanya butuh kurang lebih 5 menit untuk kriptanalisis.

### F. Perbandingan dengan pendekatan Brute Force untuk menemukan kunci enkripsi setelah menentukan bahwa panjang kunci enkripsi adalah 8 karakter.

1. Menemukan huruf paling sering muncul tiap kolomnya dengan code python

```jsx
from collections import Counter
import string

def analyze_most_frequent(ciphertext, key_length):
    columns = ['' for _ in range(key_length)]
   
    # Memisahkan teks menjadi beberapa kolom berdasarkan panjang kunci
    for i, char in enumerate(ciphertext):
        if char in string.ascii_uppercase:  # Hanya huruf A-Z
            columns[i % key_length] += char
   
    # Menentukan huruf paling sering muncul di setiap kolom
    most_frequent_letters = []
    for col in columns:
        counter = Counter(col)
        most_common = counter.most_common(1)  # Ambil huruf dengan jumlah terbanyak
        if most_common:
            most_frequent_letters.append(most_common[0][0])
        else:
            most_frequent_letters.append('-')  # Jika kolom kosong, beri tanda '-'
   
    return most_frequent_letters

# Contoh penggunaan
ciphertext = "UIGVTZGBSGPEPWAIKRKXUNIKDIWRETNCSWMMULRNAEOONQOBERBOOYWSLYQTCZMZMKQTGDYCLVUYIEICSEQTTPGBSCXGREOPVRQRYWIPWWWXBTLVAFVYOQPOGGTKWZRVVNQJEPNCMIQTGEHOKVKARTTIGWJUTSSDGIMJAYDDJRVYMTTDWULGTLCBQGBUGCAZZZKSENHKFZASSFNNWIXONPSCWEBOAWPBGKWIOWSZSIBOCFLKJCGZRLNCHFZZLLYOJJMIUCIDQKTYWSIMZWIIIWIDSKMYRZBEKKMTCCYZLZWTANRYKJVAMPRYMJIVPWIMSKQUNDHYOVDKROECHZBKIESCAXVOFTCKFTMIRJPDGXZGPSYSKZVNECEXLCGJEWIMSKMOTDSOULZOTJCKFSMKNEIBWCGIOXPBGDQYEOBISJQTGWENWJQMNQLKOFZIOOIXYDQYTLKOUFVBEYTSGEIRSZFDORZKTPSDAEOGPARYSTPKSDUMZRAANTTDWJBONRABWZVGDPQESKMLOCDOLVKZIYGFMCVKRLBSDZBOEDIXUIGVTZGBSGPOCDYCLVUYIYSDWRLZHPIBKVKARTTIAJDGLTDKLVLZHCOEYYZOGZRYMJUGTSEWSKQIAWAXSCGYIDAXVWWXMLLZJFWLSOEWGEAZRLTSFXIJHPROFTMZOPSCWEBOAWSOULZOTJPBAEKOPWECLYMYEARYGWAUFEEXVVXKNOOXJVIYOYALDVIYSFMZLZWTSEOCMSAZAYTSSKMZHPIBUCIOMDOXWFNZHPEKJCQKSEPYDPIRPSALWKQIEYCBQGBOOYTOUYVOQFECAJBNEGIQWEZKCTPRWILKVPLYHVLONEHOLYKKNEUBQLVRIVECADXREDULKKQZUEIYFTQVHPRCNZOKNCEOFTZEPEIYFVUVLZYCSIMVELTSFXSKYHOBVKWJEEEBEZVKLPTDWIANIQTCERSONRIDEFZKRPSSKKITTEOPJVYAEYCISEIRYDICXFZIEYTEJZMYIEWKKTWTSTDOJVLANMROSBIHLPDEWKWOTDCYEGTKXTTIUFUVACENLFUUNZAVHYIHEEIMUZXNECSRGNMBECIDAJVUWPACACGJENIZZVZKDFSSFXBKCSNSILMYSFCRSJBNEVACAJSOEIAWAEIZIZNYJWZKQFEXUPITAWYCAJWLRPPOSKQTGAADLVZTSTNDZVKOPSEBLVFZDPSZAKMOTDHSKKWXINAVADXUREAXUVBNEGIQWEZKCTPRWIVULZNQWIXXOGINWJIJEBUKLVAKCFRSLPPOGSLSYYBONRAUWPXXIYCSHCMONXONWIVIRJPDGXZGPSYDJLMVRZTOUKQUNCEVAVATOEOXDPWTSPCBWTGHUEAVKFWTSERYFXUGTSEWSKQIAWFYMELGTTOXKRVJCZMZMKIZIZNKDZVLELSSTZTOTJ"  # Ganti dengan teks asli
key_length = 8  # Ganti dengan panjang kunci yang diestimasi
most_frequent = analyze_most_frequent(ciphertext, key_length)

# Menampilkan hasil
print("Huruf paling sering muncul per kolom:")
print("".join(most_frequent))
```

Output:

```jsx
Huruf paling sering muncul per kolom:
WKMOEEIC
```

1. Mencocokkan huruf paling sering muncul tersebut dengan huruf paling sering muncul dalam kata bahasa inggris, yaitu huruf "E", "T", "A", "O", "N", "I", "S", "R". Berikut kodenya:

```jsx
import string

def decrypt_key(cipher_freq, plain_assumptions):
    alphabet = string.ascii_uppercase
    results = {}
   
    for plain_char in plain_assumptions:
        key = ""  # Untuk menyimpan hasil kunci per asumsi plaintext
        p_index = alphabet.index(plain_char)  # Indeks huruf asumsi plaintext
       
        for c in cipher_freq:
            c_index = alphabet.index(c)  # Indeks huruf ciphertext
            k_index = (c_index - p_index) % 26  # K = (C - P) mod 26
            key += alphabet[k_index]  # Tambahkan huruf ke kunci hasil
       
        results[plain_char] = key
   
    return results

# Input huruf terbanyak di tiap kolom
cipher_freq = ["W", "K", "M", "O", "E", "E", "I", "C"]

# Asumsi huruf plaintext bergantian
plain_assumptions = ["E", "T", "A", "O", "N", "I", "S", "R"]

# Proses dekripsi kunci
keys = decrypt_key(cipher_freq, plain_assumptions)

# Output hasil
for assumption, key in keys.items():
    print(f"Asumsi plaintext '{assumption}': {key}")
```

Didapat output:

```jsx
Asumsi plaintext 'E': SGIKAAEY
Asumsi plaintext 'T': DRTVLLPJ
Asumsi plaintext 'A': WKMOEEIC
Asumsi plaintext 'O': IWYAQQUO
Asumsi plaintext 'N': JXZBRRVP
Asumsi plaintext 'I': OCEGWWAU
Asumsi plaintext 'S': ESUWMMQK
Asumsi plaintext 'R': FTVXNNRL
```

1. Kombinasikan output tersebut di mana panjangnya adalah 8 karakter dengan 8 posisi, dan setiap posisi memiliki 8 kemungkinan huruf. Maka ada 88 = 16 juta kemungkinan. Di mana atu iterasi dekripsi membutuhkan 0.0001 detik maka 16 juta x 0.0001 detik = kira kira 28 menit. Ditambah memori yang digunakan pasti lebih besar.