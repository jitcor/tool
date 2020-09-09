# 已有分析
https://www.jianshu.com/p/208200e0c465
# 官方解密实现(c版)
https://github.com/sqlcipher/sqlcipher-tools/blob/master/decrypt.c
# 自己分析
1.先取出第一页头部16字节作为salt \
2.将password与salt进行hmac哈希得到key \
4.取出每一页尾部16字节内容作为每一页的解密iv \
5.分别对每一页执行AES-CBC-256解密 \
6.然后将解密后的数据拼接在一块构成解密后的db文件 \
# 图示分析
第一页解密，其中header即是db文件头部的16个字节的字符串"SQLite format 3\0" ,null即为空的，与解密无关的，也不会对解密后的db数据有什么影响，具体原因应该是数据加解密前后长度是一样的，那自然iv在解密后自然就没用，但为了保持长度不变，就以null填充了，这里的null可以任意字节，也可以清零
图片: ![1](https://github.com/ihbing/tool/raw/master/Common/sql/sqlcipher/data/sqlcipher%E5%8A%A0%E5%AF%86%E6%9C%BA%E5%88%B6%E5%88%86%E6%9E%90-%E5%9B%BE%E4%B8%80.png)
其它页解密，其中salt依然是第一页的salt，而iv则是当前页的
图片: ![2](https://raw.githubusercontent.com/ihbing/tool/master/Common/sql/sqlcipher/data/sqlcipher%E5%8A%A0%E5%AF%86%E6%9C%BA%E5%88%B6%E5%88%86%E6%9E%90-%E5%9B%BE%E4%BA%8C.png)

使用Java代码实现其解密机制
```java
package sqlcipher.tool;

import javax.crypto.*;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.spec.KeySpec;

/*
解密db 文件

 */
public class Decrypt {
    enum HmacAlgorithm{
        SHA1("PBKDF2WithHmacSHA1",20),
        SHA256("PBKDF2WithHmacSHA256",32),
        SHA512("PBKDF2WithHmacSHA512",64);
        String algorithm;
        int outLength;
        int outBinLength;
        HmacAlgorithm(String algorithm,int outLength){
            this.algorithm=algorithm;
            this.outLength=outLength;
            this.outBinLength=this.outLength*8;
        }

        public String getAlgorithm() {
            return algorithm;
        }

        public int getOutLength() {
            return outLength;
        }
        public int getOutBinLength() {
            return outBinLength;
        }
    }

    public static void main(String[] args) {
       if(startDecrypt("msg.db","msg_de.db",1024,64000,HmacAlgorithm.SHA1,"0C207B".toCharArray())){
           System.out.println("解密完毕");
       }
    }

    private static boolean startDecrypt(String inPath,String outPath,int pageSize,int kdfIter,HmacAlgorithm hmacAlgorithm,char[] password) {
        int headerSize = 16;
        int reserveSize;
        int hmacSize=hmacAlgorithm.getOutLength();
        int ivSize=16;
        int blockSize;
        byte[] salt = new byte[headerSize];
        byte[] iv=new byte[ivSize];
        Cipher cipher;
        reserveSize=hmacSize+ivSize;
        cipher=getCipher(password, salt,iv, kdfIter, hmacAlgorithm);
        blockSize=cipher.getBlockSize();
        reserveSize=reserveSize%blockSize==0?reserveSize:((reserveSize/blockSize+1)*blockSize);
        //初始化输入输出流
        try {
            FileInputStream inputStream = new FileInputStream(inPath);
            FileOutputStream outputStream = new FileOutputStream(outPath);
            byte[] pageBuffer = new byte[pageSize];
            byte[] outPageBuffer;
            int len;
            int pageIndex = 0;
            while ((len = inputStream.read(pageBuffer)) > 0) {
                if (len != pageSize) {
                    throw new IllegalArgumentException("read len is not " + pageSize);
                }
                outPageBuffer=new byte[pageSize];
                //若是第一页，先取出salt值
                if (pageIndex == 0) {
                    System.arraycopy(pageBuffer, 0, salt, 0, headerSize);
                    System.arraycopy(pageBuffer,pageSize-reserveSize,iv,0,ivSize);
                    cipher=getCipher(password,salt,iv,kdfIter,hmacAlgorithm);
                    int pageContentSize =pageSize-headerSize-reserveSize;
                    byte[] pageContent =new byte[pageContentSize];
                    System.arraycopy(pageBuffer, headerSize, pageContent, 0, pageContentSize);
                    byte[] dePageContent =cipher.doFinal(pageContent);
                    System.arraycopy("SQLite format 3\0".getBytes(),0,outPageBuffer,0,headerSize);
                    System.arraycopy(dePageContent,0,outPageBuffer,headerSize, pageContentSize);
                }else {
                    //先取出iv
                    System.arraycopy(pageBuffer,pageSize-reserveSize,iv,0,ivSize);
                    cipher=getCipher(password, salt,iv, kdfIter, hmacAlgorithm);
                    byte[] temp=new byte[pageSize-reserveSize];
                    System.arraycopy(pageBuffer,0,temp,0,pageSize-reserveSize);
                    temp= cipher.doFinal(temp);
                    System.arraycopy(temp,0,outPageBuffer,0,pageSize-reserveSize);
                }
                outputStream.write(outPageBuffer);
                outputStream.flush();
                pageIndex++;
            }
            return true;
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (BadPaddingException e) {
            e.printStackTrace();
        } catch (IllegalBlockSizeException e) {
            e.printStackTrace();
        }
        return false;
    }
    //AES-CBC-256
    private static Cipher getCipher(char[] secretKey,byte[] salt,byte[] iv,int kdfIter,HmacAlgorithm hmacAlgorithm){
        try {
            IvParameterSpec ivspec = new IvParameterSpec(iv);
            SecretKeyFactory factory = SecretKeyFactory.getInstance(hmacAlgorithm.getAlgorithm());
            KeySpec spec = new PBEKeySpec(secretKey, salt, kdfIter, 256);
            SecretKey tmp = factory.generateSecret(spec);
            SecretKeySpec secretKeySpec = new SecretKeySpec(tmp.getEncoded(), "AES");
            Cipher cipher = Cipher.getInstance("AES/CBC/NOPADDING");
            cipher.init(Cipher.DECRYPT_MODE, secretKeySpec, ivspec);
            return cipher;
        }catch (Exception e){
            e.printStackTrace();
            throw new IllegalStateException("decrypt err");
        }
    }
}
```
