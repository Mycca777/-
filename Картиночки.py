# 7 задание ------------------------------------------------------------------------------------------
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
        draw.point((j-1, i+1), (186 - c, 25 - a, 155 - b))
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
# 3 задание-----------------------------------------------------------------------------------------------
def perenochic(a, b):
    img = Image.open(a)
    width, height = img.size
    massiv1 = []
    for x in range(width):
        for y in range(height):
            # print((x,y))
            kaka = img.getpixel((x,y))
            pic = (kaka[0], kaka[1], kaka[2], 0)
            img.putpixel((x,y), pic)
    img = img.convert('L')
    img.save(b)
perenochic("Elbrus.jpg", "fl.png")
# 5 задание--------------------------------------------------------------------------------------------------
from PIL import Image
def image_test(im):
    try:
        img = Image.open(str(im))
        return True
    except OSError:
        return False
image_test('Elbrus.jpg')
