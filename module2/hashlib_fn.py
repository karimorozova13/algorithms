import hashlib

data = 'Kari'
hashed_data = hashlib.sha256(data.encode())

print(hashed_data.hexdigest())