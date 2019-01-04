# -*- coding: utf-8 -*-
import re
import os

dir="./image"

if not os.path.exists(dir):
	os.makedirs(dir)


jpg_header = b'\xFF\xD8\xFF'
jpg_footer = b'\xFF\xD9'


file_obj = open('8-jpeg-search.dd','rb')
data = file_obj.read()

print(type(data))
file_obj.close()

SOF_list=[match.start() for match in re.finditer(re.escape(jpg_header),data)]
EOF_list=[match.start() for match in re.finditer(re.escape(jpg_footer),data)]

print(SOF_list)
print(EOF_list)

for i in SOF_list:
	for j in EOF_list:
		img = data[i:j]
		if img:
			name = 'img_{}_{}.jpg'.format(i, j)
			name=dir+"/"+name
			with open(name, 'wb') as f:
				f.write(img)
			break


