from PIL import Image,ImageFilter
import sys
import os
from os import walk
filenames = next(walk('../image_playground'), (None, None, []))[2] #getting only filenames
#f = []
#for (dirpath, dirnames, filenames) in walk(mypath):
    #f.extend(filenames)
jpg_files=[i if '.jpg' in i else 0 for i in filenames]
jpg_files=list(dict.fromkeys(jpg_files))
jpg_files.remove(0)

for j in jpg_files:
    img = Image.open('./'+j)
    img.save(j.rstrip('.jpg')+'.png','png')


