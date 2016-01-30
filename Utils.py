__author__ = 'aneta_ochedowska'

from itertools import izip, cycle
import base64
import hashlib


class Cipher():
    def __init__(self, key):
        self.key = key

    def encrypt(self, m):
        xored = ''.join(chr(ord(x) ^ ord(y))
                        for (x, y) in izip(m, cycle(str(self.key))))
        return base64.encodestring(xored).strip()

    def decrypt(self, c):
        message = base64.decodestring(c)
        xored = ''.join(chr(ord(x) ^ ord(y))
                        for (x, y) in izip(message, cycle(str(self.key))))
        return xored


def hash_function(m):
    m = hashlib.md5(m).hexdigest()
    return m
