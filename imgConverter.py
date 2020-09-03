import sys

import os
from PIL import Image
print('hello')
inputPath=sys.argv[1]
print(inputPath)
outputPath=sys.argv[2]



if not os.path.exists(outputPath):
    os.mkdir(outputPath)
#  lopp the files in folder images
for file in os.listdir(inputPath):
    openfile = inputPath + file
    img=Image.open(openfile)
    outfile=outputPath+file+'png'
    img.save(outfile,'png')



