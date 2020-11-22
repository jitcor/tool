- MessageDigest
```java
MessageDigest md = MessageDigest.getInstance(algorithm);
md.digest(resBytes);
```
- Mac
```java
Mac mac = Mac.getInstance(algorithm);
mac.init(sk);
byte[] result = mac.doFinal(res.getBytes());
```
- cipher
```java
Cipher cipher = Cipher.getInstance(algorithm);
cipher.init(Cipher.DECRYPT_MODE, sks);
cipher.doFinal(parseHexStr2Byte(res))
```
