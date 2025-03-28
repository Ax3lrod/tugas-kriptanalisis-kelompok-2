# README

# Soal 3 : Playfair Cipher

**Waktu Cryptanalisis:**
3 jam

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

### Hasil Analisis

1. Tabel Frekuensi Digram dalam Bahasa Inggris
    
    ![image](https://github.com/user-attachments/assets/2d2c0444-d66a-40f3-8180-b536416ee4f6)
    
    ![image](https://github.com/user-attachments/assets/24e757fc-b790-4c77-ac8b-127772d5106d)
    
2. **Tabel Frekuensi Digram dalam Ciphertext**
    
    ![image](https://github.com/user-attachments/assets/c7dadec5-8c64-4fb0-8fb9-8a89dde8082c)
    
    ![image](https://github.com/user-attachments/assets/157f9e7e-26e1-4a27-8830-04ffbded1356)
    

## Langkah-langkah pemecahan

Untuk memecahkan ciphertext ini, kami menggunakan tool bernama PlayfairCrack yang kami temukan di internet. Berikut link Githubnya: [https://github.com/N8Stewart/PlayfairCrack](https://github.com/N8Stewart/PlayfairCrack)

Berikut adalah script utama dari tool tersebut yang ditulis dalam bahasa C:

```c
/*
 * Written by Nate Stewart
 * Program to crack a playfair cipher using simulated annealing with quadgrams
 * 03/20/16
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <float.h>
#include <math.h>
#include <time.h>

#include "quadgram.h"
#include "playfairCrack.h"

extern float quadgram[];

int main(int argc, char **argv) {

	char key[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	FILE *fin = stdin;

	/*
	 * Get command line arguments. Setup key and input location
	 */
	switch (argc) {
		case 2:
			fin = fopen(argv[1], "r");
			if (fin == NULL) {
				printf("Invalid file: %s. Unable to open for reading.\n", argv[3]);
				return -1;
			}
		case 1:
			if (!removeLetter(key, 'J')) {
				printf("Could not remove letter J from cipher key.\n");
				return -1;
			}
			break;
		case 4:
			fin = fopen(argv[3], "r");
			if (fin == NULL) {
				printf("Invalid file: %s. Unable to open for reading.\n", argv[3]);
				return -1;
			}
		case 3:
			if (strcmp(argv[1], "-r")) {
				printf("Optional parameter '-r' not found. '%s' found instead.\n", argv[1]);
				return -1;
			}
			if(!removeLetter(key, argv[2][0])) {
				printf("Could not remove letter %c from cipher key.\n", argv[2][0]);
				return -1;
			}
			break;
		default:
			printf("Invalid usage. See below for proper usage.\n");
			printf("\t./%s [ -r <character_to_remove> ] [ ciphertext_filepath ]\n", argv[0]);
			return -1;
	}

	/*	
	 * Input cipher and ensure it is valid
	 */
	char *ciphertext, *plaintext;
	int messageLen;
	ciphertext = readCipher(fin, INPUT_STEP_SIZE);
	messageLen = strlen(ciphertext);
	if (validateText(ciphertext, &messageLen) != 0) {
		free(ciphertext);
		return -1;
	}
	ciphertext = realloc(ciphertext, sizeof(*ciphertext) * (messageLen + 1));
	ciphertext[messageLen] = '\0';
	plaintext = calloc(messageLen + 1, sizeof(*plaintext));
	strcpy(plaintext, ciphertext);	
	
	// close the file as long as it is not stdin
	if (fin != stdin)
		fclose(fin);

	// Output relevant information for error checking
	printf("Attempting to crack the following ciphertext with key: %s\n", key);
	printf("%s\n", ciphertext);

	int iter = 0;
	double score = -DBL_MAX, maxScore = -DBL_MAX;
	srand(time(NULL)); // randomize seed
	// Run until max iteration met 
	while (iter < MAX_ITERATIONS) {
		iter++;
		score = simulatedAnnealing(key, ciphertext, plaintext, messageLen);
		if (score > maxScore) {
			maxScore = score;
			decipher(key, ciphertext, plaintext, messageLen);
			printf("\nPossible Plaintext found using key:\n");
			outputKey(key);
			printf("%s\n\n", plaintext);
		}
	}
	
	free(plaintext);
	free(ciphertext);
	return 0;
}

double simulatedAnnealing(char *key, char *ciphertext, char *plaintext, int messageLen) {
	int count, iter;
	float annealStep;
	char newKey[26], oldKey[26];
	double prob, delta, maxScore, score, bestScore;
	
	// Copy over key so we don't screw up our master copy. Decipher ciphertext using key and score it
	strcpy(oldKey,key);
	decipher(oldKey, ciphertext, plaintext, messageLen);
	maxScore = scoreText(plaintext,messageLen);
	bestScore = maxScore;
	iter = 0;

	// For each step, find our best key
	for (annealStep = ANNEALING_TEMP; annealStep >= 0; annealStep -= ANNEALING_STEP_SIZE) {
		for (count = 0; count < MAX_ITERATIONS; count++) { 
			strcpy(newKey, oldKey);
			alterKey(newKey);
			decipher(newKey, ciphertext, plaintext, messageLen);
			score = scoreText(plaintext, messageLen);
			// our difference between our current maxScore and step score
			delta = score - maxScore;
			// We did work in the positive direction (hopefully...)
			if (delta >= 0) {
				maxScore = score;
				strcpy(oldKey, newKey);
			} else if (annealStep > 0) {
				// the work we did is a side-grade 
				prob = exp(delta / annealStep);
				if (prob > 1.0 * rand() / RAND_MAX) {
					maxScore = score;
					strcpy(oldKey, newKey);				
				}
			}
			// This is our best score so far
			if (maxScore > bestScore){
				bestScore = maxScore;
				strcpy(key, oldKey);
				outputStats(iter, bestScore, key);
			} 
			iter++;
		}
	}
	
	return bestScore;
}

void keySwapRows(char *key, int r1, int r2) {
	int i;
	char temp;
	for (i = 0; i < 5; i++) {
		temp = key[r1 * 5 + i];
		key[r1 * 5 + i] = key[r2 * 5 + i];
		key[r2 * 5 + i] = temp;
	}
}

void keySwapCols(char *key, int c1, int c2) {
	int i;
	char temp;
	for (i = 0; i < 5; i++) {
		temp = key[i * 5 + c1];
		key[i * 5 + c1] = key[i * 5 + c2];
		key[i * 5 + c2] = temp;
	}
}

void keySwapChars(char *key, int i1, int i2) {	
	char temp = key[i1];
	key[i1] = key[i2];
	key[i2] = temp;
}

void keyShuffle(char *key, int num) {
	int i;
	for (i = 0; i < num; i++) {
		keySwapChars(key, rand() % 25, rand() % 25);
	}
}

void alterKey(char *key) {
	switch(rand() % 100) {
		case 1:
		case 2:
			keyShuffle(key, rand() % 26);
			break;
		case 3:
		case 4:
		case 5:
		case 6:
			keySwapRows(key, rand() % 5, rand() % 5);
			break;
		case 7:
		case 8:
		case 9:
		case 10:
			keySwapCols(key, rand() % 5, rand() % 5);
		default:
			keySwapChars(key, rand() % 25, rand() % 25);
			break;
	}
}

void decipher(char *key, char *ciphertext, char *plaintext, int len) {
	int i;
	// index, row and column of the current digram
	char c1, c2;
	int c1_ind, c1_row, c1_col, c2_ind, c2_row, c2_col;

	for (i = 0; i < len; i += 2) {
		c1 = ciphertext[i], c2 = ciphertext[i + 1];
		// strchr returns a pointer to the first index of character in key. subtract key from pointer to get index
		c1_ind = (int)(strchr(key, c1) - key), c2_ind = (int)(strchr(key, c2) - key);
		// Rows have offset 5, columns are mod 5
		c1_row = c1_ind / 5, c2_row = c2_ind / 5;
		c1_col = c1_ind % 5, c2_col = c2_ind % 5;

		if (c1_row == c2_row && c1_col == c2_col) { // Same character
			int row = c1_row - 1, col = c1_col - 1;
			if (row < 0)
				row += 5;
			if (col < 0)
				col += 5;
			int ind = 5 * row + col;
			plaintext[i] = ind, plaintext[i + 1] = ind;
		} else if (c1_row == c2_row) { // same row
			// Determine if wrapping occurred
			if (c1_col == 0) {
				plaintext[i] = key[c1_ind + 4];
				plaintext[i+1] = key[c2_ind - 1];
			} else if (c2_col == 0 ) {
				plaintext[i] = key[c1_ind - 1];
				plaintext[i+1] = key[c2_ind + 4];
			} else {
				plaintext[i] = key[c1_ind - 1];
				plaintext[i+1] = key[c2_ind - 1];
			}
		} else if (c1_col == c2_col ) { // same column
			if (c1_row == 0) {
				plaintext[i] = key[c1_ind + 20];
				plaintext[i+1] = key[c2_ind - 5];
			} else if (c2_row == 0) {
				plaintext[i] = key[c1_ind - 5];
				plaintext[i+1] = key[c2_ind + 20];
			} else {
				plaintext[i] = key[c1_ind - 5];
				plaintext[i+1] = key[c2_ind - 5];
			}
		} else { // rectangle rule
			plaintext[i] = key[5 * c1_row + c2_col];
			plaintext[i+1] = key[5 * c2_row + c1_col];
		}
	}
}

void outputKey(char *key) {
	int i;
	for (i = 0; i < 25; i += 5) { 
		printf("%c %c %c %c %c\n", key[i + 0], key[i + 1], key[i + 2], key[i + 3], key[i + 4]);
	}
}

void outputStats(int iteration, double score, char *key) {
	printf("Iteration: %8d, \tbest score: %12.4lf, \tCurrent key: %s\n", iteration, score, key);
}

bool removeLetter(char *cipher, char letter) {
	char *src, *dst;
	if (letter >= 'a' && letter <= 'z') {
		letter -= ' '; // make it capital letter 
	}
	bool found; // if the letter was found or not
	for (src = dst = cipher; *src != '\0'; src++) {
		*dst = *src;
		if (*dst != letter) 
			dst++;
		else
			found = true;
	}
	*dst = '\0';
	return found;
}

char *readCipher(FILE *fin, size_t size) {
	char *str;
	int currChar;
	size_t len = 0;
	str = malloc(sizeof(*str) * size); // Initially allocate str with provided size
	if (!str) return str; // If provided size is 0, or unable to allocate memory, return empty string
	
	while (EOF != (currChar = fgetc(fin)) && currChar != '\n') {
		str[len++] = currChar;
		if (len == size) {
			str = realloc(str, sizeof(*str) * (size += INPUT_STEP_SIZE));
			if (!str) return str; // If unable to realloc, return what we have so far
		}
	}

	// Add null terminator onto end of string
	str = realloc(str, sizeof(*str) * (++len));
	str[len - 1] = '\0';
	return str;
}

double scoreQuadgram(char *text) {
	int index[4];
	char output[5];
	memset(output, '\0', sizeof(output));
	strncpy(output, text, 4);
	// Get a number associated with the index of each character
	index[0] = (*(text + 0) - 'A') * 17576;
	index[1] = (*(text + 1) - 'A') * 676;
	index[2] = (*(text + 2) - 'A') * 26;
	index[3] = (*(text + 3) - 'A') * 1;
	//int totalIndex = index[0] + index[1] + index[2] + index[3];
	//printf("Text: %s | ", output);
	//printf("total Index:%d | 0:%d | 1:%d | 2:%d | 3:%d\n",totalIndex, index[0], index[1], index[2], index[3]);
	return quadgram[index[0] + index[1] + index[2] + index[3]];
}

double scoreText(char *text, int len) {
	int i;
	double score = 0.0;
	// Calculate all quadgrams in the text
	for (i = 0; i < len - 3; i++) {
		score += scoreQuadgram(text + i);
	}

	return score;
}

int validateText(char *input, int *len) {
	int i;
	// Declare an output array and initialize it to all 0's
	char *output = calloc(*len, sizeof(*output));
	int offset = 0;
	// Eliminate spaces and reformat case of text
	for (i = 0; i < *len; i++) {
		// Convert lower case to upper case where applicable
		if (input[i] >= 'a' && input[i] <= 'z') {
			output[i - offset] = input[i] - ' ';
		} else if (input[i] == ' ') {
			offset += 1;
		} else if (input[i] >= 'A' && input[i] <= 'Z') {
			output[i - offset] = input[i];
		} else {
			// Invalid character 
			printf("Invalid character: %c\n", input[i]);
			free(output);
			return -1;
		}
	}
	strcpy(input, output);
	free(output);
	*len -= offset; // Shrink length according to how many spaces were filtered out
	return 0;
}

```

**Output:**

```c
Attempting to crack the following ciphertext with key: ABCDEFGHIKLMNOPQRSTUVWXYZ
DCXQCQAIIUFZGRBIIBTKGSTBWCOIQCDNNGTINEDQSOGKRPENTNPOQMNGTIGVGLBPRSCEMNGZRSXSKGCSMCPNTKBFHRSNVTSXBIQDESNVNSPCRMEQDPMNDXWCCBXREFFVIBKOIGTIDMKFGLWCFEIKFCISLIPSNYNFEWHRKGHQCESUPEKGCKPOIKVGDNOAGNXQCWCQDWBLUIGCRNMKSITVCGIKIMWCKCGZDIIBKOIGFGKCRLGWQNQRISUERNNFKDENUMBIPESHNBCWHMGLPEDCXQNGPCRKCWIVLSSIRPMAIUMNRNGKRPLIDUXDXBCOBIXNNFGNRGOQWCKGTNDNGWQNQRISUEWGBPSGLIDGSASNPNLGIBKOIGFGKRLEDNPOMNFNBNZQCEDIPSEPEDZGRGTINBEFRGITBTRZWCOIQRISPVPSTIDICWGCISERNGPCSKRMQFZRIDNFGLNESQFNDUBRAMKDSRPKGNNFGLNEASIDNEAMEYEGNRPEFQWCEFNFNKNERTGWQNQRISUERNZMCTDISHSNGNNPRGLINFRHDCXQCQAIIUEALRDNOAGNXGIBGLSHNSABFEKFCWQADAGAWCPMLVGKBFUSNGKRNMCWQDRSCEDQSOSKIKSKVGGRCQPEAMIDDWOQNSIKNDXRKFBIIBTKGSBLDNOAGNXQIGTNNXNBRMQFPEIDTVNERQCIHIRMKIMBHIIVAMOQNGPCRMEPQDKFPIHISCXFTNGWQNRPLPFNDUBRKFGKSPOIMWFEMQPCRGOQNBAMMLNGKQNGPCNRUEDIRGGLBFMNGZHGGINRUEDINECGWOOKFENEKFFNDKPEKQGWPKNSNHOPCPSKUESHFNRNNRUEDIIMKSGQSGIDTNGWQNIMSGIRQDNBNYNFIRMANEASZNFXGMZKIDUSNATIDGFPPHTNZGKITVRGLVWCFEGEEGKOCKZDSNPNCYSRPCNDDWLIREDIFESRGAENEGKRTKRHZSTNBPPELQWO
Iteration:        1,    best score:   -6665.0902,       Current key: ABCDEFOHIKLMNGPQRSTUVWXYZ
Iteration:        2,    best score:   -6626.9422,       Current key: ABCDEFOHIKLMNGPQUSTRVWXYZ
Iteration:        6,    best score:   -6605.6138,       Current key: ABNDEFOHIKLMCGPQUSTRVWXYZ
Iteration:        7,    best score:   -6576.6888,       Current key: ABNHEFODIKLMCGPQUSTRVWXYZ
Iteration:       13,    best score:   -6571.7555,       Current key: ANGEXFODHBLMCKPQUSTRVWIYZ
Iteration:       15,    best score:   -6566.3704,       Current key: ANGEXFODHBLMCKPQUSTRYWIVZ
Iteration:       16,    best score:   -6563.8960,       Current key: ANGEZFODHBLMCKPQUSTRYWIVX
Iteration:       18,    best score:   -6529.7266,       Current key: ANGEIFODHBLMCKPQUSTRYWZVX
Iteration:       23,    best score:   -6525.1015,       Current key: ANGEIPODHBLMCKFQUSTRYWZVX
Iteration:      111,    best score:   -6478.9820,       Current key: CSPDTMWRHGAQNIEYZFBKXULOV
Iteration:      192,    best score:   -6432.1360,       Current key: TVBURQWYGSPMZFCAKXOLDNHIE
Iteration:     1192,    best score:   -6409.4917,       Current key: ZTKOCFXRWYMPEBVUQISGDANLH
Iteration:     1200,    best score:   -6405.7390,       Current key: ZTVOCFGRWYSPEBKUQIHXDANLM
Iteration:     1206,    best score:   -6380.6415,       Current key: ZXVYCFPRWOSBEGKUQIHTDANLM
Iteration:     2513,    best score:   -6341.0187,       Current key: UHTNLDKAEFQVMBCYZPGORXWIS
Iteration:     2518,    best score:   -6339.3909,       Current key: UHTNCDKAEFQVYBLMZPGORXWIS
Iteration:     5216,    best score:   -6317.8017,       Current key: FYSWHRGINOBVCPAMKEDQULTXZ
Iteration:    25755,    best score:   -6310.8811,       Current key: UGREQZPFMYHOBDXAILNVKSCTW
Iteration:    25756,    best score:   -6241.5805,       Current key: UGREQZPMFYHOBDXAILNVKSCTW
Iteration:    66718,    best score:   -6239.1901,       Current key: SRENIGDPTAYHCWKVMQXZBLFOU
Iteration:   105023,    best score:   -6221.9460,       Current key: IXOSGRUDWHAPMKFNVCLTEYZBQ
Iteration:   105047,    best score:   -6213.3871,       Current key: IXOSGQCMKYAFUDPNVZLTEHWBR
Iteration:   105056,    best score:   -6171.6072,       Current key: CQXKYIMOSGAFUDPNVZLTEHWBR
Iteration:   105066,    best score:   -6146.2411,       Current key: CQXKYIMOSGAFZDPNVULTEHWBR
Iteration:   520353,    best score:   -6144.6883,       Current key: OCNTZKMEDVWYPHXSRIGLBQAFU
Iteration:   520892,    best score:   -6125.6628,       Current key: BVUXZFCOHYMSEPQTLNKWIRGAD
Iteration:   584162,    best score:   -6110.5072,       Current key: HPXFLKZYWVDBMAUSRTNIGOQEC
Iteration:   584402,    best score:   -6104.4496,       Current key: HPXFZKLYCVMBDAUSRTNIGOQEW
Iteration:   584446,    best score:   -6079.1816,       Current key: HPXFZKLYCMVBDAUSRTNIGOQEW
Iteration:   595131,    best score:   -6069.5997,       Current key: PZWXYFCBVOGURAITKLMNSHDQE
Iteration:   595333,    best score:   -6042.9196,       Current key: YZPVXFHOBWGUIRATKNLSMCEDQ
Iteration:   598755,    best score:   -5996.7446,       Current key: ASRIGKTCNHYMDEFVZOPQLBWUX
Iteration:   598758,    best score:   -5950.1264,       Current key: ASRIGKLCNHYMDEFVZOPQTBWUX
Iteration:   598766,    best score:   -5935.9932,       Current key: ASRIGKLCNHUMDEFVZOPQTBWYX
Iteration:   598790,    best score:   -5932.5017,       Current key: ASRIGKLCNHUMDEFXZOPQTBWYV
Iteration:   598821,    best score:   -5574.9616,       Current key: ASRIGKLCNTUMDEFXZOPQHBWYV
Iteration:   598822,    best score:   -5542.3003,       Current key: ASRIGKLCNTUMDEFXYOPQHBWZV
Iteration:   598830,    best score:   -5534.8592,       Current key: ASRIGKLCNTUMDEFXBOPQHYWZV
Iteration:   598879,    best score:   -5428.7424,       Current key: ASRIGKLCNTUMDEFXBOPQHVWZY
Iteration:   598890,    best score:   -5287.7529,       Current key: ASRIGKLCNTUMDEFHBOPQXVWZY
Iteration:   598907,    best score:   -5054.2634,       Current key: ASRIGKLCNTUBDEFHMOPQXVWZY
Iteration:   599468,    best score:   -4689.4526,       Current key: ASRIGKLCNTHBDEFUMOPQXVWZY
Iteration:   599514,    best score:   -4555.6473,       Current key: ASRIGKLCNTHBDEFUMOPQZVWXY

Possible Plaintext found using key:
A S R I G
K L C N T
H B D E F
U M O P Q
Z V W X Y
CRYPTOGRAPHYISESSENTIALFORPROTECTINGINFORMATIONINCOMPUTINGSYSTEMSANDPLAYSAVITALROLEINTHEDAILYLIVESOFBILXLIONSOFPEOPLEWORLDWIDEBYSECURINGBOTHSTOREDANDTRANSMITXTEDXDATAFUNDAMENTALTOMANYSECURITYPROTOCOLSPARTICULARLYTRANSPORTLAYERSECURITYTLSCRYPTOGRAPHICTECHNIQUESENABLEROBUSTENCRYPTIONACROSXSVARIOUSAPPLICATIONSHOWEVERDESPITEITSIMPORTANCECRYPTOGRAPHYREMAINSFRAGILEITSSECURITYCANBECOMPLETELYUNDERMINEDBYASINGLEDESIGNFLAWORPROGRAMXMINGERRORTRADITIONALSOFTWARETESTINGMETHODSSUCHASUNITTESTINGAREINSUFXFICIENTFORDETECTINGCRYPTOGRAPHICVULNERABILITIESINSTEADCRYPTOGRAPHICSECURITYISESTABLISHEDTHROUGHRIGOROUSMATHEMATICALPROOFSANDFORMALANALYSISTOENSURECOMPLIANCEWITHESSENTIALSECURITYPRINCIPLESOFTENRELYINGONREASONABLEASXSUMPTIONSONEOFTHEXEARLYENCRYPTIONMETHODSTHATIMPROVEDUPONSIMPLESUBSTITUTIONCIPHERSISTHEPLAYFAIRCIPHERINTRODUCEDINTHETHCENTURYUNLIKEMONOALPHABETICCIPHERSPLAYFAIRENCRYPTSPAIRSOFLETXTERSUSINGAXKEYSQUAREMAKINGFREQUENCYANALYSISMOREDIFFICULTWHILEITWASONCECONSIDEREDASIGNIFICANTADVANCEMENTMOD
```

**Plaintext:**

> Cryptography is essential for protecting information in computing systems and plays a vital role in the daily lives of billions of people worldwide by securing both stored and transmitted data. It is fundamental to many security protocols, particularly Transport Layer Security (TLS). Cryptographic techniques enable robust encryption across various applications. However, despite its importance, cryptography remains fragile; its security can be completely undermined by a single design flaw or programming error. Traditional software testing methods, such as unit testing, are insufficient for detecting cryptographic vulnerabilities. Instead, cryptographic security is established through rigorous mathematical proofs and formal analysis to ensure compliance with essential security principles, often relying on reasonable assumptions on one of the early encryption methods that improved upon simple substitution ciphers. The Playfair cipher, introduced in the 18th century, unlike monoalphabetic ciphers, encrypts pairs of letters using a key square, making frequency analysis more difficult while it was once considered a significant advancement. MOD
> 

### 1. Alur Utama Program

- **Input dan Persiapan:**
    - Program membaca argumen command line untuk menentukan file input ciphertext dan optional parameter untuk menghilangkan karakter tertentu (misalnya 'J') dari kunci.
    - Kunci awal diset ke string `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"`. Kemudian, dengan memanggil fungsi `removeLetter`, program menghapus huruf tertentu (misalnya 'J') agar sesuai dengan aturan Playfair (biasanya menggunakan matriks 5x5 yang tidak memuat satu huruf).
    - Ciphertext dibaca dari file (atau stdin) dengan fungsi `readCipher` dan kemudian divalidasi oleh fungsi `validateText` untuk memastikan hanya karakter huruf (A-Z) yang ada.
- **Inisialisasi:**
    - Setelah input valid, ciphertext dan plaintext disiapkan dalam buffer. Plaintext diinisialisasi dengan salinan ciphertext untuk proses dekripsi.
    - Program mencetak informasi awal, seperti kunci yang digunakan dan ciphertext.
- **Simulated Annealing:**
    - Di dalam loop utama, program menjalankan algoritma simulated annealing hingga mencapai batas iterasi yang telah ditentukan (`MAX_ITERATIONS`).
    - Setiap iterasi memanggil fungsi `simulatedAnnealing` yang:
        - **Dekripsi dan Scoring:** Menggunakan fungsi `decipher` untuk mendekripsi ciphertext berdasarkan kunci saat ini, lalu menilai kualitas dekripsi dengan fungsi `scoreText`. Fungsi ini menghitung skor berdasarkan nilai quadgram dari teks, di mana quadgram yang lebih umum (menurut statistik bahasa Inggris) menghasilkan skor yang lebih tinggi.
        - **Key Alteration:** Fungsi `alterKey` mengubah kunci dengan beberapa metode acak (swap baris, swap kolom, swap karakter, atau pengacakan seluruh kunci) untuk mendapatkan variasi kunci baru.
        - **Probabilistik Penerimaan:** Jika perubahan kunci menghasilkan peningkatan skor (delta positif), kunci baru diterima. Jika skor menurun, masih ada peluang diterima berdasarkan fungsi probabilitas exp(Δ/T) di mana T adalah temperatur yang menurun secara bertahap (simulasi pendinginan/annealing).
        - **Output dan Penyimpanan:** Jika ditemukan kunci dengan skor terbaik yang lebih tinggi dari sebelumnya, kunci dan plaintext hasil dekripsi tersebut ditampilkan serta dicatat sebagai solusi terbaik.
- **Akhir Program:**
    - Setelah mencapai batas iterasi, program mengeluarkan plaintext terbaik yang ditemukan dan membersihkan alokasi memori sebelum keluar.

### 2. Komponen Utama dan Fungsinya

- **Fungsi `removeLetter`:**
    - Menghapus karakter tertentu dari string kunci sehingga hanya tersisa 25 huruf (sesuai dengan Playfair yang menggabungkan dua huruf, misalnya I/J).
- **Fungsi `readCipher` dan `validateText`:**
    - `readCipher` membaca ciphertext dari file atau stdin, sementara `validateText` memastikan hanya karakter valid (A–Z) yang diikutsertakan, menghilangkan spasi dan mengkonversi huruf kecil ke huruf kapital.
- **Fungsi `decipher`:**
    - Menerapkan aturan dekripsi Playfair. Ciphertext diproses dalam bentuk digram (dua huruf) dan diterapkan aturan: jika huruf berada pada baris yang sama, kolom digeser; jika berada pada kolom yang sama, baris digeser; jika berbeda, digunakan aturan persegi panjang (rectangle rule) untuk mengambil huruf dari posisi silang.
- **Fungsi `scoreQuadgram` dan `scoreText`:**
    - Menggunakan data quadgram (kelompok empat huruf) yang disimpan dalam array `quadgram` untuk memberikan skor probabilistik pada teks. Quadgram yang sering muncul dalam bahasa Inggris akan memiliki skor yang lebih tinggi.
    - Fungsi `scoreText` menjumlahkan skor untuk setiap quadgram dalam teks, sehingga skor total mencerminkan seberapa "alami" teks tersebut.
- **Fungsi `alterKey`:**
    - Secara acak memodifikasi kunci dengan beberapa metode:
        - **Shuffle Key:** Mengacak seluruh kunci.
        - **Swap Baris/Swap Kolom:** Menukar baris atau kolom pada matriks 5x5.
        - **Swap Karakter:** Menukar dua huruf di kunci.
    - Pemilihan metode dilakukan berdasarkan nilai acak untuk menjaga variasi perubahan dan menghindari terjebak pada solusi lokal.
- **Fungsi `simulatedAnnealing`:**
    - Merupakan inti dari algoritma pencarian. Fungsi ini mengulangi proses:
        1. Menghasilkan kunci baru dari kunci saat ini.
        2. Mendekripsi ciphertext dengan kunci tersebut dan menghitung skor dekripsi.
        3. Memutuskan apakah akan menerima kunci baru berdasarkan peningkatan skor atau dengan probabilitas tertentu jika skor menurun, bergantung pada temperatur (annealStep) yang menurun secara bertahap.
    - Proses ini membantu algoritma untuk "melompat" keluar dari minimum lokal dan mencari solusi global yang lebih baik.
- **Output dan Statistik:**
    - Setiap kali ditemukan peningkatan skor, fungsi `outputStats` mencetak iterasi saat ini, skor terbaik, dan kunci saat ini. Ini memberikan gambaran progresif terhadap perbaikan solusi.

### 3. Analisis Performa dan Metode

- **Efisiensi Simulated Annealing:**
    - Algoritma simulated annealing efektif untuk masalah optimisasi dengan ruang solusi yang besar dan non-linear seperti cracking Playfair Cipher. Dengan mengijinkan penerimaan solusi yang kurang baik (dengan probabilitas tertentu), algoritma ini dapat menghindari terjebak pada minimum lokal.
    - Dalam script ini, penggunaan quadgram sebagai metric scoring sangat membantu karena memberikan ukuran seberapa natural teks dekripsi tersebut berdasarkan distribusi n-gram bahasa Inggris.
- **Waktu Eksekusi:**
    - Berdasarkan pengalaman penggunaan, program ini memerlukan waktu sekitar 2 menit untuk menemukan plaintext yang mendekati solusi yang benar. Waktu tersebut bergantung pada jumlah iterasi maksimum (`MAX_ITERATIONS`), ukuran ciphertext, dan parameter annealing (temperatur awal, penurunan temperatur, dan jumlah iterasi per temperatur).
    - Kecepatan juga dipengaruhi oleh seberapa cepat fungsi `decipher` dan `scoreText` berjalan, karena kedua fungsi tersebut dipanggil berkali-kali selama iterasi simulated annealing.
- **Keunggulan dan Keterbatasan:**
    - **Keunggulan:**
        - **Kemampuan Mencari Global Optimum:** Dengan metode probabilistik, algoritma dapat melampaui solusi lokal.
        - **Penggunaan Quadgram:** Memberikan pengukuran yang realistis atas “kecocokan” dekripsi dengan bahasa alami.
    - **Keterbatasan:**
        - **Parameter Tuning:** Keberhasilan algoritma sangat bergantung pada pemilihan parameter (temperatur, step size, dan jumlah iterasi).
        - **Waktu Eksekusi:** Meskipun 2 menit cukup untuk kasus tertentu, ciphertext yang lebih panjang atau parameter yang kurang optimal dapat menyebabkan waktu eksekusi yang lebih lama.

### Kesimpulan

Script ini mengimplementasikan algoritma *simulated annealing* untuk memecahkan Playfair Cipher dengan pendekatan berbasis optimisasi probabilistik. Dengan memanfaatkan scoring quadgram, program dapat mengevaluasi kualitas dekripsi berdasarkan frekuensi kemunculan pola-pola empat huruf yang umum dalam bahasa Inggris. Meskipun metode ini membutuhkan waktu iterasi yang cukup banyak (misalnya, 2 menit dalam kasus tertentu), pendekatan ini sangat efektif untuk menemukan solusi optimal dalam ruang kunci yang sangat besar dan kompleks. Analisis ini menggarisbawahi pentingnya pemilihan parameter dan metode acak dalam mencapai solusi terbaik dalam permasalahan kriptanalisis semacam ini.
