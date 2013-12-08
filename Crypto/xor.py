#!/usr/bin/python2
# coding: utf-8

import string
from termcolor import colored

KEY_CHARSET = set(string.printable) - set(string.whitespace) - set("!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~")
TXT_CHARSET = set(string.printable) - set("\"#$%&*+/<=>@[\\]^`|~")

def split_list(list_, chunksize = 2):
    return [list_[i:i + chunksize] for i in xrange(0, len(list_), chunksize)]

class Xor():
    def xor(self, plain, key):
        cipher = ""
        for i, c in enumerate(plain):
            cipher += chr(ord(c) ^ ord(key[i % len(key)]))
        return cipher

    def force(self, cipher, key_len, key_charset = KEY_CHARSET, txt_charset = TXT_CHARSET, callback = None):
        keys   = []
        chars  = set()
        chunks = split_list(cipher, key_len)
        for i in xrange(key_len):
            ignored = set()
            for c in key_charset:
                charset = set()
                success = True
                for chunk in chunks:
                    if i < len(chunk):
                        char = self.xor(chunk[i], c)
                        if not char in txt_charset:
                            ignored |= set(char)
                            success  = False
                            break
                        charset |= set(char)
                    else:
                        continue
                if success:
                    if callback and not callback(i, c, keys):
                        continue
                    if i == len(keys):
                        keys.append([])
                    keys[i].append(c)
                    chars |= charset
            if len(keys) <= i:
                return False, keys, sorted(chars), sorted(ignored)
        return True, keys, sorted(chars), None

    def format(self, success, keys, chars, ignored):
        if success == True:
            print colored("[+] Success", "green")
            print "[+] Charset:", chars
            print colored("[+] Keys   :", "green"), colored(keys, "yellow")
        else:
            print colored("[-] Failure ", "red"), "at index %d" % len(keys)
            print "[-] Charset:", chars
            print "[-] Keys   :", keys
            print colored("[-] Ignored:", "red"), colored(ignored, "yellow")
        return success, keys, chars, ignored
