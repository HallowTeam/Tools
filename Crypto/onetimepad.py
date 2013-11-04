#!/usr/bin/python2
# coding: utf-8

import string

class OneTimePad():

    def encrypt(self, plaintext, key, charset = string.uppercase):
        ciphertext = ""
        for c1, c2 in zip(plaintext, key):
            i1 = charset.index(c1)
            i2 = charset.index(c2)
            ciphertext += charset[(i1 + i2) % len(charset)]
        return ciphertext

    def decrypt(self, ciphertext, key, charset = string.uppercase):
        plaintext = ""
        for c1, c2 in zip(ciphertext, key):
            i1 = charset.index(c1)
            i2 = charset.index(c2)
            plaintext += charset[(i1 - i2) % len(charset)]
        return plaintext