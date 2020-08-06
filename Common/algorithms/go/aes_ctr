//AEC加密和解密（CRT模式）
func aesWithCTR(text []byte, key []byte, iv []byte) ([]byte, error) {
	//指定加密、解密算法为AES，返回一个AES的Block接口对象
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	//指定计数器,长度必须等于block的块尺寸
	count := iv
	//指定分组模式
	blockMode := cipher.NewCTR(block, count)
	//执行加密、解密操作
	message := make([]byte, len(text))
	blockMode.XORKeyStream(message, text)
	//返回明文或密文
	return message, nil
}
