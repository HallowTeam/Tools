#!/usr/bin/python2
# coding: utf-8

import string

CHARSET = string.uppercase

class Vigenere():
    def formatText(self, text):
        return text.upper()

    def formatKey(self, key):
        return [c for c in key.upper() if c in CHARSET]

    def encrypt(self, plain, key):
        key    = self.formatKey(key)
        count  = 0
        plain  = self.formatText(plain)
        cipher = ""
        for c in plain:
            if c in CHARSET:
                index   = CHARSET.index(c)
                offset  = CHARSET.index(key[count % len(key)])
                cipher += CHARSET[(index + offset) % len(CHARSET)]
                count  += 1
            else:
                cipher += c
        return cipher

    def decrypt(self, cipher, key):
        key    = self.formatKey(key)
        count  = 0
        plain  = ""
        cipher = self.formatText(cipher)
        for c in cipher:
            if c in CHARSET:
                index   = CHARSET.index(c)
                offset  = CHARSET.index(key[count % len(key)])
                plain  += CHARSET[(index - offset) % len(CHARSET)]
                count  += 1
            else:
                plain  += c
        return plain

    def revert(self, cipher, plain):
        key    = ""
        plain  = self.formatKey(plain)
        cipher = self.formatKey(cipher)
        for a, b in zip(cipher, plain):
            if a in CHARSET:
                index   = CHARSET.index(a)
                offset  = CHARSET.index(b)
                key    += CHARSET[(index - offset) % len(CHARSET)]
        return key
