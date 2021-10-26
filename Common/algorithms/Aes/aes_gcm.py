from Crypto.Cipher import AES
import binascii

key = binascii.unhexlify('e629ed98829a893899ddda67f582ede72e2a187dd1ddd5ada54f49cfe2c8675f')
data = binascii.unhexlify('9012a33bfb0a51dec4f96404cdd7300ec6afca1fa0d6679a7c036652d014a38faf909e9c44d08dffac121aa85d48b7256fa74542e2545e27dc070adfc03af26f2a32f50c2c311d5c91ff6de2ca3b4347da70669575c9b198f4')
nonce, tag = data[:12], data[-16:]
cipher = AES.new(key, AES.MODE_GCM, nonce)
print(cipher.decrypt_and_verify(data[12:-16], tag))
# b'I will become what I deserve, Is there anything like freewil?'
