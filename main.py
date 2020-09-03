from PIL import Image, ImageFilter

myImage=Image.open('.\icemountain.jpg')
# newImg=myImage.resize((400,500))

myImage.thumbnail((500,500))
print(myImage.size)

# newImg.save('img300.jpg')

# resizeImage.show()

