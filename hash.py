import hashlib

def hash_password(passOrig):
    salt = "5gz"
    dbPass = passOrig + salt
    password_hashed = hashlib.md5(dbPass.encode())
    return password_hashed