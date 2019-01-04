#
# pycarve.py - carve out jpg pictures from dd image
# with simple Header/Footer Carving
# http://www.forensicswiki.org/wiki/Carving
#
# Reading binary file in Python
# http://stackoverflow.com/questions/1035340/reading-binary-file-in-python
#
# Convert string to hex
# http://code.activestate.com/recipes/496969/
#
# Modules (definitions and statements) are imported by the import statement

#!/usr/bin/env python
import sys
import os
import string

dir="./image"

if not os.path.exists(dir):
    os.makedirs(dir)



import sys  # for argv etc.

try:
    argv1, argv2 = sys.argv
except:
    argv1, argv2 = "8-jpeg-search.dd pic".split()

argv2=dir+"/"+argv2
print(argv1)
# open image file in read binary mode
fd1 = open(argv1, mode='rb')
print(fd1)
# # Headers for jpeg carving
jpgHeader = b'\xFF\xD8\xFF'
jpgFooter = b'\xFF\xD9'

# #buffer to read from file
buff = ""
# # number of file and offset are set equal to zero
picIndex = 0
offset = 0

try:
    while True:
        # read file until we find the interesting header of footer

        if buff != jpgHeader and jpgFooter:
            # read one byte of the file
            b = fd1.read(1)
            

            if b:
            # if we have succeded, increase the buffer by one byte
                buff = buff + b
                # aa=3
            else:
                #raise exception
                raise EOFError('End of file reached')
            #increasing offset by one
            offset += 1
            #print offset,
            #print the information on the screen to see the progress
            if offset % 100000 == 0:
                print offset,


        #recovering jpeg file

        # print("---------")
        if buff.endswith(jpgHeader):
            print(jpgHeader.encode("hex") + " Head offset at: " + str(offset)) #hex(offset)
            print len(buff), 'buffer cleared'
            buff = jpgHeader # clear buffer
        if buff.endswith(jpgFooter) and buff.startswith(jpgHeader):
            print(jpgFooter.encode("hex") + " Footer offset at: " + str(offset)), #hex(offset)
            picIndex = picIndex + 1
            with  open(argv2 + str(picIndex) + ".jpg", mode='wb') as fd2:
                print(fd2)
                fd2.write(buff)
                print len(buff), 'bytes\n'
            buff = ""

        # read next byte ready for the inner while
        b = fd1.read(1)
        if b:
        # if we have succeded, increase the buffer by one byte 
            buff = buff+b
            offset +=1
        else:
            #raise exception
            raise EOFError('End of file reached')
        
except Exception as e:
    print e
print("exit, wrote " + str(picIndex) + " files")

#def write_file(filename, chunksize=8192):
