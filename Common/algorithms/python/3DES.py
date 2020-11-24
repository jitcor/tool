# 跟java中DESede通用
from Crypto.Cipher import DES3
import base64
text=base64.b64encode(b'1001244624')
pad = DES3.block_size - (len(text) % DES3.block_size)
print(DES3.new(('x'*24).encode('utf-8'), DES3.MODE_ECB).encrypt((text.decode('utf-8') + (chr(pad) * pad)).encode('utf-8')).hex().upper())
