//reference:https://www.cnblogs.com/akidongzi/p/12036165.html
package cipher

import (
	"bytes"
	"crypto"
	"crypto/cipher"
	"crypto/rand"
	"crypto/rsa"
	"fmt"
	"io"
	"math/big"
)
func doRSAEncrypt(data []byte, N string, E int) ([]byte, error) {
	n := new(big.Int)
	n.SetString(N, 16)
	publicKey := &rsa.PublicKey{
		N: n,
		E: E,
	}
	partLen:=publicKey.N.BitLen()/8-11
	chunks:=split(data,partLen)
	cipherData:=make([]byte,0)
	for _,chunk:=range chunks{
		if cipherText, err := rsa.EncryptPKCS1v15(rand.Reader, publicKey, chunk); err != nil {
			return nil, err
		} else {
			cipherData= append(cipherData, cipherText...)
		}
	}
	return cipherData,nil
}
func split(buf []byte, lim int) [][]byte {
	var chunk []byte
	chunks := make([][]byte, 0, len(buf)/lim+1)
	for len(buf) >= lim {
		chunk, buf = buf[:lim], buf[lim:]
		chunks = append(chunks, chunk)
	}
	if len(buf) > 0 {
		chunks = append(chunks, buf[:len(buf)])
	}
	return chunks
}
