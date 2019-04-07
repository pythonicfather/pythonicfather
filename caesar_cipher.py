# Author : pythonicfather
# Date : 05/04/2019
# Follow @pythonicfather for more

# Generate the alphabet

alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
# >>> ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
#      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Caesar's Cipher 
# Caesar’s cipher : The algorithm is to offset the alphabet and the key 
# is the number of characters to offset it.

def caesar_cipher(plaintext, key):
    return "".join(list(map(lambda c : alphabet[(alphabet.index(c) + key) % len(alphabet)], plaintext)))

# Caesar's Decipher
# We retriese the offset added earlier.

def caesar_decipher(ciphertext, key):
    return "".join(list(map(lambda c : alphabet[(alphabet.index(c) - key) % len(alphabet)], ciphertext)))

def examples():
    print("Ciphertext of 'ABC' : " + "'" + caesar_cipher("ABC", 3) + "'")
    print("Plaintext of 'DEF' : " + "'" + caesar_decipher("DEF", 3) + "'")
    print("Ciphertext of 'SECRET' : " + "'" + caesar_cipher("SECRET", 3) + "'")
    print("Plaintext of 'VHFUHW' : " + "'" + caesar_decipher("VHFUHW", 3) + "'")