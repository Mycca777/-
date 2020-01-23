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
from PIL import Image, ImageDraw

myimage = Image.open("Elbrus.jpg")
myimage.resize((1,1))
draw = ImageDraw.Draw(myimage)
width, height = myimage.size
pix = myimage.load()
for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        draw.point((j, i), (255 - c, 255 - a, 255 - b))
myimage
# 9 задание----------------------------------------------------------------------------------------------
from PIL import Image, ImageDraw, ImageFont
def zadanie9(a):
    mode = 'RGB'
    size = 400,400
    img0 = Image.new(mode, size, color = 0).convert('RGBA')
    myname = Image.new('RGBA', img0.size, (255,255,255,0))
    
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(myname)
    draw.text((100,100), "Mycca", font=font, fill=(255,255,255,255))
    
    result = Image.alpha_composite(img0, myname)
    result = result.transpose(Image.FLIP_LEFT_RIGHT)
    result.save(a)
zadanie9("file1.png")
