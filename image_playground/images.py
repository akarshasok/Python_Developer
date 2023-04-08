from PIL import Image,ImageFilter
img = Image.open('./pikachu.jpg')
img1=Image.open('./astro.jpg')
filt_img=img.filter(ImageFilter.BLUR) #blurs image
shp_img= img.filter(ImageFilter.SHARPEN) #sharpens image
cl_img =img.convert('L') #converts colors
rt_img=img.rotate(180)#rotate
re_img=img.resize((300,300))#resize
img1.thumbnail((400,400)) #making a thumbnail by keeping the aspect ratio
img1.save('thumbnail.jpg')
filt_img.save('blur.png','png') #save file as png because its edited.
shp_img.save('sharp.png','png')
cl_img.save('grey.png','png')
rt_img.save('rt_img.png','png')
re_img.save('re_img.png','png')
#cl_img.show() #shows the image