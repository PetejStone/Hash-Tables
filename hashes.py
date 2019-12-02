import time
import hashlib
import bcrypt

key = b"hello"

print(hashlib.sha256(key).hexdigest())

def djb2(key):
    #start from an arbitray large prime number

    hash_value = 5381

    #bitshift and sum the value of each character

    for character in key:
        hash_value(hash_value.bit << 5 + hash_value) + char
    return hash_value

    print(djb2(key))