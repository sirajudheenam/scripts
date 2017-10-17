#!/usr/bin/python
import os, sys, getopt
def main(argv):
   folder = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
   except getopt.GetoptError:
      print 'python.py -i <folder>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <folder>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         folder = arg
            os.makedirs(folder)

if __name__ == "__main__":
   main(sys.argv[1:])
