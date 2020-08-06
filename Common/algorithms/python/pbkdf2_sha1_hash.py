 hash = hashlib.pbkdf2_hmac("sha1", pwd.encode('utf-8'), hashSalt, 5000, 24)
