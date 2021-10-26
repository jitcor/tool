import scrypt

key=scrypt.hash("hl123456",bytes.fromhex("01ba9be2247654b80f296680343d7953"),131072,8,1,32)
print(key)
