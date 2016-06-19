常用第三方模块
PIL（Python Imaging Library） 现在已经用Pillow替代PIL了 因为PIL已经不再维护

    from PIL import Image           # 不能用import image形式
    im_local = 'C:\Users\dell\Documents\GitHub\PythonStudy\py27\N1_Basic\Pic.jpg'
    im = Image.open(im_local)
    print im.format, im.size, im.mode
    im.show()
    im.thumbnail((im.size[0]/2, im.size[1]/2))      # 缩放到50%:
    im.show()

其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全
模糊效果

    from PIL import Image
    from PIL import ImageFilter
    im = Image.open(im_local)
    im2 = im.filter(ImageFilter.BLUR)
    im2.show()


PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图

    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    import random

随机字母:

    def rndChar():
        return chr(random.randint(65, 90))

随机颜色1

    def rndColor():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

随机颜色2

    def rndColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

240 x 60:

    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)          # 创建Font对象
    draw = ImageDraw.Draw(image)                        # 创建Draw对象
    for x in range(width):                              # 填充每个像素
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    for t in range(4):                                  # 输出文字
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    image = image.filter(ImageFilter.BLUR)              # 模糊
    image.show(image)
