#!/usr/bin/python2
# coding: utf-8

import string

class Caesar():
  def translate(self, cipher, offset = None):
    if offset == None:
      for i in xrange(1, len(string.lowercase)):
        print self.translateAlpha(cipher, i)
    else:
      return self.translateAlpha(cipher, offset)

  def translateAlpha(self, cipher, offset):
    text = ""
    for c in cipher:
      if c.islower():
        text += string.lowercase[(string.lowercase.index(c) + offset) % len(string.lowercase)]
      elif c.isupper():
        text += string.uppercase[(string.uppercase.index(c) + offset) % len(string.uppercase)]
      else:
        text += c
    return text
