#!/usr/bin/python
import os
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
fold=/tmp/python-dir01
def makemydir(fold):
  try:
    os.makedirs(fold)
  except OSError:
    pass
  os.chdir(fold)

mypath = str(sys.argv)
if not os.path.isdir(mypath):
   os.makedirs(mypath)
