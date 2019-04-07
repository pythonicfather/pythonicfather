import random

# Modulus and Base
p = 43
g = 7

# Random Alice and Bob
A = random.randint(1, 1000)
B = random.randint(1, 1000)

# Public key of Alice and Bob
a = g**A % p
b = g**B % p

# Key computation
Ka = b**A % p
Kb = a**B % p
print(f'p = {p}, g = {g} \nAlice =\t{A}, {a}, {Ka} \nBob =\t{B}, {b}, {Kb} \nSecret Key = {g**(A*B)%p}')
