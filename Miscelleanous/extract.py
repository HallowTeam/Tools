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
import string

################################################################################
### Parameters:
################################################################################
##
## - data        : ???
## - alignName   : ???
## - alignSize   : ???
## - extract_beg : ???
## - extract_end : ???
## - extract_all : ???
##
################################################################################
################################################################################

data        =
alignName   = -1
alignSize   = -1
extract_all = [
]
extract_beg = [
]
extract_end = [
]

################################################################################
################################################################################

counter  = 0
fallback = False
original = data
extracts = extract_beg + extract_end + extract_all

if not extracts:
  print "You must extract something..."
  exit(0)

if alignName == -1:
  alignName = max(len(name) for name, length in extracts)
if alignSize == -1:
  alignSize = max(len(str(length)) for name, length in extracts)

if alignName == 0:
  fallback   = True
  alignName = len(str(len(extracts)))

for i, extract in enumerate([extract_beg, extract_end]):
  for name, size in extract:
    extract = data[:size] if i == 0 else data[-size:]
    data    = data[size:] if i == 0 else data[:-size]
    if fallback == True:
      name    = str(counter)
      counter = counter + 1
    print "{:{:d}s} ({:{:d}d}): {:s}".format(name, alignName, size, alignSize, extract)

for name, size in extract_all:
  if fallback == True:
    name    = str(counter)
    counter = counter + 1
  print "{:{:d}s} ({:{:d}d}): {:s}".format(name, alignName, len(data), alignSize, data)
