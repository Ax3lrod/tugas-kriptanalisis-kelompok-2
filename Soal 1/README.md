# Soal 1 : Monoalphabetic Cipher

## Ciphertext:

<aside>
🔑

LAHYCXPAJYQHRBJWRWMRBYNWBJKUNCXXUOXAYAXCNLCRWPRWOXAVJCRXWRWLXVYDCRWPBHBCNVBRCRBDBNMNENAHFQNANKHKRUURXWBXOYNXYUNFXAUMFRMNXWJMJRUHKJBRBBNLDARWPKXCQMJCJJCANBCJWMMJCJRWVXCRXWLAHYCXPAJYQRLBHBCNVBJANODWMJVNWCJUCXBCJWMJAMYAXCXLXUBVXBCWXCJKUHCQNCAJWBYXACUJHNABNLDARCHCUBYAXCXLXUFQRLQNWJKUNBBCAXWPNWLAHYCRXWJLAXBBJFRMNAJWPNXOJYYURLJCRXWBMNBYRCNRCBRVYXACJWLNLAHYCXPAJYQHRBRWQNANWCUHOAJPRUNNENWCQNVXBCBNLDANLAHYCXPAJYQRLBHBCNVLJWKNANWMNANMLXVYUNCNUHRWBNLDANKHJBRWPUNBYNLRORLJCRXWOUJFXAYAXPAJVVRWPNAAXACAJMRCRXWJUBXOCFJANCNBCRWPVNCQXMBBDLQJBDWRCCNBCRWPJANRWBDOORLRNWCCXDWLXENABNLDARCHEDUWNAJKRURCRNBRWLAHYCXBHBCNVBRWBCNJMLAHYCXPAJYQRLBNLDARCHRBNBCJKURBQNMCQAXDPQVJCQNVJCRLJUVXMNURWPJWMARPXAXDBYAXXOBMNVXWBCAJCRWPCQJCJBHBCNVVNNCBCQNWNLNBBJAHBNLDARCHYAXYNACRNBCQNBNJAPDVNWCBXOCNWANUHXWYUJDBRKUNJBBDVYCRXWBCXEJURMJCNCQNRALUJRVBXWNXOCQNNJAURNBCJWMBRVYUNBCLAHYCXPAJYQRLCNLQWRZDNBRBCQNLJNBJALRYQNAFQRLQMJCNBKJLTCXJAXDWMKLCQRBVNCQXMNWLXMNBYUJRWCNGCKHBQROCRWPNJLQUNCCNAXOCQNJUYQJKNCKHJORGNMWDVKNAXOYXBRCRXWBFQRUNCQRBJYYAXJLQFJBNOONLCRENJCCQNCRVNMDNCXCQNXKBLDARCHXOCQNVNCQXMRCYAXERMNBWXANJUBNLDARCHCXMJHBRWLNCQNANJANXWUHYXBBRKUNBQROCBCQNLRYQNALJWKNNJBRUHKAXTNWCQAXDPQKADCNOXALNMNBYRCNRCBBRVYURLRCHCQNLJNBJALRYQNAANVJRWBXWNXOCQNVXBCFRMNUHANLXPWRINMNWLAHYCRXWCNLQWRZDNBQXFNENARCXOONABWXANJUYAXCNLCRXWJBRCLJWKNZDRLTUHMNLRYQNANMKHQJWMJMMRCRXWJUUHRCBLRYQNACNGCRBNJBRUHRMNWCRORJKUNKNLJDBNCQNOANZDNWLHMRBCARKDCRXWXOUNCCNABVRAAXABCQJCXOCQNNWPURBQUJWPDJPNCQRBQRPQURPQCBJTNHYARWLRYUNRWVXMNAWLAHYCXPAJYQHCADNBNLDARCHANURNBWXCXWUHXWBNLANLHKDCJUBXXWBCAXWPVJCQNVJCRLJUOXDWMJCRXWBJWMLXVYDCJCRXWJURWONJBRKRURCH

</aside>

## Langkah Penyelesaian
### 1. Menghitung Frekuensi Kemunculan Huruf
Disini kami menggunakan tools https://www.dcode.fr/frequency-analysis untuk menghitung frekuensi kemunculan huruf. Hasil dari tools tersebut sebagai berikut:
| Huruf | Jumlah | Frekuensi (%) |
|-------|--------|----------------|
| N     | 179    | 11.38%         |
| C     | 155    | 9.85%          |
| R     | 139    | 8.84%          |
| B     | 120    | 7.63%          |
| X     | 111    | 7.06%          |
| A     | 109    | 6.93%          |
| J     | 108    | 6.87%          |
| W     | 97     | 6.17%          |
| L     | 73     | 4.64%          |
| Q     | 66     | 4.20%          |
| U     | 61     | 3.88%          |
| Y     | 56     | 3.56%          |
| H     | 51     | 3.24%          |
| M     | 46     | 2.92%          |
| D     | 39     | 2.48%          |
| V     | 37     | 2.35%          |
| P     | 32     | 2.03%          |
| O     | 32     | 2.03%          |
| K     | 30     | 1.91%          |
| F     | 12     | 0.76%          |
| E     | 8      | 0.51%          |
| Z     | 4      | 0.25%          |
| T     | 4      | 0.25%          |
| G     | 3      | 0.19%          |
| I     | 1      | 0.06%          |

### 2. Subtitusi Monoalphabetic
Kami menggunakan toold https://quipqiup.com/ untuk melakukan subtitusi monooalphabetic berdasarkan analisis frekuensi kemunculan huruf yang sudah dilakukan sebelumnya, dan didapatkan hasil se[erti berikut:

<aside>

cryptography is an indispensable tool for protecting information in computing systems it is used everywhere by billions of people worldwide on a daily basis securing both data at rest and data in motion cryptographic systems are fundamental to standard protocols most notably the transport layer security tls protocol which enables strong encryption across a wide range of applications despite its importance cryptography is inherently fragile even the most secure cryptographic system can be rendered completely insecure by a single specification flaw or programming error traditional software testing methods such as unit testing are insufficient to uncover security vulnerabilities in cryptosystems instead cryptographic security is established through mathematical modeling and rigorous proofs demonstrating that a system meets the necessary security properties these arguments often rely on plausible assumptions to validate their claims one of the earliest and simplest cryptographic techniques is the caesar cipher which dates back to around bc this method encodes plain text by shifting each letter of the alphabet by a fixed number of positions while this approach was effective at the time due to the obscurity of the method it provides no real security today since there are only possible shifts the cipher can be easily broken through brute force despite its simplicity the caesar cipher remains one of the most widely recognized encryption techniques however it offers no real protection as it can be quickly deciphered by hand additionally its ciphertext is easily identifiable because the frequency distribution of letters mirrors that of the english language this highlights a key principle in modern cryptography true security relies not only on secrecy but also on strong mathematical foundations and computational in feasibility

</aside>
