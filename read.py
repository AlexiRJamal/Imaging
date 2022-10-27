from PIL import Image

print("Opening image")
img = Image.open('testimage.jpg')
print("Image opened.\nLoading image")
pix = img.load()
print("Image loaded")
print("Converting to list")
pixel_values = list(img.getdata())
print("Saving to file")
f = open('values.txt', 'w')
f.write(str(pixel_values))
f.close()
print("RGB values saved.")