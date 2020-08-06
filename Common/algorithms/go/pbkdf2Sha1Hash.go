func pbkdf2Sha1Hash(password, salt []byte, iter int) []byte {
	return pbkdf2.Key(password, salt, iter, 24, sha1.New)
}
