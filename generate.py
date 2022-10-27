import random
from PIL import Image

print("Started.")
width = 1920
height = 1080
im = Image.new('RGB', (width, height))
print("Image created")

print("Generating...")
pixels = im.load()
for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels[x,y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

print("Saving...")
im.save('img2.png')
print("Image saved")

# from PIL import Image, ImageFilter
# import random
# print("Started.")
# width = 10
# height = 10
# data = []
# counter = 1
# img = Image.new('RGB', [width, height], 255)

# def makeImage():
#     print("Generating image...")
#     for i in range(width*height):
#         red = random.randint(0, 255)
#         green = random.randint(0, 255)
#         blue = random.randint(0, 255)
#         data.append((red, green, blue))

#     print("Image generated.")
#     print("Converting to tuple...")
#     thistuple = tuple(data)
#     print("Putting data...")
#     img.putdata(thistuple)
#     print("Saving image...")
#     img.save("img1.png")
#     print("Image 'img1.png' has been saved.")
#     data.clear()

# makeImage()
# img_grey = img.convert("L")
# edges = img_grey.filter(ImageFilter.FIND_EDGES)
# edges.save('img_grey.png')

# with Image.open('testimage.jpg') as img:
#     img.load()
#     img_grey = img.convert("L")
#     edges = img_grey.filter(ImageFilter.FIND_EDGES)
#     edges.save("img_grey.png")