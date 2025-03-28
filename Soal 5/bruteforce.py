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
