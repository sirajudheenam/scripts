#!/usr/bin/python
import os

def makemydir("/tmp/python-created-01"):
  try:
    os.makedirs("/tmp/python-created-01")
  except OSError:
    pass
  os.chdir("/tmp/python-created-01")

mypath = "/tmp/python-created-02"
if not os.path.isdir(mypath):
   os.makedirs(mypath)
