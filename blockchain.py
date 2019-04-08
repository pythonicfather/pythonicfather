import hashlib
from ecdsa import SigningKey
from ecdsa import NIST256p

# Calculating the Bitcoin Adress

def generate_key():
    pri_key = SigningKey.generate(curve=NIST256p)
    pub_key = pri_key.get_verifying_key()
    return pri_key, pub_key 

public_key = generate_key()[1]

public_key = b"MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAESJZDh7MdG7ve7a2Av/QiErYejkiP\n6Krir+AEwtASEF0tKRDYgvDSuSPhGUhZOIXcKojZF6w+hm8DaNWcyUg/JQ=="

sha256_h = hashlib.sha256()
sha256_h.update(public_key)

adress = hashlib.new('ripemd160')
adress.update(sha256_h.digest())

print(f'Bitcoin Adress = {adress.hexdigest()}')