import base64
import hashlib
import hmac
import random
try:
    import crypt
except ImportError:
    crypt = None


class BasePasswordHash(object):
    def __init__(self):
        self._algorithm = None
        self._chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def get_random_string(self, length=12):
        """
        返回一个随机字符串
        """
        return ''.join(random.choice(self._chars) for _ in range(length))

    def salt(self):
        """
        生成在ASCII码范围内的随机字符串salt
        """
        return self.get_random_string()

    def encode(self, password):
        raise NotImplemented('子类必须实现encode方法')

    def verify(self, password, encoded):
        raise NotImplemented('子类必须实现verify方法')


class PBKDF2SHA256Hash(BasePasswordHash):
    """
    使用PBKDF2算法加密密码，hash使用SHA256(推荐)
    结果是64字节的二进制字符串。
    """
    algorithm = "pbkdf2_sha256"
    iterations = 36000
    digest = hashlib.sha256

    def encode(self, password, salt=None, iterations=None):
        if salt is None:
            salt = self.salt()
        assert password is not None
        assert salt and '$' not in salt
        if not iterations:
            iterations = self.iterations
        dklen = None
        hash_value = hashlib.pbkdf2_hmac(
            self.digest().name, password.encode('utf-8'), salt.encode('utf-8'), iterations, dklen)
        hash_value = base64.b64encode(hash_value).decode('ascii').strip()
        return "%s$%d$%s$%s" % (self.algorithm, iterations, salt, hash_value)

    def verify(self, password, encoded):
        algorithm, iterations, salt, hash_value = encoded.split('$', 3)
        assert algorithm == self.algorithm
        encoded_2 = self.encode(password, salt, int(iterations))
        return hmac.compare_digest(encoded, encoded_2)


class PBKDF2SHA1Hash(PBKDF2SHA256Hash):
    """
    使用PBKDF2算法加密密码，hash使用SHA1。
    """
    algorithm = "pbkdf2_sha1"
    digest = hashlib.sha1


class SHA1Hash(BasePasswordHash):
    """
    使用SHA1算法加密密码(不推荐)
    """
    algorithm = "sha1"

    def encode(self, password, salt=None):
        if salt is None:
            salt = self.salt()
        assert password is not None
        assert salt and '$' not in salt
        hash_value = hashlib.sha1((salt + password).encode('utf-8')).hexdigest()
        return "%s$%s$%s" % (self.algorithm, salt, hash_value)

    def verify(self, password, encoded):
        algorithm, salt, hash_value = encoded.split('$', 2)
        assert algorithm == self.algorithm
        encoded_2 = self.encode(password, salt)
        return hmac.compare_digest(encoded, encoded_2)


class MD5Hash(BasePasswordHash):
    """
    使用加salt的MD5加密算法(不推荐)
    """
    algorithm = "md5"

    def encode(self, password, salt=None):
        if salt is None:
            salt = self.salt()
        assert password is not None
        assert salt and '$' not in salt
        hash_value = hashlib.md5((salt + password).encode('utf-8')).hexdigest()
        return "%s$%s$%s" % (self.algorithm, salt, hash_value)

    def verify(self, password, encoded):
        algorithm, salt, hash_value = encoded.split('$', 2)
        assert algorithm == self.algorithm
        encoded_2 = self.encode(password, salt)
        return hmac.compare_digest(encoded, encoded_2)


class CryptHash(BasePasswordHash):
    """
    使用UNIX下的crypt加密密码(不推荐)
    crypt模块不是所有平台都支持，只有unix平台能使用。
    """
    algorithm = "crypt"

    def salt(self):
        return self.get_random_string(2)

    def encode(self, password, salt=None):
        if salt is None:
            salt = self.salt()
        assert len(salt) == 2
        data = crypt.crypt(password, salt)
        assert data is not None
        return "%s$%s$%s" % (self.algorithm, '', data)

    def verify(self, password, encoded):
        algorithm, salt, data = encoded.split('$', 2)
        assert algorithm == self.algorithm
        return hmac.compare_digest(data, crypt.crypt(password, data))


def make_password(password, hasher='PBKDF2SHA256Hash'):
    """
    密码加密
    :param password: 原密码字符串
    :param hasher: 加密方式
    :return: 加密后的字符串
    """
    hashers = ['PBKDF2SHA256Hash', 'PBKDF2SHA1Hash', 'SHA1Hash', 'MD5Hash', 'CryptHash']
    assert hasher in hashers
    assert password is not None
    assert type(password) == str
    if hasher == 'PBKDF2SHA1Hash':
        hash_ = PBKDF2SHA1Hash()
    elif hasher == 'SHA1Hash':
        hash_ = SHA1Hash()
    elif hasher == 'MD5Hash':
        hash_ = MD5Hash()
    elif hasher == 'CryptHash':
        if crypt is not None:
            hash_ = CryptHash()
        else:
            raise ImportError('你的平台不支持crypt')
    else:
        hash_ = PBKDF2SHA256Hash()
    return hash_.encode(password)


def check_password(password, encoded, hasher='PBKDF2SHA256Hash'):
    """
    校验密码
    :param password: 原密码字符串
    :param encoded: 加密后的字符串
    :param hasher: 验证的加密方式
    :return: 验证是否正确
    """
    hashers = ['PBKDF2SHA256Hash', 'PBKDF2SHA1Hash', 'SHA1Hash', 'MD5Hash', 'CryptHash']
    assert hasher in hashers
    assert password is not None
    assert type(password) == str
    if hasher == 'PBKDF2SHA1Hash':
        hash_ = PBKDF2SHA1Hash()
    elif hasher == 'SHA1Hash':
        hash_ = SHA1Hash()
    elif hasher == 'MD5Hash':
        hash_ = MD5Hash()
    elif hasher == 'CryptHash':
        if crypt is not None:
            hash_ = CryptHash()
        else:
            raise ImportError('你的平台不支持crypt')
    else:
        hash_ = PBKDF2SHA256Hash()
    return hash_.verify(password, encoded)

