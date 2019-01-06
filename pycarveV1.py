import sys
import os
import string

dir="./image"

#create "image" directory
if not os.path.exists(dir):
    os.makedirs(dir)



import sys  # for argv etc.

#argv1: binary file name
#argv2: image upfront name i.e. pic1, pic2 ...
try:
    argv1, argv2 = sys.argv
except:
    argv1, argv2 = "8-jpeg-search.dd pic".split()

argv2=dir+"/"+argv2# the images will save dir directory
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
        
        if buff.endswith(jpgHeader):#Header for jpeg carving
            
            buff = jpgHeader # clear buffer
        if buff.endswith(jpgFooter) and buff.startswith(jpgHeader):
            
            if len(buff)>5:#there is data between Header and Footer
                picIndex = picIndex + 1
                with  open(argv2 + str(picIndex) + ".jpg", mode='wb') as fd2:
                    
                    fd2.write(buff)
                    print("pic"+str(picIndex))#show jpeg name
                    
            buff = ""#clear buffer
            

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
print("exit, wrote " + str(picIndex) + " files")#show the total number of images.