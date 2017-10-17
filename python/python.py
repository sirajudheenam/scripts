#!/usr/bin/python
import os
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

def makemydir("/tmp/python-created-01"):
  try:
    os.makedirs("/tmp/python-created-01")
  except OSError:
    pass
  os.chdir("/tmp/python-created-01")

mypath = str(sys.argv)
if not os.path.isdir(mypath):
   os.makedirs(mypath)
