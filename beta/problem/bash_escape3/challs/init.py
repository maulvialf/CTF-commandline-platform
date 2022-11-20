#!/usr/bin/env python
import sys
import os
class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

nama = raw_input("Input something: ")
blacklist = [" ", "cat", "hd", "|", "find", "grep", "strings", "nano"]
for i in blacklist:
    if(i in nama):
        print "Forbidden string. You input this character '%s'" % i
        sys.exit(0)


cmd = 'echo "Hallo ' + nama + '";'
print 'Menjalankan perintah system("' + cmd + '")'
os.system(cmd)


