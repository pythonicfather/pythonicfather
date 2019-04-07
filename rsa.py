from random import randint
from math import gcd
import sympy

# RSA Algorithme
def rsa(p,q):
    # Public key generation

    ## n and phi computation
    n = p*q
    phi = (p-1)*(q-1)

    ## e Random number generation
    while True:
        e = randint(1,phi)
        if gcd(e, phi) == 1:
            break

    print(f'Public key : (e = {e}, n = {n})')

    # Private key generation
    ## Compute d
    for d in range(phi):
        if e*d % phi == 1:
            break

    print(f'Private key : (d = {d}, n = {n})')

    return (e, n), (d, n)

# RSA Cipher with public key
def rsa_cipher(message, public_key):
    return message**public_key[0] % public_key[1]

# RSA Decipher with private key
def rsa_decipher(message, private_key):
    return message**private_key[0] % private_key[1]

# Transform a message to blocks
def message_to_blocks(message, blocks_size):
    return [int(str(message)[i:i+blocks_size]) for i in range(0, int(len(str(message))), blocks_size)]

# RSA Cipher blocks generation
def rsa_cipher_blocks(message, blocks_size, public_key):
    return [rsa_cipher(message_block, public_key) for message_block in message_to_blocks(message, blocks_size)]

# RSA Decipher blocks generation
def rsa_decipher_blocks(cipher_message_blocks, private_key):
    return [rsa_decipher(cipher_message_block, private_key) for cipher_message_block in cipher_message_blocks]

def example1():
    # Example 1 : Cipher and Decipher
    rsa(47,71)
    print(rsa_cipher(688, (79, 3337)))
    print(rsa_decipher(1570, (1019, 3337)))

def example2():
    # Example 2 : Cipher blocks
    # Public and private keys
    n = 3337
    e = 79
    d = 1019

    public_key = (e, n)
    private_key = (d, n)

    # The size of the blocks to encrypte < len(str(n))
    blocks_size = 3

    # Message to encrypt
    message = 6882326879666683

    # The encrypted message blocks
    cipher_message_blocks = rsa_cipher_blocks(message, 3, public_key)

    # The decrypted message blocks
    decipher_message_blocks = rsa_decipher_blocks(cipher_message_blocks, private_key)

    # The decrypted message 
    deciphered_message = int("".join(map(str, decipher_message_blocks)))

    print(f'Message = {message}, Encrypted Message Blocks = {cipher_message_blocks}')
    print(f'Encrypted Message Blocks= {cipher_message_blocks}, Decrypted Message = {decipher_message_blocks}')
    print(f'The decrypted message is : {deciphered_message}')

def example3():
    # Example 3 - Exercise
    c = 564648324243696562331689
    public_key = (11, 703)
    private_key = (59, 703)
    deciphered_message = "".join(map(chr, rsa_decipher_blocks(message_to_blocks(c, 3), private_key)))
    print(deciphered_message)

def example4():
    # Digital signatures
    public_key, private_key = (11,703), (59, 703)
    message = "MESSAGE"
    m = int(''.join(map(str, list(map(ord, list(message))))))
    print(m)
    # Ciphered message with private key
    print(rsa_cipher_blocks(m, 2, private_key))
    # Deciphered message with public key
    print(rsa_decipher_blocks(rsa_cipher_blocks(m, 2, private_key), public_key))
    print("".join(list(map(chr, rsa_decipher_blocks(rsa_cipher_blocks(m, 2, private_key), public_key)))))