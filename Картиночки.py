def perenochic(a, b):
    img = Image.open(a)
    width, height = img.size
    print((width, height))
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