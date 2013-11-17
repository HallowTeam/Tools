#!/usr/bin/python2
# coding: utf-8

import string

charset = set(string.printable) - set(string.whitespace) | set(" ")

def split_list(list_, chunksize = 2):
    return [list_[i:i + chunksize] for i in xrange(0, len(list_), chunksize)]

class Xor():
    def xor(self, plaintext, key):
        cipher = ""
        for i, c in enumerate(plaintext):
            cipher += chr(ord(c) ^ ord(key[i % len(key)]))
        return cipher

    def force(self, cipher, key_len, key_charset = charset, cipher_charset = charset, callback = None):
        keys   = []
        chunks = split_list(cipher, key_len)
        for i in xrange(key_len):
            for c in key_charset:
                success = True
                for chunk in chunks:
                    if i < len(chunk) and not self.xor(chunk[i], c) in cipher_charset:
                        success = False
                        break
                if success:
                    if callback and not callback(i, c, keys):
                        continue
                    if i == len(keys):
                        keys.append([])
                    keys[i].append(c)
            if len(keys) <= i:
                print "[-] Nothing found at %d" % i
                print "[-] " + str(keys)
                break
        return keys
