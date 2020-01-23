# 3 задание ------------------------------------------------------------------------------------------
from PIL import Image, ImageDraw
def gifka(width, height, x, y, size):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((x, y, x + size, y + size), fill='red')
    return img
a= []
x, y = 0, 0
for i in range(10):
    b = gifka(400, 400, x, y, 40)
    a.append(b)
    x += 40
    y += 40
a[0].save('moving_ball.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)
# 4 задание ---------------------------------------------------------------------------------------------
myimage = Image.open(a)
myimage.resize((1,1))
draw = ImageDraw.Draw(myimage)
width, height = myimage.size
pix = myimage.load()
for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        draw.point((i, j), (255 - a, 255 - b, 255 - c))
myimage
