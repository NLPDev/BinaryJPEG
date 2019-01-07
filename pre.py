import os
import sys
import glob

from shutil import copyfile

#argv2: the folder to search
try:
    argv1, argv2 = sys.argv
except:
    argv2 = "./"#current script folder

dir="./binary/"#target folder

#create binary directory
if not os.path.exists(dir):
    os.makedirs(dir)

dir2="./image"

#create "image" directory
if not os.path.exists(dir2):
    os.makedirs(dir2)



folder=argv2
files = os.listdir(folder)
for fi in files:
    if '.dd' in fi:#file extension is .dd
        print(fi)
        copyfile(fi, dir+fi)#copy file to dir directory


for binName in glob.glob(argv2+"*.dd"):
	aa=binName
	# print(aa)
	picName=aa.split("/")
	aa=picName[1].split(".")
	picName=aa[0]
	

	argv2=dir2+"/"+picName+"_pic" # the images will save dir directory
	
	# open image file in read binary mode
	fd1 = open(binName, mode='rb')
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