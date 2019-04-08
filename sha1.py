import hashlib

sha_h = hashlib.new('sha1')
ripemd_h = hashlib.new('ripemd160')

sha_h.update('abc'.encode('utf-8'))
print(h.hexdigest())