from PIL import Image

for i in range(0, 50):
    filename = "frame%d.jpg" % i;
    im1 = Image.open(filename)
    im2 = im1.rotate(180)
    im2.save(filename)

