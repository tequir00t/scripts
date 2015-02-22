#!/usr/bin/python
import sys
import base64
import subprocess

def main(argv):
    string=argv
    if (len(argv) % 4) == 1:
        print 'Invalid base64 string, removing the last char'
        string=string[:len(string)-1]
    if (len(argv) % 4) == 2:
        string=string+'=='
    if (len(argv) % 4) == 3:
        string=string+'='
    if ('-' in string) or ('_' in string):
        string=string.replace('-','/').replace('_','+')
    decoded=base64.b64decode(string)
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
    print "==============HEX Data==============="
    print xxd



if __name__ == "__main__":
   main(str(sys.argv[1]))
