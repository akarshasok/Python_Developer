from PIL import Image,ImageFilter
import sys
import os
from os import walk
ip1 = sys.argv[1] #input path
ip2=sys.argv[2] #output path for pictures

if not os.path.exists(ip2):
    os.makedirs(ip2) #creating an op path if it doesnt exist

filenames = next(walk(ip1), (None, None, []))[2] #getting only filenames
#f = []
#for (dirpath, dirnames, filenames) in walk(mypath):
    #f.extend(filenames)
jpg_files=[i if '.jpg' in i else 0 for i in filenames]
jpg_files=list(dict.fromkeys(jpg_files))
jpg_files.remove(0)
for j in jpg_files:
    a= j.rstrip('.jpg')
    img = Image.open('./'+j)
    img.save(f'{ip2}{a}.png','png')

