import hashlib

def hash_password(password):
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest
    return hex_dig

print(hash_password("hey"))