#!/usr/bin/python
import sys
import base64
import zlib
import subprocess

def main(argv):
    f=open(argv,mode='rb')
    a=f.read()
    f.close()
    decoded=zlib.decompress(a)
    p=subprocess.Popen(['file','-'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    output=p.communicate(input=decoded)[0]
    p=subprocess.Popen(['xxd',],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    xxd=p.communicate(input=decoded)[0]
    print "==========Detected Filetype=========="
    print output
    print 
    print "==============RAW Data==============="
    print decoded
    print
#    print "==============HEX Data==============="
#    print xxd



if __name__ == "__main__":
   main(str(sys.argv[1]))
